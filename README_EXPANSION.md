# The world expansion: design and testing

The world of Empire of Zek grew from 55 rooms to 251 in five phases. This file records what each
phase added, the code that changed, how the new content was balanced, and how it was tested. The
original plan and the decisions behind it are in `EXPANSION_PLAN.md`.

| | Before | Now |
|---|---|---|
| Rooms | 55 | 251 |
| Monster types | 51 | 137 |
| Bosses | 6 | 18 |
| Items | 108 | 197 |
| Quests | 6 | 20 |
| Cities | 1 | 4 (Brightwater, Hearthdeep, Silverbough, Sunspire) |

## The shape of the world

Brightwater sits at the centre, with a road out of each gate. Each direction has its own theme
and gets harder the farther you go from town. The Planes of the Gods sit above it all.

| Direction | Theme | Levels | City |
|---|---|---|---|
| North | Northlands, crypt, swamp, Ironspine, Ashen Peaks, Ruins of Elandor | 9-52 | none |
| West | Westmarch farms, then the snowy Rimefells and the Deepdelve Mine | 3-22 | **Hearthdeep** (dwarves) |
| South | meadows and woods, then the ancient Eldergrove | 1-34 | **Silverbough** (elves) |
| East | the Dustway, the Redrock Badlands, then the Scorchsands desert | 8-49 | **Sunspire** (desert traders) |
| Above | the Planes of the Gods, reached from Brightwater's temple | 51-60 | none (endgame) |

- **Several areas per level range:** up to four, so players have variety and, in later lives, a
  different route each time. For example, levels 20-25 are found in the Ironspine, the Deepdelve
  Mine, the Redrock Badlands and the edge of the Eldergrove.
- **Loops:** the regions join up instead of ending in dead ends. The Rimefells connect to the
  Mirefen over a high pass, the Eldergrove reaches the Westmarch quarry, and the Scorchsands
  reach the Ruins of Elandor.
- **Distinct regions:** each region has its own monsters, damage element and gear drops.
- **Respawn:** death always returns you to the Temple of the Dawn in Brightwater.
- **Shops:** Brightwater's shops sell gear up to level 20. Each new city sells gear for its own
  level range:
  - Hearthdeep: dwarven gear for levels 12-24.
  - Silverbough: elven gear for levels 24-34.
  - Sunspire: desert gear for levels 38-44.

Run `python tools/draw_map.py` to draw `map.svg`, a map of every room.

## Phase 1: groundwork and the north (55 to 73 rooms)

- **Room files:** `data/rooms.py` was split into one file per region under `data/rooms/`, plus
  `npcs.py`.
- **Map tool:** `tools/draw_map.py` can draw any number of underground areas as separate boxes.
- **14 new monsters.**

| Region | New rooms | Levels |
|---|---|---|
| Ironspine Mountains | Griffon's Crag, Ogre Quarry, Hill Giants' Steading, Circle of Red Hands, Rimeglass Gorge, Rime Glacier, Jarls' Mead-Hall | 22-34 |
| Mirefen | Spawning Grounds, Bogwood Hollow, Leech Fens | 18-21 |
| Ruins of Elandor | Silvered Gardens, Sunken Amphitheatre, Hall of the Moon Court | 34-40 |
| Ashen Peaks | Meltwater Gorge, Smoking Scree, Burning Fields, Drake Roost, Forge of the Dragon Cult | 37-47 |

The Meltwater Gorge and Smoking Scree now sit between the Frost Throne and the Ashen Waste. They
fill the old jump from level 34 straight to 41.

## Phase 2: the west and Hearthdeep (73 to 110 rooms)

**Totals:** 14 new monsters, 20 new items and 4 new quests.

| Area | Rooms | Levels | What's there |
|---|---|---|---|
| West Gate | 1 | safe | Off Brightwater's North Gate |
| Westmarch | 8 | 3-10 | Farms, Thornbury hamlet, a goblin-infested quarry, the hill road |
| Rimefells | 12 | 10-20 | Snow wolves, frost goblins, ice spiders, yetis, frost wisps, snow trolls; a high pass east to the Mirefen |
| Hearthdeep | 10 | safe | The dwarven hold |
| Deepdelve Mine | 6 | 18-21 | Below Hearthdeep. Boss: **Ghaldrek the Stonewake** (21) |

