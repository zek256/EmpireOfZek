"""The Ironspine Mountains (20-34)."""
from data.rooms.common import R

ROOMS = {
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
        "footprints are pressed deep into the trail. A goat track scrambles west toward the high crags.",
        {"s": "foothills", "n": "giants_plateau", "e": "orc_outpost", "w": "eagle_crag"},
        spawns=[("harpy", 3)], level=(21, 22)),
    "eagle_crag": R(
        "Griffon's Crag", "Ironspine Mountains",
        "A knuckle of bare rock juts out over a thousand-foot drop, crowned with nests woven from whole "
        "saplings. Huge barred feathers and the picked bones of mountain goats litter every ledge. "
        "Wings beat somewhere overhead, and a shadow sweeps across the stone.",
        {"e": "mountain_pass", "n": "ogre_quarry"},
        spawns=[("griffon", 2), ("harpy", 1)], level=(22, 23)),
    "giants_plateau": R(
        "The Giant's Plateau", "Ironspine Mountains",
        "A windswept plateau of stone, scattered with the bones of cattle and the remains of huge "
        "campfires. A cave mouth to the north breathes freezing air. The clang of stone on stone "
        "echoes from a quarry to the west, and smoke rises from a crude steading to the east.",
        {"s": "mountain_pass", "n": "frost_caverns", "w": "ogre_quarry", "e": "giant_steading"},
        spawns=[("hill_giant", 2), ("orc_raider", 1)], level=(23, 24)),
    "ogre_quarry": R(
        "The Ogre Quarry", "Ironspine Mountains",
        "Great blocks of granite have been torn from the mountainside and left where they fell, as if "
        "the quarrymen lost interest halfway through. Ogres in rank bearskins squat among the rubble, "
        "gnawing on haunches of mutton. A frozen gorge opens to the north.",
        {"s": "eagle_crag", "e": "giants_plateau", "n": "rimeglass_gorge"},
        spawns=[("mountain_ogre", 2), ("hill_giant", 1)], level=(24, 25)),
    "giant_steading": R(
        "The Hill Giants' Steading", "Ironspine Mountains",
        "A longhouse built from whole pine trunks and roofed with sod squats against the mountain. "
        "A cauldron big enough to boil an ox hangs over a smoky fire, and a pile of bones taller than "
        "a man is heaped beside the door. Glacier ice glitters on the slopes to the north.",
        {"w": "giants_plateau", "s": "orc_outpost", "n": "rime_glacier"},
        spawns=[("hill_giant", 2), ("mountain_ogre", 1)], level=(25, 26)),
    "orc_outpost": R(
        "Orcish Outpost", "Ironspine Mountains",
        "A watchtower of lashed timbers and spiked iron overlooks the pass. War-drums thump from "
        "somewhere to the east, where black smoke rises above a great camp. A rutted track climbs "
        "north toward the giants' steading.",
        {"w": "mountain_pass", "e": "orc_warcamp", "n": "giant_steading"},
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
        "mud and the stench is overwhelming. Drums and chanting carry down from a ring of standing "
        "stones to the north.",
        {"w": "orc_warcamp", "n": "blood_circle"},
        spawns=[("orc_warbeast", 3)], level=(27, 28)),
    "blood_circle": R(
        "The Circle of Red Hands", "Ironspine Mountains",
        "Standing stones smeared with red handprints ring a trampled hilltop where the warlord's "
        "sworn guard swear their oaths in blood. A shaman tends a fire of bones at the centre, and "
        "armoured orcs stand in a silent ring, watching you with flat yellow eyes.",
        {"s": "warbeast_pens"},
        spawns=[("orc_bloodguard", 2), ("orc_shaman", 1)], level=(28, 29)),
    "warlord_tent": R(
        "The Warlord's Tent", "Ironspine Mountains",
        "Trophies of a hundred battles hang from the tent poles: shields, banners, and heads. Upon a "
        "throne of bones and iron sits the largest orc you have ever seen. He grins, and rises.",
        {"s": "orc_warcamp"},
        spawns=[("warlord_gorrak", 1)], level=(31, 31)),
    "rimeglass_gorge": R(
        "Rimeglass Gorge", "Ironspine Mountains",
        "A river froze mid-plunge here, and the gorge walls are sheathed in ice as clear as glass. "
        "White shapes lope along the frozen riverbed, and a long howl rises and is answered from the "
        "heights. To the east, the gorge opens into the blue mouth of the Frost Caverns.",
        {"s": "ogre_quarry", "e": "frost_caverns", "n": "jarls_mead_hall"},
        spawns=[("winter_wolf", 3)], level=(29, 30)),
    "frost_caverns": R(
        "The Frost Caverns", "Ironspine Mountains",
        "A cathedral of blue ice. Frozen waterfalls hang like curtains, and your footsteps ring on the "
        "icy floor. Pale shapes drift through the walls themselves. Side passages lead west to a "
        "frozen gorge and east onto the open glacier.",
        {"s": "giants_plateau", "n": "frost_throne", "w": "rimeglass_gorge", "e": "rime_glacier"},
        spawns=[("ice_wraith", 3), ("frost_troll", 1)], level=(30, 32)),
    "rime_glacier": R(
        "The Rime Glacier", "Ironspine Mountains",
        "A river of ancient ice grinds slowly down the mountain, split by crevasses that plunge into "
        "blue darkness. Pale drakes bask on the ice where the thin sun touches it, and frost-ghosts "
        "drift between the seracs.",
        {"w": "frost_caverns", "s": "giant_steading"},
        spawns=[("rime_drake", 2), ("ice_wraith", 1)], level=(30, 31)),
    "jarls_mead_hall": R(
        "The Jarls' Mead-Hall", "Ironspine Mountains",
        "A feasting hall of the frost giants, its rafters carved from glacier ice and hung with "
        "shields as big as cartwheels. Giants sprawl along benches of frozen stone, their white wolves "
        "gnawing bones at their feet. A passage east leads to the throne of the jarls.",
        {"s": "rimeglass_gorge", "e": "frost_throne"},
        spawns=[("frost_giant", 2), ("winter_wolf", 1)], level=(33, 34)),
    "frost_throne": R(
        "Hall of the Frost Jarls", "Ironspine Mountains",
        "A vast hall carved from a glacier, with a throne of ice upon a dais. Frost giants stand guard "
        "around it. Far above, a crack in the ice opens onto a red, smoky sky to the north.",
        {"s": "frost_caverns", "n": "meltwater_gorge", "w": "jarls_mead_hall"},
        spawns=[("frost_giant", 2), ("frost_troll", 1)], level=(32, 34)),
}
