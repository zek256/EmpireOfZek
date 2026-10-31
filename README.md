# Empire of Zek

An offline, single-player, text-based fantasy MUD/RPG in pure Python 3 (standard library only).

Begin in the town of Brightwater, clear rats from the inn cellar, hunt wolves in the Whispering
Woods, break the bandit chieftain, descend into the Crypt of Varnoth, aid the dwarves of Hearthdeep
in the snowbound west, and fight your way through the Mirefen, the Ironspine Mountains and the
haunted Ruins of Elandor to the lair of Pyraxis the Eternal Flame. At level 50, be **reborn** as a new class and carry your past lives with you.

## Running

Open a terminal in this folder (in File Explorer, click the address bar, type `cmd` and press Enter) and run:

```
python main.py
```

Requires Python 3.8+. No installation, no network.

Options:

| flag | effect |
|---|---|
| `--no-color` | disable ANSI colours (also honours the `NO_COLOR` environment variable) |
| `--seed N` | fixed random seed, for reproducible runs |
| `--tick S` | seconds per game tick (default 4) |
| `--dev` | enables test commands: `setlevel <n>`, `goto <room_id>`, `addgold <n>`, `give <item_id>` |

Saves are written as JSON to `saves/<name>.json`.

## Commands

| command | what it does |
|---|---|
| `look` / `l` [thing] | describe the room, or look at a monster, person or item |
| `n` `s` `e` `w` `u` `d` (or `north`, `go north`...) | move |
| `exits` | list exits and where they lead |
| `attack` / `k` / `kill` <target> | start a fight (`k rat`, `k 2.wolf` for the second wolf); during a fight, switch targets |
| `cast` / `c` <spell> [target] | cast a spell (`cast magic missile rat`, `c fireball`); in a fight it is used on the next round |
| `ability` / `ab` <name> [target] | use a class ability (`ab slam`, `ab cleave`); in a fight it is used on the next round |
| `spells` / `abilities` | list all known spells and abilities, with locked ones greyed out |
| `consider` / `con` <target> | judge a monster's danger (colour-coded by level) |
| `flee` [dir] | try to escape combat (moving during combat also attempts to flee) |
| `inventory` / `i` | what you carry |
| `equipment` / `eq` | what you wear |
| `wear` / `wield` / `equip` <item> | equip an item (level requirements apply) |
| `remove` <item or slot> | take something off |
| `use` / `drink` <potion> | drink a potion (in a fight it replaces your next round's attack) |
| `examine` / `x` <item> | item details, compared with what you have equipped |
| `get` <item> / `get all` / `drop` <item> | pick up / drop |
| `talk` <person> | talk to NPCs; this offers and turns in quests |
| `quests` / `journal` | quest log |
| `find` <quest name, number, or monster> | shortest route to your quest target (or the quest giver once it's done), e.g. `find vermin` prints `wd`. With one active quest, plain `find` works. Also `track` / `where` |
| `list`, `buy [qty] <item>`, `sell [qty or all] <item>`, `sell junk` | trade with merchants: Durgan Ironhand (weapons and armor, smithy), Elowen Silverthread (cloth, wands, orbs and rings for casters, west off the South Road), Mirela (potions) |
| `sleep` / `rest` | fall asleep and recover 10% of max HP and mana every tick (not with hostile monsters nearby) |
| `wake` / `stand` | get up (you also wake automatically when fully rested, or when attacked) |
| `pet` / `pet dismiss` | inspect or release your summoned companion |
| `stats` / `score` | full character sheet |
| `level` | XP progress and upcoming abilities |
| `rebirth` | at level 50, be reborn as a new class |
| `alias <word> <command>` | create a shortcut: after `alias mm cast magic missile`, typing `mm` casts it (`mm rat` targets the rat). Built-in commands and directions can't be overridden. `alias` lists yours, `unalias <word>` removes one. Aliases are saved with your character. |
| `save`, `load`, `quit`, `help` | system |

The prompt shows your HP, mana and progress toward your next level in gold
(e.g. `<192/192 hp (100%) 350/350 mana (100%) EXP: 3%>`). In combat it adds your target's
remaining health in red `TARGET: 56%`, and `[ASLEEP]` while sleeping.
In room listings monsters are coloured by danger relative to your level
(grey/green/blue easy, white even, yellow/red dangerous), and `(!)` / `(?)` mark NPCs with a quest to
offer or turn in.

## Time and combat

The world runs on a real-time clock: every **4 seconds** is one game tick.

- **Combat:** `kill <target>` starts a fight, and your first attack lands at once. After that, one
  combat round happens every tick, and you automatically attack your current target each round.
  A spell, ability, potion or flee you type is queued and replaces the auto-attack on the next round.
  Moving during a fight also tries to flee.
- **Who attacks on sight:** aggressive monsters are rare. Only undead, demons, elementals, guards,
  cultists and bosses attack you as soon as you enter their room, and outside boss rooms at most
  one monster per room does. In a boss room, everything attacks. Animals and roaming humanoids
  (wolves, spiders, kobolds, lizardfolk, orcs...) leave you alone and only fight the one you
  attack; the others in the room stay out of it. `consider` tells you whether a monster will
  attack on sight.
- **Sleep:** while asleep you recover 10% of your max HP and mana each tick. You can't move or
  fight, but you can check `stats`, `inventory` and so on. You wake when fully rested, when
  attacked, or when you type `wake`.
- **Monsters** don't regenerate. Instead, when you leave a room (walking out, fleeing or dying),
  every monster in it recovers to full health and loses any stuns or damage-over-time effects.
  A boss has to be beaten in one go.
- **Awake:** outside combat you slowly regenerate (2% HP and 3% mana per tick). Spell cooldowns,
  buffs and monster respawns all count in ticks.

## Races and classes

**Races:** human (+5% HP, mana and damage), high elf (+12% mana), elf (dodge/crit), dark elf (crit), gnome (mana/dodge),
ogre (+12% HP), troll (regeneration), undead (immune to poison/disease), orc (+6% damage).

**Classes:** warrior, cleric, wizard, bard, necromancer, shaman, druid, rogue, ranger, paladin,
shadow knight. Each has its own HP and mana growth, casting stat, attack stat, per-level stat
gains, and 6-7 spells/abilities unlocked between levels 1 and 48:

- Warrior: Slam, Battle Cry, Second Wind, Cleave, Shield Wall, Rampage, Avatar of War
- Cleric: Minor Healing, Smite, Divine Aegis, Greater Healing, Holy Wrath, Resurgence, Sunburst
- Wizard: Magic Missile, Frost Bolt, Mana Shield, Fireball, Lightning Lance, Meteor
- Necromancer: Lifetap, Raise Skeleton (pet), Plague, Bone Spear, Siphon Soul, Bone Colossus, Wail of the Damned
- Shaman: Frost Shock, Ancestral Mending, Spirit Wolf (pet), Spirit of the Bear, Serpent Venom, Chain Lightning, Ancestral Avatar
- Druid: Thornlash, Regrowth, Entangling Roots, Moonfire, Barkskin, Starfall, Wrath of the Wild
- Rogue: Backstab, Poisoned Blade, Evasion, Kidney Shot, Eviscerate, Shadow Dance, Assassinate
- Ranger: Aimed Shot, Hunter's Mend, Multishot, Bonded Wolf (pet), Serpent Sting, Rain of Arrows, Deadeye
- Paladin: Holy Strike, Lay on Hands, Blessing of Might, Divine Shield, Hammer of Justice, Consecration, Avenging Wrath
- Shadow Knight: Shadow Strike, Disease Cloud, Dread Aura, Harm Touch, Vampiric Embrace, Death Coil, Unholy Frenzy
- Bard: Discordant Note, Ballad of Mending, Lullaby, War March, Dirge of Despair, Crescendo, Legend's Anthem

Spells cost mana, and the cost scales with level. Abilities are free but have cooldowns. Both are
learned automatically on level up.

## Character maths

- **HP** = 10 + (class HP + 3) x level + CON x level x 0.2 (x racial modifier)
- **Mana** = 15 + class mana x level + casting stat x level x 0.1 (x racial modifier)
- **Stats** = race base + class starting bonus + class gains x (level - 1) + rebirth bonus + gear
- **XP to next level** = 100 x level^1.5, the same in every life no matter how many rebirths
- Monsters far below your level give little XP and hit you less. Fighting above your level gives
  bonus XP and is dangerous.

## Rebirth

At level 50, `rebirth` lets you choose any other class:

- Level and XP reset to 1 / 0.
- You keep **every ability of every class you have lived**. Each becomes usable again when your
  current level reaches the level at which it was originally learned (a warrior-turned-wizard gets
  Slam back at level 1, Cleave at 12, Avatar of War at 42).
- The **full stat gains of each previous class at level 50** become a permanent bonus. It phases
  in as you level (bonus x level / 50), so it stacks across rebirths and reaches full strength at 50.
- Gear above level 1 is unequipped until you can wield it again, so you climb back up with your
  new class's starting gear. Experience needed per level is exactly the same as in your first life.

## World

Town of Brightwater (inn, temple, smithy, alchemist, Silverthread Arcana caster shop, barracks,
and the North and West Gates), Greenmeadow (1-5), Whispering Woods and the bandit camp (4-10),
the Westmarch farms and goblin quarry (3-10), Barrowfield and the Crypt of Varnoth dungeon (9-17),
the snowy Rimefells (10-20) around the dwarven city of **Hearthdeep** (smith, rune-carver, alehouse
with potions) and the Deepdelve Mine below it (18-21), the Mirefen (15-22), the ancient Eldergrove
(20-34) around the elven city of **Silverbough** (bladesmith, moonweaver, inn with potions), reached
south through the Whispering Woods or from the Westmarch quarry, the Ironspine Mountains with the
orc warcamp, the giants and the frost caverns (20-34), the Ruins of Elandor (32-41), and the Ashen
Peaks up to the dragon's lair (37-52). Brightwater's shops sell gear up to level 20; Hearthdeep
sells dwarven gear for levels 12-24 and Silverbough elven gear for levels 24-34.
That is 145 rooms, 91 monster types including 8 bosses, and 152 items. Run
`python tools/draw_map.py` to draw `map.svg`, a map of every room.

**Quests:** Vermin in the Cellar (Bram, inn), Wolves at the Gate, The Bandit Chieftain, Trouble in
the Rimefells, The Skullsplitter Horde (Captain Halvard, barracks), The Bone King and The Hag of the
Mirefen (Sister Aveline, temple), The Blight Spreads (Elowen, Silverthread Arcana), Goblins in the
Henhouse (Farmer Haverick, Thornbury), Fur for the Gatewatch (Captain Orla, Hearthdeep), The
Stonewake (Thane Hargrim, Hearthdeep), The Sacred Herd and The Rotwood Circle (Warden-Captain
Faelan, Silverbough) and The Heart of the Blight (Speaker Saelwyn, Silverbough).

Dying returns you to the temple with half HP, losing 10% of the XP needed for your level and 10% of
your gold.

## Code layout

```
main.py          entry point, title menu, CLI flags
game.py          command parser, game clock, exploration, quests, find, aliases, shops, rebirth, save/load
character.py     Character (stats, HP/mana, levelling, abilities, equipment, rebirth, aliases) and Pet
combat.py        tick-based combat rounds, ability resolution, monster AI, XP/loot rewards
world.py         rooms, monster instances, respawning, world persistence
ui.py            colour, word wrap, background input reader
data/races.py    races and racial perks
data/classes.py  classes, stat growth, starting gear
data/abilities.py  all spells and abilities
data/items.py    weapons, armor, caster gear, potions, trophies
data/monsters.py monster templates, special attacks, loot tables
data/rooms/      the world map, one file per region, plus npcs.py
data/quests.py   quests
tools/           validate.py (data check), balance_sim.py, draw_map.py (draws map.svg)
```

Adding content is data-only: add a room to its region's file in `data/rooms/`, a monster to
`data/monsters.py`, an ability with `spell(...)` / `ability(...)` in `data/abilities.py`, and so on.
A new region file must also be listed in `REGIONS` in `data/rooms/__init__.py`.
