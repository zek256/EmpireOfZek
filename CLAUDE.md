# Empire of Zek

Offline single-player text MUD in pure Python 3, standard library only (no dependencies, no network).
`README.md` is the player-facing manual; keep it in sync when gameplay or commands change.

## Running and testing

```
python main.py                 # play
python main.py --dev           # adds setlevel <n>, goto <room_id>, addgold <n>, give <item_id>
python main.py --tick 0.5      # faster game clock (default 4s) for testing
python main.py --no-color --seed 3
```

There is no build step and no unit test suite. Verify changes by:
- **Data check**: `python tools/validate.py` after any edit to `data/`. It checks two-way exits,
  that every room is reachable, spawns, loot, shops, quests (givers, prereqs, collectable targets),
  class gear and ability classes, and exits 1 on errors.
- **Balance**: `python tools/balance_sim.py [fights|endurance|bosses|endgame|unlock|gear] [--n 30] [--levels 1,12,30]`
  runs every class through the real `Combat` code with output silenced. The tuning targets are
  in its docstring. It fights one monster at a time with best-in-slot gear, so it is optimistic.
  Re-run it after touching combat formulas, monster multipliers or class growth.
- **Map**: `python tools/draw_map.py [out.svg]` redraws `map.svg` (every room, exits, areas, levels,
  bosses) after room changes. It lays rooms on a grid from their exits and exits with an error if
  two rooms land on the same square, so it doubles as a geography check for new regions. Areas
  that would overlap the surface (dungeons below, realms above) go in the `INSETS` list in
  `mapview.py` and are drawn as separate boxes. New areas need a colour in its `COLORS` table.
  The same layout drives the in-game `map` / `automap` (`mapview.py`), which shows one layer
  (the surface or one inset) at a time.
- **World expansion**: `EXPANSION_PLAN.md` holds the agreed plan (regions, level ranges, phases).
- **Scripted play**: pipe commands into `main.py`. Piped input arrives instantly, so no game ticks
  pass between lines. Combat rounds and sleep need real time, so for those drive the game with
  delays between lines (a small `subprocess` script that writes a line, sleeps, writes the next)
  together with `--tick 0.3`.
- **Direct calls**: import `game.Game` with a `Character`, stub `ui.say/out/rule` to no-ops, and
  call methods (`cmd_attack`, `attempt_flee`, `world_tick`) to check logic without the clock.

**Always test in a copy outside this folder** (e.g. `%TEMP%\zektest`, copy `*.py` and `data/`).
The user plays from this folder, and `saves/` holds their real characters. Never delete,
overwrite or "clean up" anything in `saves/`. Windows can't launch Python from very long paths,
so keep the temp path short.

Git: the user commits manually. Don't run `git init`, commit or connect remotes unless asked.

## Architecture

```
main.py       CLI flags, title menu; starts ui's input thread; sets game.TICK_SECONDS
game.py       Game: command dispatch, game clock, exploration, quests, find, aliases, shops,
              sleep, rebirth, save/load, character creation
character.py  Character (stats, HP/mana, XP, abilities, equipment, rebirth) and Pet
combat.py     Combat: one round per tick, ability resolution, monster AI, rewards
world.py      MonsterInstance, Room (spawning + aggression rule), World (respawns, persistence)
ui.py         colour, wrapping, background stdin reader, prompt tracking
mapview.py    room grid layout (shared with tools/draw_map.py), text map and automap rendering
data/         all content as plain Python data (races, classes, abilities, items, monsters, quests)
data/rooms/   one module per region, each with a ROOMS dict, merged in __init__ (REGIONS list,
              duplicate ids raise); NPCs in npcs.py; START_ROOM/RESPAWN_ROOM in __init__
```

### The game clock (game.Game.run)
- A daemon thread reads stdin into a queue (`ui.start_input`). The main loop waits on that queue
  until the next tick: either a typed line arrives (`handle`) or the tick fires (`game_tick`).
- A tick is a combat round (`Combat.round`) when fighting, otherwise `world_tick`: awake regen
  (2% HP and 3% mana) or sleep (10%), effect and cooldown timers, respawns.
- **Never call `input()`.** It races the reader thread. Use `game.ask()` / `ui.read_line()`.
  The clock pauses during `ask()` prompts (menus, quit and rebirth confirmations).
