"""The Dustway, the caravan road east of Brightwater (8-15)."""
from data.rooms.common import R

ROOMS = {
    "dustway_road": R(
        "The Dustway", "Dustway",
        "A road of pale, powdery dust runs east between dry fields and thorn hedges. Every passing "
        "cart raises a cloud that hangs in the air for an hour. Hyenas lope along the ditches, "
        "giggling, waiting for something to fall behind.",
        {"w": "east_gate", "e": "dry_ford"},
        spawns=[("dust_hyena", 3)], level=(8, 9)),
    "dry_ford": R(
        "The Dry Ford", "Dustway",
        "The road dips across the bed of a river that has not run in a generation, its stones bleached "
        "white. Masked riders wait in the shade of the far bank. A side track leads south to a "
        "waystation flying a faded blue flag.",
        {"w": "dustway_road", "e": "gallows_hill", "s": "dustway_waystation"},
        spawns=[("highwayman", 2), ("dust_hyena", 1)], level=(9, 10)),
    "dustway_waystation": R(
        "The Dustway Waystation", "Dustway",
        "A walled waystation of whitewashed stone, with a well, a stable, and a common room where "
        "caravan guards play cards. It is the last safe roof before the Badlands. A tough old woman "
        "with a crossbow keeps the gate. Here you may rest in safety.",
        {"n": "dry_ford", "e": "gnoll_scrub"}, npcs=["marta"], safe=True),
    "gallows_hill": R(
        "Gallows Hill", "Dustway",
        "A low hill beside the road is crowned by an old gallows, its ropes long since rotted away. "
        "The highwaymen use it as a lookout now, and their horses are tethered below. A hand-painted "
        "sign nailed to the post reads: TOLL - EVERYTHING YOU HAVE.",
        {"w": "dry_ford", "e": "dustway_toll", "s": "gnoll_scrub"},
        spawns=[("highwayman", 3)], level=(10, 12)),
    "gnoll_scrub": R(
        "The Gnoll Scrub", "Dustway",
        "Thorny scrub covers the land south of the road, riddled with the dens of gnoll scavengers. "
        "Picked bones lie in the dust, and the air is thick with flies and the yammering of the pack.",
        {"w": "dustway_waystation", "n": "gallows_hill"},
        spawns=[("gnoll_scavenger", 3)], level=(11, 12)),
    "dustway_toll": R(
        "The Broken Tollhouse", "Dustway",
        "A tollhouse of the old king's road lies in ruins, its roof fallen in and its gate torn down. "
        "Gnoll raiders have taken it for a camp, and a highwayman who thought he could share it hangs "
        "from the gatepost.",
        {"w": "gallows_hill", "e": "badlands_edge"},
        spawns=[("gnoll_raider", 2), ("highwayman", 1)], level=(13, 14)),
    "badlands_edge": R(
        "The Edge of the Badlands", "Dustway",
        "The fields end. Ahead, the land breaks into a maze of red rock: canyons, mesas and towers of "
        "stone carved by wind into strange shapes. Gnoll banners of hide and bone flap from a cairn "
        "beside the road.",
        {"w": "dustway_toll", "e": "canyon_mouth"},
        spawns=[("gnoll_raider", 2), ("gnoll_scavenger", 1)], level=(14, 15)),
}