- **Hearthdeep's people:**
  - Brakka Ironhand, Durgan's sister, sells dwarven arms and armour.
  - Tamsin Runecutter sells rune gear for casters.
  - Gilda Barrelbrew runs the alehouse and sells potions.
  - Captain Orla gives a quest to collect yeti fur.
  - Thane Hargrim gives a quest to kill the Stonewake.
- **How players find it:**
  - Captain Halvard's quest Trouble in the Rimefells (level 11) sends players west.
  - Durgan's greeting mentions his sister in Hearthdeep.
  - Farmer Haverick gives a level 5 quest in Thornbury.
- **Shop move:** Brightwater's level 22-24 stock now sells in Hearthdeep instead. That's the
  mithril sword, hunter's recurve, mithril hauberk, starsilk hood, wand of embers and tome of
  warding.

## Phase 3: the south and Silverbough (110 to 145 rooms)

**Totals:** 12 new monsters, 22 new items and 4 new quests.

| Area | Rooms | Levels | What's there |
|---|---|---|---|
| Greenmeadow | 1 | 2-4 | The Willow Mill |
| Whispering Woods | 2 | 8-10 | Fern Gully and the Old South Way, with brown bears |
| Eldergrove | 22 | 20-34 | Centaurs, owls, wood trolls, thorn sprites, greatstags, blighted treants, rotwood druids, blight wolves, gloom dryads. Boss: **Rotheart, the Blighted Oak** (33) |
| Silverbough | 10 | safe | The elven city in the trees |

- **Two ways in:** the Eldergrove is reached from the Old South Way in the Whispering Woods, and
  from the Westmarch quarry through its western arm.
- **Silverbough's people:**
  - Speaker Saelwyn gives a quest to kill Rotheart.
  - Warden-Captain Faelan gives two quests: cull the blighted stags, then hunt the rotwood druids.
  - Ilyra Leafsong sells elven arms and armour.
  - Caelum Moonweave sells caster gear.
  - Merewyn runs the inn and sells potions.
- **How players find it:** Elowen in Brightwater's Silverthread Arcana gives The Blight Spreads
  (level 24), which sends players south.

## Phase 4: the east and Sunspire (145 to 201 rooms)

**Totals:** 21 new monsters, 27 new items and 6 new quests.

| Area | Rooms | Levels | What's there |
|---|---|---|---|
| East Gate | 1 | safe | Off Brightwater's South Road |
| Dustway | 7 | 8-15 | Hyenas, highwaymen, gnolls, and the safe Dustway Waystation |
| Redrock Badlands | 10 | 18-27 | Gnolls, scorpions, wyverns, dust devils. Boss: **Yellowtooth, Gnoll Warlord** (26) |
| Scorchsands | 20 | 35-49 | Raiders, dune scorpions, salt wraiths, mirage stalkers, djinn, sand giants, great sandworms |
| Sunspire | 12 | safe | The walled desert city around its great obelisk |
| Tomb of the Sand Kings | 6 | 45-48 | Below a sunken pyramid. Boss: **Ussreth, the Last Sand King** (48) |

- **Two ways into the desert:** north from the Badlands, and down the stair below Elandor's Sunken
  Amphitheatre into the buried elven quarter.
- **New people:**
  - Old Marta (Dustway Waystation) gives two quests: kill highwaymen, then Yellowtooth.
  - Emira Zahrin (Sunspire) gives a quest to kill the last Sand King.
  - Sun-Captain Idrisa (Sunspire) gives a quest to kill sand giants.
  - Archivist Mehrun (Sunspire) gives a quest to collect desert glass.
  - Zahir the Bladewright (Sunspire) sells sunsteel arms and armour.
  - Amsa Silkwind (Sunspire) sells silk caster gear.
  - Nadim the Caravan-Master (Sunspire) sells potions, including supreme potions.
