"""Westmarch, the farmland west of Brightwater (3-10)."""
from data.rooms.common import R

ROOMS = {
    "westmarch_road": R(
        "The Westmarch Road", "Westmarch",
        "A rutted cart road leaves the West Gate and wanders between hedgerows and stone walls, past "
        "fields of barley and turnips. Smoke rises from a hamlet to the west, and a farm track runs "
        "south toward a red-roofed barn.",
        {"e": "west_gate", "w": "thornbury", "s": "haverick_farm"},
        spawns=[("wild_boar", 2), ("field_snake", 1)], level=(3, 4)),
    "haverick_farm": R(
        "Haverick's Farm", "Westmarch",
        "A tidy farmstead with a red-roofed barn and a duck pond, its fences recently mended and "
        "already broken again. Feathers are strewn across the yard, the henhouse door hangs open, "
        "and small muddy footprints lead everywhere.",
        {"n": "westmarch_road"},
        spawns=[("goblin_sneak", 2), ("wild_boar", 1)], level=(4, 5)),
    "thornbury": R(
        "Thornbury Hamlet", "Westmarch",
        "A handful of thatched cottages cluster around a village green and an old well, guarded by a "
        "fence of sharpened stakes that looks newer than anything else here. A farmer leans on the "
        "well with a pitchfork, glaring westward. The road continues west toward the quarry hills.",
        {"e": "westmarch_road", "w": "quarry_rim"}, npcs=["haverick"], safe=True),
    "quarry_rim": R(
        "The Quarry Rim", "Westmarch",
        "The fields give way to scrubby hills scarred by the old Westmarch quarry, whose grey cliffs "
        "drop away to the south. Goblin cookfires smoke on the far ledges, and the hill road "
        "climbs on to the west.",
        {"e": "thornbury", "s": "goblin_quarry", "w": "hill_road"},
        spawns=[("hill_goblin", 2), ("goblin_sneak", 1)], level=(6, 7)),
    "goblin_quarry": R(
        "The Goblin Quarry", "Westmarch",
        "Abandoned cranes and rotting scaffolds lean over a pit of cut grey stone, and the goblins "
        "have made it their kingdom. Crude huts of stolen planks crowd the ledges, a shaman's totem "
        "of crow skulls stands in the middle, and tunnels lead deeper into the rock to the west.",
        {"n": "quarry_rim", "w": "quarry_depths"},
        spawns=[("hill_goblin", 2), ("goblin_shaman", 1)], level=(7, 8)),
    "quarry_depths": R(
        "The Quarry Depths", "Westmarch",
        "The lowest cut of the quarry, where the walls rise sheer on every side and water drips into "
        "green pools. The biggest goblins lounge here on piles of loot from a dozen farms, and a "
        "ramp of rubble climbs north to the hill road. To the south, a cleft in the quarry wall "
        "opens onto the dark eaves of a great forest.",
        {"e": "goblin_quarry", "n": "hill_road", "s": "westwood_verge"},
        spawns=[("goblin_brute", 2), ("goblin_shaman", 1)], level=(8, 10)),
    "hill_road": R(
        "The Hill Road", "Westmarch",
        "The road climbs through bare, windy hills where heather grows between grey boulders. Wolves "
        "howl in the hollows, and to the west a lonely watchtower stands against a sky that is "
        "already white with distant snow.",
        {"e": "quarry_rim", "s": "quarry_depths", "w": "old_watchtower"},
        spawns=[("dire_wolf", 2), ("hill_goblin", 1)], level=(8, 9)),
    "old_watchtower": R(
        "The Old Watchtower", "Westmarch",
        "A broken watchtower of Brightwater's old border guard stands on the last of the western "
        "hills, its upper floors long fallen in. Snow lies in the lee of its walls. To the north the "
        "land climbs into the white hills of the Rimefells, where the dwarves of Hearthdeep dwell.",
        {"e": "hill_road", "n": "frostfoot_trail"},
        spawns=[("goblin_brute", 1), ("snow_wolf", 2)], level=(9, 10)),
}
