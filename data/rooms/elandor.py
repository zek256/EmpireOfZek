"""The Ruins of Elandor (32-41)."""
from data.rooms.common import R

ROOMS = {
    "misty_hills": R(
        "The Misty Hills", "Ruins of Elandor",
        "A thick silver mist rolls between the hills. Shapes loom out of it: broken elven arches, "
        "toppled statues, and the faint glimmer of a white city to the east.",
        {"w": "crossroads", "e": "ruins_gate"},
        spawns=[("ruin_stalker", 2)], level=(32, 34)),
    "ruins_gate": R(
        "The Moonlit Gate of Elandor", "Ruins of Elandor",
        "A soaring gate of white stone, carved with leaves and stars, still stands though the walls "
        "around it have fallen. Spectral guards in silver armour patrol the threshold. Beyond a "
        "broken wall to the north, pale trees glimmer in an overgrown garden.",
        {"w": "misty_hills", "e": "ruins_plaza", "n": "silvered_gardens"},
        spawns=[("phantom_sentinel", 3)], level=(33, 34)),
    "silvered_gardens": R(
        "The Silvered Gardens", "Ruins of Elandor",
        "Trees with bark like hammered silver grow wild among cracked fountains and toppled benches, "
        "their leaves chiming faintly in the breeze. Hedges once clipped into the shapes of stags and "
        "swans have run riot into thorny tangles. A colonnade leads east toward the library.",
        {"s": "ruins_gate", "e": "ruins_library"},
        spawns=[("ruin_stalker", 2), ("phantom_sentinel", 1)], level=(34, 35)),
    "ruins_plaza": R(
        "The Plaza of Heroes", "Ruins of Elandor",
        "A great plaza ringed by statues of elven heroes. Some have fallen and shattered; others "
        "turn their marble heads to watch you. A grand library lies to the north, a crystal tower "
        "rises to the east, and broad steps lead down to an amphitheatre in the south.",
        {"w": "ruins_gate", "n": "ruins_library", "e": "ruins_tower", "s": "sunken_amphitheatre"},
        spawns=[("living_statue", 2), ("ruin_stalker", 1)], level=(35, 37)),
    "sunken_amphitheatre": R(
        "The Sunken Amphitheatre", "Ruins of Elandor",
        "Tiers of white stone seating descend in a great half-circle to a stage of cracked marble, "
        "where the last songs of Elandor were sung. The ground has slumped, and drifts of pale sand "
        "have crept in from the south to fill the lowest rows. Silent knights in silver stand on the "
        "stage as if waiting for a play that will never begin. Beyond the stage, a stair runs down "
        "into the dunes.",
        {"n": "ruins_plaza", "s": "sunken_stair"},
        spawns=[("moonblade_revenant", 2), ("living_statue", 1)], level=(37, 38)),
    "ruins_library": R(
        "The Library of Whispers", "Ruins of Elandor",
        "Endless shelves of crumbling tomes rise into darkness. Ghostly elven scholars drift between "
        "them, still reading, still muttering spells under their breath. A silver door to the east "
        "bears the crescent moon of the royal court.",
        {"s": "ruins_plaza", "w": "silvered_gardens", "e": "moon_court"},
        spawns=[("spectral_mage", 3)], level=(36, 37)),
    "moon_court": R(
        "The Hall of the Moon Court", "Ruins of Elandor",
        "A long hall of white marble lies open to the sky, where the lords of Elandor once sat in "
        "judgement beneath the moon. Their crescent thrones stand empty, guarded by sentinels of "
        "rune-carved stone that turn to face you with a grinding of ancient joints.",
        {"w": "ruins_library"},
        spawns=[("arcane_sentinel", 2), ("moonblade_revenant", 1)], level=(38, 40)),
    "ruins_tower": R(
        "The Crystal Observatory", "Ruins of Elandor",
        "At the top of a spiralling crystal stair, a domed observatory opens onto a sky full of stars "
        "even in daylight. A figure of empty robes and a crown of starlight turns from its telescope. "
        "'You should not have come here, child of a younger age.'",
        {"w": "ruins_plaza"},
        spawns=[("seluvar", 1)], level=(41, 41)),
}
