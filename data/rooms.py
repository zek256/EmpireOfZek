"""The hand-crafted world of Brightwater and the lands around it.

Each room: name, area, desc, exits {dir: room_id}, spawns [(monster_id, count)],
npcs [npc_id], safe (no combat / free resting), items [item_id] lying on the ground.
"""

START_ROOM = "town_square"
RESPAWN_ROOM = "temple"


def R(name, area, desc, exits, spawns=None, npcs=None, safe=False, items=None, level=None):
    return {"name": name, "area": area, "desc": desc, "exits": exits, "spawns": spawns or [],
            "npcs": npcs or [], "safe": safe, "items": items or [], "level": level}


ROOMS = {
    # ================================================================= BRIGHTWATER
    "town_square": R(
        "Brightwater Town Square", "Brightwater",
        "Cobblestones worn smooth by centuries of feet spread out around a great marble fountain, "
        "where a statue of the Dawnfather raises a sun-disc toward the sky. Merchants cry their wares, "
        "children chase pigeons, and the smell of fresh bread drifts from somewhere nearby. The Gilded "
        "Griffin Inn stands to the west, the Temple of the Dawn to the east, the market street runs "
        "north and the south road leads toward the gate.",
        {"n": "market_street", "w": "inn", "e": "temple", "s": "south_road"}, safe=True),
    "inn": R(
        "The Gilded Griffin Inn", "Brightwater",
        "A warm common room of dark oak beams and crackling hearthfire. Tankards clatter, a lute plays "
        "somewhere in the corner, and a gilded griffin carved above the bar watches over the patrons. "
        "A trapdoor behind the bar leads down into the cellar. Here you may rest in safety.",
        {"e": "town_square", "d": "cellar"}, npcs=["bram"], safe=True),
    "cellar": R(
        "The Inn Cellar", "Brightwater",
        "Damp stone walls sweat in the lamplight. Casks of ale and sacks of grain are stacked high, many "
        "of them gnawed open. Something squeaks and skitters in the shadows between the barrels.",
        {"u": "inn"}, spawns=[("giant_rat", 4), ("cellar_spider", 1)], level=(1, 2)),
    "temple": R(
        "The Temple of the Dawn", "Brightwater",
        "Sunlight pours through tall windows of stained glass, painting the white marble floor in gold "
        "and rose. Incense curls before a great altar where an eternal flame burns. Robed acolytes move "
        "softly between the pews. Those who fall in battle awaken here, under the Dawnfather's grace.",
        {"w": "town_square"}, npcs=["aveline"], safe=True),
    "market_street": R(
        "Market Street", "Brightwater",
        "A bustling lane of timber-framed shops leans over the street. The ring of a hammer on an anvil "
        "sounds from the smithy to the west, and a cheerful painted sign to the east announces "
        "'Mirela's Sundries & Tinctures'. The north gate rises at the end of the street.",
        {"s": "town_square", "w": "smithy", "e": "general_store", "n": "north_gate"}, safe=True),
    "smithy": R(
        "Ironhand Smithy", "Brightwater",
        "Heat rolls off a roaring forge. Racks of swords, axes, maces and bows line the soot-blackened "
        "walls, and suits of mail hang from hooks like hollow knights. A broad-shouldered smith works "
        "the bellows.",
        {"e": "market_street"}, npcs=["durgan"], safe=True),
    "general_store": R(
        "Mirela's Sundries & Tinctures", "Brightwater",
        "Shelves crammed with jars, bottles, bundles of herbs and coils of rope rise to the ceiling. "
        "Bubbling alembics fill the shop with the scent of mint and sulphur.",
        {"w": "market_street"}, npcs=["mirela"], safe=True),
    "north_gate": R(
        "The North Gate", "Brightwater",
        "Twin towers of grey stone flank a great iron-bound gate. Guards in blue tabards stand watch, "
        "eyes on the King's Road that winds north into the hills. A sturdy barracks stands to the east.",
        {"s": "market_street", "n": "kings_road", "e": "barracks"}, safe=True),
    "barracks": R(
        "The Guard Barracks", "Brightwater",
        "Rows of cots, racks of spears, and a long table strewn with maps. A map of the region is pinned "
        "to the wall, with red pins marking bandit sightings in the Whispering Woods.",
        {"w": "north_gate"}, npcs=["halvard"], safe=True),
    "south_road": R(
        "The South Road", "Brightwater",
        "Neat cottages with flower boxes line the road as it runs toward the low southern gate. To the "
        "west, a narrow shopfront of blue-painted wood hangs a silver sign of a needle threading a star. "
        "Beyond the town wall, golden fields roll away toward a dark smudge of forest.",
        {"n": "town_square", "s": "meadow_path", "w": "silverthread"}, safe=True),
    "silverthread": R(
        "Silverthread Arcana", "Brightwater",
        "Bolts of shimmering cloth in midnight blue, violet and silver hang from the rafters, and glass "
        "cases hold wands, orbs and rings that glimmer with faint inner light. The air smells of lavender "
        "and candle wax. Behind a counter heaped with spellbooks, an elegant woman threads a needle "
        "that glows like a falling star.",
        {"e": "south_road"}, npcs=["elowen"], safe=True),

    # ================================================================= GREENMEADOW (1-5)
    "meadow_path": R(
        "Greenmeadow Path", "Greenmeadow",
        "A dirt path winds through waist-high grass dotted with poppies and cornflowers. Bees drone "
        "lazily in the warm air, and the walls of Brightwater rise behind you to the north. Something "
        "rustles in the grass.",
        {"n": "south_road", "s": "meadow_crossing", "e": "old_farm"},
        spawns=[("field_snake", 2), ("giant_rat", 1)], level=(1, 3)),
    "old_farm": R(
        "The Abandoned Farmstead", "Greenmeadow",
        "A farmhouse with a caved-in roof slumps beside a weed-choked garden. A tattered scarecrow "
        "leans at a drunken angle, and fresh kobold tracks circle the broken barn.",
        {"w": "meadow_path", "e": "kobold_warren"},
        spawns=[("kobold_scavenger", 3), ("wild_boar", 1)], level=(3, 4)),
    "kobold_warren": R(
        "The Kobold Warren", "Greenmeadow",
        "Burrows riddle a low hillside, the earth stamped flat and littered with bones, rags and stolen "
        "pots. A crude totem of sticks and feathers marks the warren's heart.",
        {"w": "old_farm"},
        spawns=[("kobold_scavenger", 2), ("kobold_trapper", 2)], level=(3, 5)),
    "meadow_crossing": R(
        "Willowbrook Crossing", "Greenmeadow",
        "A clear brook chuckles beneath an old stone bridge, its banks shaded by weeping willows. To the "
        "south, the trees thicken into the Whispering Woods.",
        {"n": "meadow_path", "s": "woods_edge"},
        spawns=[("wild_boar", 2), ("field_snake", 1)], level=(2, 4)),

    # ================================================================= WHISPERING WOODS (4-10)
    "woods_edge": R(
        "Edge of the Whispering Woods", "Whispering Woods",
        "Ancient oaks close overhead, their leaves murmuring in a wind you cannot feel. Shafts of green "
        "light fall across the mossy trail. Somewhere deeper in, a wolf howls.",
        {"n": "meadow_crossing", "s": "woods_deep", "w": "spider_hollow"},
        spawns=[("grey_wolf", 3)], level=(4, 5)),
    "spider_hollow": R(
        "Spider Hollow", "Whispering Woods",
        "Grey webs as thick as sailcloth drape between the trees, heavy with cocooned shapes. The air "
        "is still and smells of rot. Many-legged shadows shift high in the canopy.",
        {"e": "woods_edge"},
        spawns=[("giant_spider", 3)], level=(5, 6)),
    "woods_deep": R(
        "The Deep Woods", "Whispering Woods",
        "The trees here are vast and gnarled, their roots coiled like sleeping serpents. Little light "
        "reaches the forest floor. You notice boot-prints and the remains of a cookfire: bandits.",
        {"n": "woods_edge", "s": "bandit_approach", "e": "wolf_den"},
        spawns=[("bandit_scout", 2), ("grey_wolf", 2)], level=(5, 7)),
    "wolf_den": R(
        "The Dire Wolf Den", "Whispering Woods",
        "A rocky hollow beneath a fallen giant of an oak. Gnawed bones and tufts of black fur are "
        "everywhere. Yellow eyes gleam from the darkness of the den.",
        {"w": "woods_deep"},
        spawns=[("dire_wolf", 3)], level=(7, 8)),
    "bandit_approach": R(
        "Bandit Palisade", "Whispering Woods",
        "A crude wall of sharpened logs blocks the trail, its gate hanging open. Skulls of deer, and "
        "worse, are spiked along the top. Archers watch from a rickety platform.",
        {"n": "woods_deep", "s": "bandit_camp"},
        spawns=[("bandit_archer", 2), ("bandit_cutthroat", 1)], level=(7, 9)),
    "bandit_camp": R(
        "The Bandit Camp", "Whispering Woods",
        "Tents of stolen canvas ring a bonfire. Crates bearing the seals of Brightwater merchants are "
        "stacked high. In the largest tent, a heavy figure lounges on a looted throne.",
        {"n": "bandit_approach"},
        spawns=[("bandit_cutthroat", 2), ("bandit_chieftain", 1)], level=(8, 10)),

    # ================================================================= KING'S ROAD & BARROWFIELD (9-17)
    "kings_road": R(
        "The King's Road", "The Northlands",
        "A paved road, its stones heaved by frost and roots, runs north between rolling hills. An old "
        "milestone reads 'Brightwater 1 league'. Crows wheel above a hill to the east.",
        {"s": "north_gate", "n": "crossroads", "e": "barrowfield"}, safe=True),
    "barrowfield": R(
        "Barrowfield Graveyard", "Barrowfield",
        "Leaning headstones and grassy burial mounds cover the hillside. Many graves gape open, the "
        "earth clawed away from within. A cold mist clings to the ground even at midday.",
        {"w": "kings_road", "e": "barrow_chapel"},
        spawns=[("restless_zombie", 3), ("carrion_ghoul", 1)], level=(9, 10)),
    "barrow_chapel": R(
        "The Ruined Chapel", "Barrowfield",
        "A roofless chapel of black stone stands at the top of the hill. Its altar has been defaced with "
        "sigils of a grinning skull. A stair behind the altar descends into darkness, and a foul wind "
        "rises from below.",
        {"w": "barrowfield", "d": "crypt_entry"},
        spawns=[("carrion_ghoul", 2), ("restless_zombie", 1)], level=(10, 11)),
    "crypt_entry": R(
        "Crypt of Varnoth: Entry Stair", "Crypt of Varnoth",
        "Worn steps spiral down into a vaulted antechamber. The air is cold and dry and tastes of dust. "
        "Niches in the walls hold ancient skulls whose eye sockets seem to follow you.",
        {"u": "barrow_chapel", "n": "crypt_hall"},
        spawns=[("crypt_bat", 2), ("skeleton_warrior", 1)], level=(11, 12)),
    "crypt_hall": R(
        "Crypt of Varnoth: Hall of the Fallen", "Crypt of Varnoth",
        "A long hall lined with stone sarcophagi, their lids carved with sleeping knights. Several lids "
        "have been pushed aside from within. Green witchlight flickers in iron braziers.",
        {"s": "crypt_entry", "e": "crypt_ossuary", "n": "crypt_catacombs"},
        spawns=[("skeleton_warrior", 3)], level=(12, 13)),
    "crypt_ossuary": R(
        "Crypt of Varnoth: The Ossuary", "Crypt of Varnoth",
        "Every surface of this chamber is built from bones: walls of femurs, pillars of skulls, a "
        "chandelier of ribcages. In the centre, something enormous made of bones stirs.",
        {"w": "crypt_hall"},
        spawns=[("bone_guardian", 2), ("skeleton_warrior", 1)], level=(13, 14)),
    "crypt_catacombs": R(
        "Crypt of Varnoth: The Weeping Catacombs", "Crypt of Varnoth",
        "Narrow tunnels twist away in every direction. Faint, mournful weeping echoes from nowhere and "
        "everywhere. Your breath frosts in the air.",
        {"s": "crypt_hall", "n": "crypt_shrine"},
        spawns=[("wailing_spirit", 3)], level=(14, 15)),
    "crypt_shrine": R(
        "Crypt of Varnoth: Shrine of the Bone King", "Crypt of Varnoth",
        "Black candles burn before an altar heaped with offerings of bone and blood. Robed cultists "
        "chant beneath a mosaic of a crowned skeleton. Great doors of iron lie to the north.",
        {"s": "crypt_catacombs", "n": "crypt_sanctum"},
        spawns=[("crypt_cultist", 3), ("wailing_spirit", 1)], level=(14, 16)),
    "crypt_sanctum": R(
        "Crypt of Varnoth: The Bone Throne", "Crypt of Varnoth",
        "A vast circular chamber. Upon a throne of skulls sits a crowned skeleton in rotting royal robes. "
        "As you enter, green fire kindles in its eyes and a voice like grinding stones fills the room: "
        "'Another soul... for my collection.'",
        {"s": "crypt_shrine"},
        spawns=[("varnoth", 1)], level=(17, 17)),

    # ================================================================= CROSSROADS & MIREFEN (15-22)
    "crossroads": R(
        "The Weathered Crossroads", "The Northlands",
        "Four roads meet beneath a lightning-struck oak, where a weathered signpost points in every "
        "direction: 'Mirefen' to the west, 'Ironspine Pass' to the north, 'Elandor (abandoned)' to "
        "the east, and 'Brightwater' to the south.",
        {"s": "kings_road", "w": "mire_edge", "n": "foothills", "e": "misty_hills"}, safe=True),
    "mire_edge": R(
        "Edge of the Mirefen", "The Mirefen",
        "The road sinks into a land of black water, rotting reeds and twisted, moss-hung trees. "
        "Bubbles rise and burst with a stench of decay. Something large moves beneath the surface.",
        {"e": "crossroads", "w": "mire_deep", "s": "lizard_village"},
        spawns=[("bog_lurker", 3)], level=(15, 16)),
    "lizard_village": R(
        "Lizardfolk Stilt-Village", "The Mirefen",
        "Huts of reeds and mud perch on tall stilts above the water, connected by swaying rope bridges. "
        "Hissing voices fall silent as you approach, and spears are raised.",
        {"n": "mire_edge"},
        spawns=[("lizardman_warrior", 4)], level=(16, 17)),
    "mire_deep": R(
        "The Drowned Forest", "The Mirefen",
        "Dead trees rise from waist-deep water like the masts of sunken ships. Pale lights drift between "
        "them, beckoning. A huge shape, moss-covered and grunting, wades through the murk.",
        {"e": "mire_edge", "w": "serpent_pools"},
        spawns=[("swamp_troll", 2), ("will_o_wisp", 2)], level=(17, 18)),
    "serpent_pools": R(
        "The Serpent Pools", "The Mirefen",
        "Steaming pools of green water are fringed with giant ferns. Great coils slide just beneath "
        "the surface. On a hummock to the north, smoke rises from a crooked chimney.",
        {"e": "mire_deep", "n": "hag_hut"},
        spawns=[("mire_serpent", 3)], level=(19, 20)),
    "hag_hut": R(
        "The Hag's Hut", "The Mirefen",
        "A crooked hut of black timber squats on chicken-like legs of twisted root. Inside, a cauldron "
        "bubbles with something that has eyes. Herbs, bones and caged birds hang from every rafter. "
        "A cackling voice greets you: 'Ooooh, fresh meat for Mother's pot!'",
        {"s": "serpent_pools"},
        spawns=[("bog_hag", 1)], level=(22, 22)),

    # ================================================================= IRONSPINE MOUNTAINS (20-31)
    "foothills": R(
        "The Ironspine Foothills", "Ironspine Mountains",
        "The land rises in rocky, heather-covered folds toward the jagged grey peaks of the Ironspine. "
        "A cold wind whistles through the boulders, and you catch the musky scent of a great cat.",
        {"s": "crossroads", "n": "mountain_pass"},
        spawns=[("mountain_lion", 3)], level=(20, 21)),
    "mountain_pass": R(
        "Ironspine Pass", "Ironspine Mountains",
        "A narrow trail clings to the side of a sheer cliff. Far below, a river glints like a silver "
        "thread. Filthy nests of sticks and bones are wedged into the rock above, and a giant's "
        "footprints are pressed deep into the trail.",
        {"s": "foothills", "n": "giants_plateau", "e": "orc_outpost"},
        spawns=[("harpy", 3)], level=(21, 22)),
    "giants_plateau": R(
        "The Giant's Plateau", "Ironspine Mountains",
        "A windswept plateau of stone, scattered with the bones of cattle and the remains of huge "
        "campfires. A cave mouth to the north breathes freezing air.",
        {"s": "mountain_pass", "n": "frost_caverns"},
        spawns=[("hill_giant", 2), ("orc_raider", 1)], level=(23, 24)),
    "orc_outpost": R(
        "Orcish Outpost", "Ironspine Mountains",
        "A watchtower of lashed timbers and spiked iron overlooks the pass. War-drums thump from "
        "somewhere to the east, where black smoke rises above a great camp.",
        {"w": "mountain_pass", "e": "orc_warcamp"},
        spawns=[("orc_raider", 3)], level=(24, 25)),
    "orc_warcamp": R(
        "The Skullsplitter Warcamp", "Ironspine Mountains",
        "Hundreds of hide tents sprawl across a mountain valley. Orcs sharpen axes, warbeasts snort in "
        "pens, and shamans dance around totems hung with skulls. A great tent of black hide stands "
        "at the camp's heart to the north.",
        {"w": "orc_outpost", "n": "warlord_tent", "e": "warbeast_pens"},
        spawns=[("orc_berserker", 2), ("orc_shaman", 2)], level=(26, 27)),
    "warbeast_pens": R(
        "The Warbeast Pens", "Ironspine Mountains",
        "Pens of iron bars hold snorting, armoured beasts the size of oxen. The ground is churned to "
        "mud and the stench is overwhelming.",
        {"w": "orc_warcamp"},
        spawns=[("orc_warbeast", 3)], level=(27, 28)),
    "warlord_tent": R(
        "The Warlord's Tent", "Ironspine Mountains",
        "Trophies of a hundred battles hang from the tent poles: shields, banners, and heads. Upon a "
        "throne of bones and iron sits the largest orc you have ever seen. He grins, and rises.",
        {"s": "orc_warcamp"},
        spawns=[("warlord_gorrak", 1)], level=(31, 31)),
    "frost_caverns": R(
        "The Frost Caverns", "Ironspine Mountains",
        "A cathedral of blue ice. Frozen waterfalls hang like curtains, and your footsteps ring on the "
        "icy floor. Pale shapes drift through the walls themselves.",
        {"s": "giants_plateau", "n": "frost_throne"},
        spawns=[("ice_wraith", 3), ("frost_troll", 1)], level=(30, 32)),
    "frost_throne": R(
        "Hall of the Frost Jarls", "Ironspine Mountains",
        "A vast hall carved from a glacier, with a throne of ice upon a dais. Frost giants stand guard "
        "around it. Far above, a crack in the ice opens onto a red, smoky sky to the north.",
        {"s": "frost_caverns", "n": "ashen_waste"},
        spawns=[("frost_giant", 2), ("frost_troll", 1)], level=(32, 34)),

    # ================================================================= RUINS OF ELANDOR (32-41)
    "misty_hills": R(
        "The Misty Hills", "Ruins of Elandor",
        "A thick silver mist rolls between the hills. Shapes loom out of it: broken elven arches, "
        "toppled statues, and the faint glimmer of a white city to the east.",
        {"w": "crossroads", "e": "ruins_gate"},
        spawns=[("ruin_stalker", 2)], level=(32, 34)),
    "ruins_gate": R(
        "The Moonlit Gate of Elandor", "Ruins of Elandor",
        "A soaring gate of white stone, carved with leaves and stars, still stands though the walls "
        "around it have fallen. Spectral guards in silver armour patrol the threshold.",
        {"w": "misty_hills", "e": "ruins_plaza"},
        spawns=[("phantom_sentinel", 3)], level=(33, 34)),
    "ruins_plaza": R(
        "The Plaza of Heroes", "Ruins of Elandor",
        "A great plaza ringed by statues of elven heroes. Some have fallen and shattered; others "
        "turn their marble heads to watch you. A grand library lies to the north and a crystal "
        "tower rises to the east.",
        {"w": "ruins_gate", "n": "ruins_library", "e": "ruins_tower"},
        spawns=[("living_statue", 2), ("ruin_stalker", 1)], level=(35, 37)),
    "ruins_library": R(
        "The Library of Whispers", "Ruins of Elandor",
        "Endless shelves of crumbling tomes rise into darkness. Ghostly elven scholars drift between "
        "them, still reading, still muttering spells under their breath.",
        {"s": "ruins_plaza"},
        spawns=[("spectral_mage", 3)], level=(36, 37)),
    "ruins_tower": R(
        "The Crystal Observatory", "Ruins of Elandor",
        "At the top of a spiralling crystal stair, a domed observatory opens onto a sky full of stars "
        "even in daylight. A figure of empty robes and a crown of starlight turns from its telescope. "
        "'You should not have come here, child of a younger age.'",
        {"w": "ruins_plaza"},
        spawns=[("seluvar", 1)], level=(41, 41)),

    # ================================================================= ASHEN PEAKS (40-52)
    "ashen_waste": R(
        "The Ashen Waste", "Ashen Peaks",
        "A blasted landscape of grey ash and black rock stretches beneath a sky the colour of a bruise. "
        "Rivers of lava glow in the distance, and pillars of living flame dance on the plain.",
        {"s": "frost_throne", "n": "cinder_road"},
        spawns=[("fire_elemental", 3), ("salamander", 1)], level=(41, 42)),
    "cinder_road": R(
        "The Cinder Road", "Ashen Peaks",
        "A road of fused black glass climbs the flank of a smoking volcano. Grey drakes bask on the warm "
        "rocks, and ruined statues of dragon-worshippers line the way.",
        {"s": "ashen_waste", "n": "obsidian_halls"},
        spawns=[("ash_drake", 2), ("salamander", 2)], level=(42, 44)),
    "obsidian_halls": R(
        "The Obsidian Halls", "Ashen Peaks",
        "Halls of polished black glass, carved into the heart of the volcano by the dragon cult. "
        "Scaled guards stand at attention, and great golems of obsidian grind along the corridors.",
        {"s": "cinder_road", "d": "molten_depths"},
        spawns=[("dragonkin_guard", 3), ("obsidian_golem", 1)], level=(45, 46)),
    "molten_depths": R(
        "The Molten Depths", "Ashen Peaks",
        "A cavern of roaring heat where lakes of magma churn and spit. Demons of fire stalk the shores, "
        "and something colossal wades through the molten rock. A vast tunnel to the north glows "
        "with a terrible red light.",
        {"u": "obsidian_halls", "n": "dragon_lair"},
        spawns=[("flame_demon", 2), ("magma_titan", 1)], level=(48, 50)),
    "dragon_lair": R(
        "The Lair of Pyraxis", "Ashen Peaks",
        "A cavern so vast its ceiling is lost in smoke. A mountain of gold, gems and the bones of "
        "heroes fills the floor, and coiled upon it is a dragon older than kingdoms. One golden eye "
        "opens. 'Ahh,' rumbles a voice like an avalanche. 'A morsel that believes itself a legend.'",
        {"s": "molten_depths"},
        spawns=[("pyraxis", 1)], level=(52, 52)),
}

