"""Greenmeadow, the fields south of Brightwater (1-5)."""
from data.rooms.common import R

ROOMS = {
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
        "south, the trees thicken into the Whispering Woods. Upstream to the west, a waterwheel "
        "creaks.",
        {"n": "meadow_path", "s": "woods_edge", "w": "willow_mill"},
        spawns=[("wild_boar", 2), ("field_snake", 1)], level=(2, 4)),
    "willow_mill": R(
        "The Willow Mill", "Greenmeadow",
        "An old watermill stands on the brook, its wheel still turning though the miller left years "
        "ago. Spilled grain lies everywhere, and the floorboards upstairs creak under something "
        "heavier than a mouse.",
        {"e": "meadow_crossing"},
        spawns=[("giant_rat", 2), ("kobold_scavenger", 1)], level=(2, 4)),
}