- **How players find it:** Sister Aveline's quest The Thirsting Dead (level 36) sends players to
  Sunspire.

## Phase 5: the Planes of the Gods (201 to 251 rooms)

### What was added: 50 rooms, levels 51-60

| Tier | Plane | Levels | Boss |
|---|---|---|---|
| - | Threshold of the Gods (2 safe rooms, with the Herald, who explains the way) | safe | - |
| 1 | Sky, Growth, Fear | 51-55 | Caelestra the Sky-Warden, Verdis the Wildmother, Vhaal the Dreadmaker (55) |
| 2 | Fire, Water, Earth, Air | 54-58 | Ignaros, Nerevos, Ulmathra, Zephyrion (58) |
| 3 | Time | 57-60 | **Lord Zek, Ruler of All (60)** |

- **Getting there:** a stair behind the altar of the Temple of the Dawn in Brightwater climbs up
  to the Threshold.
- **The second tier:** each first-tier plane leads on to its elements. Sky leads to Air, Growth
  to Earth and Water, and Fear to Fire.
- **The Door of Time:** it opens only once the character has killed all four elemental lords. If
  it is still shut, it tells you which lords remain.
- **Lord Zek's throne:** it opens only for a character who has lived every class to level 50. The
  current class counts once it reaches 50. The door lists the classes still missing.
- **The rest of the planes:** open to anyone who can survive them.
- **Rewards:**
  - The plane bosses and Lord Zek drop 17 mythic level-50 items, including Zek's sword Eternity,
    the Crown of Zek and the Hourglass Amulet.
  - Killing Lord Zek adds the title **"Champion of Zek"** to the score sheet.
  - Characters below level 50 in later lives get large amounts of XP from plane monsters, if they
    are strong enough to survive them.

Files: `data/rooms/planes.py` (rooms), the end of `data/monsters.py` (monsters and bosses), the
"Mythic gear" section of `data/items.py`, and the Herald in `data/rooms/npcs.py`.

### Code changes

Phases 1-4 were data only. Phase 5 was the first to need game code.

- **Room gates:** a room can carry a `gate` (see `R()` in `data/rooms/common.py`):
  - `{"kills": [boss ids], "msg": ...}` requires the character to have killed every listed boss.
  - `{"all_classes": True, "msg": ...}` requires every class to have been lived to level 50.

  `Game.gate_block()` checks gates on normal movement and when fleeing. The dev command `goto`
  ignores them.
- **Kill record:** `Character.boss_kills` records every boss the character has ever killed, kept
  across rebirths. Old saves load with an empty list.
- **Mastered classes:** `Character.mastered_classes()` returns the past lives plus the current
  class once it is at level 50.
- **Title:** the score sheet shows "Champion of Zek" once `lord_zek` has been killed.
- **Balance simulator:** a new endgame mode, `python tools/balance_sim.py endgame`, tests level-50
  characters with 1, 6 and 11 lives lived, using best-in-slot gear.
- **Data check:** `tools/validate.py` now checks that gates only require bosses and that every
  gate has a refusal message.
- **Map:** `tools/draw_map.py` draws all the planes together in one box on the right of the map.

## Balance

### Levels 1-50 (phases 1-4)

Every new monster was compared with existing monsters of the same level, using the real combat
code with every class and best-in-slot gear. New monsters cost about the same HP per fight as
their neighbours.

- **Toughened after testing:**
  - The dragon cult flamecaller was too easy, so it was made tougher. It is still slightly
    easier than its neighbours, but it heals itself.
  - The scarab swarm was too easy, so it was made tougher.
- **The new world bosses** were tested at their own level and at their level +3, with 5 potions:

| Boss | Level | Compared with |
|---|---|---|
| Ghaldrek the Stonewake | 21 | about as hard as Varnoth and Old Mother Gristle |
| Yellowtooth, Gnoll Warlord | 26 | about as hard as Warlord Gorrak |
| Rotheart, the Blighted Oak | 33 | about as hard as Gorrak and Seluvar |
| Ussreth, the Last Sand King | 48 | between Seluvar and Pyraxis |

### The Planes (phase 5)