# ======================================================================= NPCs
NPCS = {
    "bram": {
        "name": "Bram the innkeeper", "keywords": ["bram", "innkeeper", "barkeep"],
        "desc": "A stout, red-bearded man with a stained apron and a booming laugh.",
        "greeting": "'Welcome to the Gilded Griffin, friend! Rest your bones, the beds are soft and "
                    "the ale is cold. Type REST to sleep here in safety.'",
        "quests": ["cellar_rats"],
    },
    "aveline": {
        "name": "Sister Aveline", "keywords": ["aveline", "sister", "priestess"],
        "desc": "A serene priestess in white and gold robes, a sun-disc upon her brow. Her eyes are kind but tired.",
        "greeting": "'May the Dawnfather light your path, traveller. Should you fall, it is here you "
                    "shall awaken.'",
        "quests": ["bone_king", "bog_hag"],
    },
    "durgan": {
        "name": "Durgan Ironhand", "keywords": ["durgan", "smith", "blacksmith"],
        "desc": "A broad, soot-streaked smith with forearms like oak branches and a braided grey beard.",
        "greeting": "'Need steel? You've come to the right forge. Type LIST to see my wares.'",
        "shop": ["iron_longsword", "steel_dagger", "yew_longbow", "runed_staff", "iron_mace",
                 "knights_blade", "leather_jerkin", "leather_gloves", "leather_leggings",
                 "iron_buckler", "studded_gloves", "chain_shirt", "iron_helm", "chain_leggings",
                 "iron_boots", "knight_breastplate", "steel_kite_shield", "plate_gauntlets",
                 "mithril_sword", "hunters_recurve", "mithril_hauberk"],
    },
    "elowen": {
        "name": "Elowen Silverthread", "keywords": ["elowen", "silverthread", "enchantress", "tailor"],
        "desc": "A tall, silver-haired high elf in robes of shifting violet, with ink-stained fingers and "
                "eyes that seem to read the magic in everything they rest upon.",
        "greeting": "'Steel is for those who cannot think their way out of trouble. For the rest of us, "
                    "there is silk, starlight and a well-chosen wand. Type LIST to see my wares.'",
        "shop": ["linen_robe", "apprentice_hood", "silk_gloves", "felt_slippers", "woven_trousers",
                 "copper_focus_ring", "wand_of_sparks", "moonstone_pendant", "acolyte_robe", "crystal_orb",
                 "spellweave_hood", "willow_staff", "enchanted_gloves", "mystic_leggings",
                 "spellbinder_robe", "runebound_slippers", "sapphire_ring", "archivist_robe",
                 "starsilk_hood", "wand_of_embers", "tome_of_warding"],
    },
    "mirela": {
        "name": "Mirela the alchemist", "keywords": ["mirela", "alchemist", "shopkeeper"],
        "desc": "A spry old woman with spectacles perched on her nose and purple-stained fingers.",
        "greeting": "'Potions, tinctures, elixirs! Something for every ache, dearie. Type LIST to browse.'",
        "shop": ["minor_healing_potion", "minor_mana_potion", "healing_potion", "mana_potion",
                 "greater_healing_potion", "greater_mana_potion", "supreme_healing_potion",
                 "supreme_mana_potion", "ring_of_vigor"],
    },
    "halvard": {
        "name": "Captain Halvard", "keywords": ["halvard", "captain", "guard"],
        "desc": "A grizzled veteran in a blue tabard, his face crossed with old scars.",
        "greeting": "'Keep your blade sharp, citizen. The roads aren't safe these days.'",
        "quests": ["wolf_pelts", "bandit_chief", "orc_warlord"],
    },
}
