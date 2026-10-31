"""The Scorchsands, the desert north of the Badlands and east of Elandor (35-49)."""
from data.rooms.common import R

ROOMS = {
    # ------------------------------------------------- the southern dunes, from the Badlands (35-41)
    "dune_edge": R(
        "The Dune Edge", "Scorchsands",
        "Red rock gives way to golden sand, and the dunes begin, rolling north like the waves of a "
        "frozen sea. The heat is a living thing. Black-veiled riders sit their horses on the nearest "
        "crest, watching you without moving.",
        {"s": "last_mesa", "n": "dune_sea"},
        spawns=[("desert_raider", 2)], level=(35, 36)),
    "dune_sea": R(
        "The Dune Sea", "Scorchsands",
        "Dunes as high as hills march to the horizon in every direction, and the wind sends plumes of "
        "sand off their crests like spray. A worn caravan trail runs west toward a glint of gold. "
        "Something shifts beneath the sand at your feet.",
        {"s": "dune_edge", "w": "caravan_road"},
        spawns=[("dune_scorpion", 2), ("desert_raider", 1)], level=(37, 38)),
    "caravan_road": R(
        "The Caravan Road", "Scorchsands",
        "Stone markers half-buried in the sand mark the caravan road to Sunspire, each carved with a "
        "sun. Bleached bones of camels lie beside it, and raiders lurk behind the dunes, waiting for "
        "stragglers.",
        {"e": "dune_sea", "w": "sunward_approach"},
        spawns=[("desert_raider", 3)], level=(37, 38)),
    "sunward_approach": R(
        "The Sunward Approach", "Scorchsands",
        "The walls of Sunspire rise to the north, golden in the sun, with the great obelisk standing "
        "above them like a needle of light. Caravans queue at the Sunward Gate, and the raiders keep "
        "a wary distance from the city's archers.",
        {"e": "caravan_road", "w": "raiders_wash", "n": "ss_south_gate"},
        spawns=[("desert_raider", 2)], level=(36, 37)),
    "raiders_wash": R(
        "The Raiders' Wash", "Scorchsands",
        "A dry riverbed winds between the dunes, shaded by cliffs of yellow sandstone. The raiders "
        "water their horses at a hidden seep here, and their black tents are pitched in the shade.",
        {"e": "sunward_approach", "w": "glass_waste"},
        spawns=[("desert_raider", 2), ("dune_scorpion", 1)], level=(38, 39)),
    "glass_waste": R(
        "The Glass Waste", "Scorchsands",
        "Something burned here, long ago, hot enough to turn the sand to glass. Green shards crunch "
        "underfoot and catch the sun so fiercely that you have to squint. Scorpions bask on the "
        "glass, their pale shells almost invisible.",
        {"e": "raiders_wash", "n": "mirage_flats"},
        spawns=[("dune_scorpion", 3)], level=(39, 40)),
    "mirage_flats": R(
        "The Mirage Flats", "Scorchsands",
        "A flat plain of white sand where the heat makes the air shimmer like water. Lakes appear and "
        "vanish, palm trees float upside down in the sky, and twice you see a great cat that is not "
        "there. Then once, you see one that is.",
        {"s": "glass_waste", "w": "sand_sea_edge"},
        spawns=[("mirage_stalker", 2)], level=(40, 41)),
    # ------------------------------------------------- the western sands, from the Ruins of Elandor (36-43)
    "sunken_stair": R(
        "The Sunken Stair", "Scorchsands",
        "Below the amphitheatre of Elandor, a grand stair of white stone runs down into a sea of "
        "sand that has swallowed half of it. The elven city's southern quarter lies buried here, and "
        "a marble hero still stands guard up to his chest in the dunes.",
        {"n": "sunken_amphitheatre", "e": "buried_colonnade"},
        spawns=[("living_statue", 1), ("dune_scorpion", 1)], level=(36, 37)),
    "buried_colonnade": R(
        "The Buried Colonnade", "Scorchsands",
        "The tops of a long colonnade of elven columns rise out of the sand like the ribs of a giant. "
        "Raiders have strung their awnings between them, and a statue that was not quite buried "
        "deep enough is pulling itself free.",
        {"w": "sunken_stair", "e": "sand_sea_edge"},
        spawns=[("desert_raider", 2), ("living_statue", 1)], level=(36, 37)),
    "sand_sea_edge": R(
        "The Edge of the Sand Sea", "Scorchsands",
        "The last of the elven ruins sink beneath the dunes, and the desert opens wide. Trails lead "
        "north toward a line of palms and east over the shimmering flats.",
        {"w": "buried_colonnade", "e": "mirage_flats", "n": "glassed_dunes"},
        spawns=[("dune_scorpion", 2)], level=(37, 38)),
    "glassed_dunes": R(
        "The Glassed Dunes", "Scorchsands",
        "The dunes here are crusted with a skin of brittle glass that cracks underfoot like thin ice. "
        "Raiders pick their way across with their horses' hooves wrapped in rags.",
        {"s": "sand_sea_edge", "n": "palm_oasis"},
        spawns=[("desert_raider", 2), ("dune_scorpion", 1)], level=(38, 39)),
    "palm_oasis": R(
        "The Palm Oasis", "Scorchsands",
        "A pool of blue water lies in a hollow ringed with date palms, the only green for leagues. "
        "By old law no blood should be spilled here, but the raiders have forgotten old laws. The "
        "West Gate of Sunspire lies a short walk to the east.",
        {"s": "glassed_dunes", "e": "ss_west_gate", "n": "salt_flats"},
        spawns=[("desert_raider", 2)], level=(38, 39)),
    "salt_flats": R(
        "The Salt Flats", "Scorchsands",
        "A blinding white plain of salt stretches north, flat as a table and hot as a forge. The "
        "bodies of travellers who lost their way lie where they fell, dried and white. Some of them "
        "are not lying down.",
        {"s": "palm_oasis", "n": "salt_pans"},
        spawns=[("salt_wraith", 3)], level=(41, 42)),
    "salt_pans": R(
        "The Salt Pans", "Scorchsands",
        "Square pans cut into the salt by some long-dead people are filled with brine that smells of "
        "death. The salt wraiths drift between them, moaning for water, and something with no shape "
        "of its own pads across the crust.",
        {"s": "salt_flats"},
        spawns=[("salt_wraith", 2), ("mirage_stalker", 1)], level=(42, 43)),
    # ------------------------------------------------- the deep desert, north of Sunspire (43-49)
    "northern_dunes": R(
        "The Northern Dunes", "Scorchsands",
        "North of Sunspire, the caravan roads end and the true desert begins. The dunes are red here, "
        "and taller than towers. The wind carries voices that belong to no one, and pillars of "
        "smoke walk on the horizon.",
        {"s": "ss_north_gate", "e": "whirling_sands", "w": "giants_causeway"},
        spawns=[("mirage_stalker", 2), ("wild_djinn", 1)], level=(43, 44)),
    "whirling_sands": R(
        "The Whirling Sands", "Scorchsands",
        "A storm that never ends turns over a great bowl in the dunes, and the djinn ride it like "
        "horses, laughing. Sand blasts your skin raw, and you can barely see your own hand.",
        {"w": "northern_dunes", "n": "valley_of_kings"},
        spawns=[("wild_djinn", 2), ("mirage_stalker", 1)], level=(44, 45)),
    "giants_causeway": R(
        "The Giants' Causeway", "Scorchsands",
        "A road of huge paving stones, each one as big as a house, runs across the dunes toward "
        "nothing. The sand giants claim it was built by their ancestors, and they do not like "
        "visitors on it.",
        {"e": "northern_dunes", "n": "sandworm_deeps"},
        spawns=[("sand_giant", 2)], level=(46, 47)),
    "valley_of_kings": R(
        "The Valley of the Kings", "Scorchsands",
        "A long valley of sandstone cliffs is carved with the doors of a hundred tombs, every one "
        "broken open and robbed long ago. Sand giants lair in the largest, and a djinn drifts among "
        "the doors as if searching for something. To the west, the tip of a pyramid rises from the sand.",
        {"s": "whirling_sands", "w": "sunken_pyramid"},
        spawns=[("sand_giant", 2), ("wild_djinn", 1)], level=(46, 47)),
    "sandworm_deeps": R(
        "The Sandworm Deeps", "Scorchsands",
        "The dunes here sag into vast pits where the sand pours away like water down a drain. The "
        "ground trembles constantly. Then the sand bulges, and something as wide as a house rises out "
        "of it, mouth first.",
        {"s": "giants_causeway", "e": "sunken_pyramid"},
        spawns=[("great_sandworm", 2)], level=(48, 49)),
    "sunken_pyramid": R(
        "The Sunken Pyramid", "Scorchsands",
        "Only the top of a vast pyramid of black stone rises above the sand, its capstone of gold "
        "still blazing in the sun. A doorway has been dug free on one face, guarded by statues with "
        "the heads of jackals, and a stair leads down into the dark: the Tomb of the Sand Kings.",
        {"e": "valley_of_kings", "w": "sandworm_deeps", "d": "tomb_antechamber"},
        spawns=[("tomb_guardian", 1), ("scarab_swarm", 2)], level=(45, 46)),
}
