"""The Deepdelve Mine below Hearthdeep (18-21)."""
from data.rooms.common import R

ROOMS = {
    "deepdelve_foot": R(
        "Deepdelve: The Lift Foot", "Deepdelve Mine",
        "The lift cage rattles to a stop on a landing of cut stone, far below the hold. Mine carts "
        "lie overturned along the rails, and the tunnel walls have been gouged by something that "
        "chewed through solid rock. A gallery runs north into the dark.",
        {"u": "deepdelve_lift", "n": "deepdelve_gallery"},
        spawns=[("rockgnasher", 2)], level=(18, 19)),
    "deepdelve_gallery": R(
        "Deepdelve: The Long Gallery", "Deepdelve Mine",
        "A long gallery held up by pillars of uncut stone, its lanterns long since gone out. Grey "
        "figures with picks shuffle between the pillars, still mining, though they no longer seem to "
        "care what. Water drips to the west, and crystal light glimmers to the east.",
        {"s": "deepdelve_foot", "w": "deepdelve_flooded", "e": "deepdelve_seam", "n": "deepdelve_camp"},
        spawns=[("deepkin_delver", 2), ("rockgnasher", 1)], level=(19, 20)),
    "deepdelve_flooded": R(
        "Deepdelve: The Flooded Shaft", "Deepdelve Mine",
        "An old shaft has flooded to the waist with black, freezing water that reflects your light "
        "back at you. Something long and slick moves just beneath the surface, and the timbers "
        "groan overhead.",
        {"e": "deepdelve_gallery"},
        spawns=[("giant_leech", 2)], level=(19, 20)),
    "deepdelve_seam": R(
        "Deepdelve: The Crystal Seam", "Deepdelve Mine",
        "The tunnel opens into a cavern whose walls are thick with crystals as long as spears, all "
        "glowing a cold, cloudy white. Some of the clusters have grown into the shapes of men, and "
        "some of those are moving.",
        {"w": "deepdelve_gallery"},
        spawns=[("crystal_golem", 2)], level=(20, 21)),
    "deepdelve_camp": R(
        "Deepdelve: The Delvers' Camp", "Deepdelve Mine",
        "The lost miners of Hearthdeep made camp here, and they are here still, grey-skinned and "
        "hollow-eyed, sitting around a fire that gives no warmth. They rise as one when you enter. "
        "Beyond them, a vault door of black iron stands open on a deeper dark.",
        {"s": "deepdelve_gallery", "n": "stonewake_vault"},
        spawns=[("deepkin_delver", 3)], level=(20, 21)),
    "stonewake_vault": R(
        "Deepdelve: The Stonewake Vault", "Deepdelve Mine",
        "The miners broke through into a cavern that no dwarf ever cut, where the rock is veined "
        "with glowing crystal like a living thing. At its heart, a figure of granite as tall as a "
        "tower uncurls from the wall. Its voice is the groaning of the mountain: 'YOU DUG. I WOKE.'",
        {"s": "deepdelve_camp"},
        spawns=[("ghaldrek", 1)], level=(21, 21)),
}