Win rates from `balance_sim.py endgame`, for level-50 characters averaged over all classes. Boss
fights use 5 potions.

| Fight | 1 life | 6 lives | 11 lives |
|---|---|---|---|
| First-tier monsters | about 50% (they kill you half the time) | trivial | trivial |
| Plane champions | 0% | 89-98% | 100% |
| Elemental lords | 0% | 27-65% | 100% |
| Lord Zek | 0% | **0%** | **68-75%** (every class 50-90%) |

- **Without mythic gear:** an 11-life character with no mythic gear at all still beats Zek about
  60% of the time. Good equipment matters but is not strictly required.
- **Why the multipliers are so large:** past-life stat bonuses make multi-life characters
  enormously strong. A 6-life character already beat a standard level 60 boss every time, so plane
  monsters use much bigger multipliers than anything else in the game:

  | Monsters | HP multiplier | Damage multiplier |
  |---|---|---|
  | Regulars | 3.3-5.5 | 2.6-3.6 |
  | Plane bosses | 7.5-11 | 3.3-3.9 |
  | Lord Zek | 15 | 5.3 |

  This is also recorded in `CLAUDE.md`.
- **Tuning changes during testing:**
  - Lord Zek was too hard at first (41% with 11 lives). His HP went from 18 to 15 and his damage
    from 5.6 to 5.3.
  - The first-tier regular monsters were too easy for a 1-life character (50-84% wins), so they
    were toughened.
  - The Lords of Water and Earth were softer than Fire and Air, so they were toughened.

## Testing

All testing was done in a copy of the game outside this folder (`%TEMP%\zektest`), so `saves/`
was never touched.

### Every phase

| Check | Result |
|---|---|
| Data check (`python tools/validate.py`) | Passes after every phase. Final: 251 rooms, 137 monsters (18 bosses), 197 items, 20 quests |
| Map (`python tools/draw_map.py`) | No rooms overlap, so the geography is consistent in every region |
| Room split (phase 1) | The world data was identical before and after splitting `data/rooms.py` |
| New monsters | Compared with existing monsters of the same level for every class |
| Walks | Every new room and loop walked in the real game, including all four cities and the boss rooms |
| NPCs | Every new NPC's quest or shop list checked |
| Your saves | Copies of both characters (Zek and Zekariah) loaded after every phase, finally with all 251 rooms |

### The Planes (phase 5)

| Check | Result |
|---|---|
| Door of Time | Refuses entry and lists the missing lords; opens once all four are killed |
| Lord Zek's throne | Refuses entry and lists the missing classes, including the current class below level 50; opens when every class is mastered |
| Kill record | Bosses are recorded on kill; ordinary monsters are not |
| Title | "Champion of Zek" appears on the score sheet after killing Lord Zek |
| Saves | The kill record survives a save round trip; old saves without it load with an empty list |
| Rooms | All 50 plane rooms are reachable by walking from the temple with the game's own movement |
| Live game | A scripted run through the real game loop (temple, stair, Threshold, the Herald, the Door of Time) worked |

### Re-running the checks

```
python tools/validate.py
python tools/draw_map.py
python tools/balance_sim.py fights
python tools/balance_sim.py bosses
python tools/balance_sim.py endgame --n 10
```

- **`validate.py`:** run after any change to `data/`.
- **`draw_map.py`:** run after adding rooms. It stops with an error if two rooms land on the same
  square.
- **`balance_sim.py fights` and `bosses`:** cover levels 1-52.
- **`balance_sim.py endgame`:** lists every monster above level 50 with its win rate for 1, 6 and
  11 lives, plus the worst class at 11 lives. Re-run it after changing plane monster multipliers,
  class stat growth or mythic gear.

## Documentation

- **`README.md`:** the player-facing manual. Its world section and quest list cover everything
  above.
- **`CLAUDE.md`:** notes for development: the room package, gates and boss kills, the endgame
  balance targets, and the map tool.
- **`EXPANSION_PLAN.md`:** the original plan, the decisions made along the way, and a progress
  log for each phase.
- **`map.svg`:** the finished world.

Nothing has been committed.