- Moving does **not** advance time. Only ticks do.
- Speedwalking (`cmd_run`, `parse_path`, `walk_step`): `run nnes` or a bare path word like `3n2e`
  that isn't a command or alias. The first step is immediate; the rest sit in `Game.walk` and
  the main loop takes one every `WALK_SECONDS` (0.5), a second timer beside the tick. Any typed
  line stops it ("You stop."), as does `check_aggro` finding an attacker; in combat only the
  first step is used, as a flee. `run` is not a flee alias (by the user's choice). Direct
  `handle()` calls only take the first step: call `walk_step()` yourself for the rest.

### Combat flow
- `kill X` or an offensive spell out of combat calls `start_combat`. The first action resolves
  immediately and `reset_clock()` gives a full tick before round 2.
- In combat, typed actions don't act right away. `Combat.queue()` stores one action
  (spell/ability/potion/flee), and the next `round()` runs it in place of the auto-attack.
  Queued abilities are re-validated when they fire (`ability_round`).
- A second slot, `Combat.held`, keeps one ability that was used while still cooling down
  (`use_ability` calls `Combat.hold` instead of refusing). Each `round()` first tries
  `fire_held()`: once off cooldown it fires and takes the round, leaving `queued` for the next
  round; if `ability_error` fails then (usually mana) it is dropped. Stuns delay both slots.
- `end_round`: player effects tick, pet attacks, aggressive room monsters join, monsters act,
  monster effects tick, mana regen, cooldowns, world respawn tick, then death/victory checks.
- Effect timing gotcha: effects the player applies to themselves are created with `fresh: True`
  so the end-of-round tick doesn't eat a turn. Monster-applied effects must **not** be fresh.
  Player stuns are applied during the monster phase, after the player tick, so they last
  into the next round. Monster stuns are consumed when the monster tries to act.
  Cooldowns are set to `cooldown + 1` in combat for the same reason.
- `level_gap_mult` scales damage both ways by level difference. Monsters below the player
  also miss more.

### Aggression rules (deliberately rare, Aardwolf-style)
- Template flag `aggro` in `data/monsters.py`: only undead, demons, elementals, guards,
  cultists and bosses. Animals and roaming humanoids are passive.
- `Room.spawn` enforces the per-room rule: a room containing a boss makes **every** monster
  aggressive. Any other room allows at most `max_aggro` (default 1) aggressive instances, and
  extras spawn passive. Aggression is per instance and is not saved; it is recomputed on load.
- Aggressive monsters ignore players more than `AGGRO_GAP` (6) levels above them.
- Attacking a passive monster fights only that one. Passive neighbours never join, but
  aggressive monsters in the room do.
- `Game.leave_room()` (called from `go()` and `player_died()`) restores every monster in the room
  being left to full HP and clears its effects. Monsters have no other regeneration.

### Player and progression
- Stats are **derived, not stored**: race base + class start + class gains x (level-1) + rebirth
  bonus + gear + buffs. Only level, XP, gear, effects etc. are persisted.
- HP and mana formulas live in `Character.max_hp/max_mana`. XP per level is
  `100 * level^1.5`, identical in every life (no rebirth penalty, by the user's choice).
- Rebirth (level 50): the old class's full stat gains (gains x 49) are appended to `past_lives`
  and phase in as `total * level / 50`. Abilities of every lived class stay known and unlock
  at their original level. Gear above level 1 is unequipped.
- Race perks are keys in `RACES[...]["perks"]` read via `Character.perk()`: hp_mult,
  mana_mult, dmg_mult, crit, dodge, regen_mult, immune, xp_mult (supported, currently unused).
- Ability power = `base + lvl*level + scale*stat`. Spell cost scales `cost * (1 + 0.1*(level-1))`.

### Monsters
Templates only set multipliers. Real HP, damage and armor come from level in `MonsterInstance`
(`(20 + 15L)` HP etc.). To make a monster tougher, change its multipliers, not raw numbers.
Specials: big / dot / stun / drain / heal. Bosses respawn after 120 ticks, others after 30.
Monsters above level 50 (the Planes of the Gods) use far larger multipliers (hp 3.3-5.5, dmg
2.6-3.6 for regulars; 7.5-11 / 3.3-3.9 for plane bosses; Lord Zek 15 / 5.3) because past-life
stat bonuses make multi-life characters enormously strong.

### Gates and boss kills
- A room may carry `gate` (see `data/rooms/common.R`): `{"kills": [boss ids], "msg"}` or
  `{"all_classes": True, "msg"}`. `Game.gate_block(rid)` checks it in `cmd_move` and when
  fleeing; `goto` ignores it. `validate.py` checks gate kills are bosses.
- `Character.boss_kills` records every boss id ever slain (set in `Game.on_kill`, kept across
  rebirths). `Character.mastered_classes()` = past lives + the current class once at level 50.
- The Door of Time needs the four elemental lords; Lord Zek's throne needs every class mastered.
  Killing `lord_zek` shows the "Champion of Zek" title on the score sheet.

### Inventory and items
- Inventory is a flat list of item ids (duplicates = quantity). Equipment is `{slot: id}` over
  `items.SLOTS` (one ring slot).
- Armor and weapon training: every weapon and armor item has a `kind` (a `WEAPON_KINDS` family,
  an `ARMOR_TIERS` tier, `shield`, or the free kinds `offhand`, `jewelry`, `any`). Classes set
  `armor` (heaviest tier), `shield` and `weapons`. `Character.trained_for` takes the union over
  `lived_classes()`, so training survives rebirth (the user wants that as a reason to live a plate
  class). `load_game` moves untrained gear from old saves into the pack. `validate.py` checks kinds
  fit slots and that starting gear is allowed; `balance_sim.py gear` shows each tier's best
  armor by level (look for gaps when adding items), and `unlock` measures a plate past life.
- Loot and gold go straight into the inventory on kill. Ground items only come from `drop`.
- Sell price is always `value // 3`. Buy price = `value`.

### Quests, NPCs, find
- Quests are `kill` (counted in `on_kill`) or `collect` (counted from inventory, removed on
  turn-in). They are offered and turned in through `talk`. `prereq` and `min_level` gate them.
- `find` runs a BFS over room exits to the nearest room that *spawns* the target (or the quest
  giver once ready). It doesn't check whether the monster is currently alive.

### Player aliases
Stored in `Character.aliases` and saved. They are expanded once at the top of `handle()`,
with extra words appended. `reserved_words()` (every `cmd_*`, `ALIASES`, directions, `go`)
can never be aliased, and an alias can't start with another alias.

## Conventions

- New command: add `cmd_<name>(self, args)` to `Game`. It is picked up automatically. Add short
  forms to `Game.ALIASES`, and add it to `NO_COMBAT` / `SLEEP_OK` if relevant, to the `HELP`
  table and to the README.
- Content goes in `data/` via the helper constructors (`weapon()`, `armor()`, `M()`, `R()`,
  `spell()`, `ability()`). Room exits must be two-way.
- All output goes through `ui.say` (wrapped), `ui.out` (raw) or `ui.rule`. Never use `print`
  directly: `ui._emit` tracks the open prompt and starts on a fresh line under it.
- Combat lines are not indented, and the round shows no HP/mana bar row (user preference).
  HP, mana and level % live in the prompt.
- Text tone is high fantasy. Room descriptions are 2-4 sentences.
- Save format: `saves/<name>.json` = `{version, player, room, world}`. New `Character` fields
  need a default in `from_dict` (see `aliases`) so old saves still load.

## Balance notes

Tuned with `tools/balance_sim.py`: same-level fights cost roughly 25-55% HP, and bosses are
beatable at level+3 with potions. Necromancer, with its pet and drain, is the strongest solo
class. That is intended. Wizards are fragile and get no area spell until Fireball at 16.
With armor training, wizards rely on Mana Shield (strengthened to 15 + 4.5/level + 1.3 INT when
cloth-only gear went in); they now clear ordinary fights with lots of HP to spare but are 70-90%
against bosses at the boss's own level. Bards used to be too slow to kill bosses (30+ rounds);
Discordant Note was raised to 10 + 2.4/level + 0.8 CHA and their unused INT gain became DEX.
They now win 55-100% of boss fights at the boss's own level (the Bog Hag, about 40%, is the
hardest) and essentially all at +3.

Endgame (`balance_sim.py endgame`, level-50 characters with 1/6/11 lives, best-in-slot gear):
first-tier plane monsters beat a 1-life character about half the time and are trivial with 6
lives; plane champions are ~90-100% with 6 lives; elemental lords ~30-65% with 6 lives and 100%
with 11; Lord Zek ~0% with 6 lives and ~65-75% with 11 (every class 50-90%), about 60% without
any mythic gear. The user asked for Zek to need a full every-class character with good gear.
