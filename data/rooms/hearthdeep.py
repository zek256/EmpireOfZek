"""Hearthdeep, the dwarven hold in the Rimefells (safe)."""
from data.rooms.common import R

ROOMS = {
    "hearthdeep_gate": R(
        "The Gate of Hearthdeep", "Hearthdeep",
        "Two great doors of iron-bound stone stand open in the mountainside, each carved with a "
        "dwarven king holding a hammer and a torch. Warm air and the smell of coal smoke roll out "
        "into the snow. The gatewatch keeps its post to the west, and lantern-lit terraces climb "
        "to the east.",
        {"s": "snowbound_meadow", "n": "hall_of_hearths", "w": "hearthdeep_gatewatch", "e": "lantern_terraces"},
        safe=True),
    "hearthdeep_gatewatch": R(
        "The Gatewatch", "Hearthdeep",
        "A guardroom cut into the rock beside the gate, lined with racks of axes and crossbows. "
        "Dwarves in steel and fur play dice by a brazier while a map of the Rimefells, pinned with "
        "iron nails, covers one wall.",
        {"e": "hearthdeep_gate"}, npcs=["orla"], safe=True),
    "lantern_terraces": R(
        "The Lantern Terraces", "Hearthdeep",
        "Terraces of dressed stone step up the inside of a vast cavern, each lined with workshops "
        "and homes lit by hanging lanterns of coloured glass. Children chase each other along the "
        "railings, and somewhere a dwarf is singing a very long song about a very old grudge.",
        {"w": "hearthdeep_gate", "n": "hearthdeep_east_door"}, safe=True),
    "hearthdeep_east_door": R(
        "The East Door", "Hearthdeep",
        "A smaller gate opens east onto the Cairn Saddle and the high road to the Mirefen. The hold's "
        "main hall lies to the west, and a narrow stair climbs north to a rune-cutter's workshop.",
        {"s": "lantern_terraces", "w": "hall_of_hearths", "e": "cairn_saddle", "n": "runecutters"},
        safe=True),
    "hall_of_hearths": R(
        "The Hall of Hearths", "Hearthdeep",
        "The great hall of Hearthdeep, where a hundred hearths burn in a ring around a pillar carved "
        "with the names of every dwarf who ever lived here. The ring of hammers sounds from a forge "
        "to the west, and the Thane's hall lies through a pair of bronze doors to the north.",
        {"s": "hearthdeep_gate", "w": "ironhand_forge", "e": "hearthdeep_east_door", "n": "thanes_hall"},
        safe=True),
    "ironhand_forge": R(
        "The Ironhand Forge", "Hearthdeep",
        "The ancestral forge of the Ironhand clan, where a river of molten iron runs in a channel "
        "across the floor and a dozen anvils ring at once. Finished axes, hammers and suits of plate "
        "stand in ranks along the walls. A stair leads up to an alehouse.",
        {"e": "hall_of_hearths", "n": "stone_flagon"}, npcs=["brakka"], safe=True),
    "stone_flagon": R(
        "The Stone Flagon", "Hearthdeep",
        "A low, warm alehouse carved from the rock, with barrels as tall as a man lining the walls "
        "and a fire that has not gone out in three hundred years. Dwarves argue cheerfully over "
        "tankards of dark ale. Here you may rest in safety.",
        {"s": "ironhand_forge"}, npcs=["gilda"], safe=True),
    "runecutters": R(
        "Runecutter's Workshop", "Hearthdeep",
        "A quiet workshop where rune-carved staves, rings and amulets lie on velvet under glass. The "
        "air smells of stone dust, and every surface hums faintly with bound power. An old dwarf "
        "with a jeweller's loupe in one eye works at a bench by the window.",
        {"s": "hearthdeep_east_door"}, npcs=["tamsin"], safe=True),
    "thanes_hall": R(
        "The Thane's Hall", "Hearthdeep",
        "A long hall hung with clan banners and lit by braziers, where the Thane of Hearthdeep sits "
        "on a throne of grey granite. The mood is grim. Beyond the throne, a great iron cage hangs "
        "in a shaft, the lift down to the mines of Deepdelve.",
        {"s": "hall_of_hearths", "n": "deepdelve_lift"}, npcs=["hargrim"], safe=True),
    "deepdelve_lift": R(
        "The Deepdelve Lift", "Hearthdeep",
        "A great iron cage hangs from chains in a shaft that drops into blackness, its winch manned by "
        "two nervous guards. Since the miners stopped coming back, nobody rides it down. Cold air "
        "breathes up from below, carrying a sound like grinding stone.",
        {"s": "thanes_hall", "d": "deepdelve_foot"}, safe=True),
}
