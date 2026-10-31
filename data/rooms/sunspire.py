"""Sunspire, the walled trade city of the Scorchsands (safe)."""
from data.rooms.common import R

ROOMS = {
    "ss_south_gate": R(
        "Sunspire: The Sunward Gate", "Sunspire",
        "A gate of gilded bronze stands open in walls of golden sandstone, guarded by warriors in "
        "spired helms and veils of mail. Caravans of camels and mules shuffle through, and the noise "
        "of the spice market rolls out to meet you.",
        {"s": "sunward_approach", "n": "ss_market"}, safe=True),
    "ss_market": R(
        "Sunspire: The Spice Market", "Sunspire",
        "Awnings of every colour shade stalls heaped with saffron, pepper, dates, incense and dyes. "
        "Merchants shout prices in a dozen tongues. A silk bazaar lies to the west, the city wells "
        "to the east, and the obelisk square to the north.",
        {"s": "ss_south_gate", "n": "ss_obelisk", "w": "ss_bazaar", "e": "ss_wells"}, safe=True),
    "ss_bazaar": R(
        "Sunspire: The Silk Bazaar", "Sunspire",
        "A covered bazaar where bolts of silk in every colour of the sunset hang from the rafters, "
        "and enchanters sit cross-legged among their wares. Lamps of coloured glass make the gloom "
        "glow like the inside of a jewel.",
        {"e": "ss_market"}, npcs=["amsa"], safe=True),
    "ss_wells": R(
        "Sunspire: The Wells of Sunspire", "Sunspire",
        "Seven deep wells lined with blue tile are the reason Sunspire exists at all. Water-carriers "
        "come and go with jars on their shoulders, and an old scholar sits on the rim of the "
        "nearest, watching the shadow of the obelisk crawl across the square.",
        {"w": "ss_market"}, safe=True),
    "ss_obelisk": R(
        "Sunspire: The Obelisk Square", "Sunspire",
        "A great square of white stone surrounds the Obelisk of Sunspire, a needle of black stone "
        "capped with gold that is older than the city and older, they say, than the desert. Its "
        "shadow is the city's clock. Streets lead off in every direction.",
        {"s": "ss_market", "n": "ss_palace", "w": "ss_smiths", "e": "ss_caravanserai"}, safe=True),
    "ss_smiths": R(
        "Sunspire: The Street of Smiths", "Sunspire",
        "Forges glow in every doorway of this narrow street, and the air rings with hammers. The best "
        "of them belongs to a master bladewright whose sunsteel scimitars are famous from here to "
        "the sea. The West Gate lies at the street's end.",
        {"e": "ss_obelisk", "w": "ss_west_gate"}, npcs=["zahir"], safe=True),
    "ss_west_gate": R(
        "Sunspire: The West Gate", "Sunspire",
        "A smaller gate opens west toward the palm oasis, its towers topped with brass sun-discs "
        "that flash signals across the desert. Guards check every caravan for raiders in disguise.",
        {"e": "ss_smiths", "w": "palm_oasis"}, safe=True),
    "ss_caravanserai": R(
        "Sunspire: The Great Caravanserai", "Sunspire",
        "A vast inn built around a courtyard, where caravans stable their camels below and their "
        "masters sleep above. A fountain plays in the middle, and the caravan-master sells "
        "potions for the road from a booth beside it. Here you may rest in safety.",
        {"w": "ss_obelisk"}, npcs=["nadim"], safe=True),
    "ss_palace": R(
        "Sunspire: The Palace of the Sun", "Sunspire",
        "A palace of white marble and gold, its halls cooled by fountains and shaded by screens of "
        "carved cedar. The Emira of Sunspire holds court on a cushioned dais beneath a sun-disc of "
        "beaten gold. An archive lies to the west and the barracks of the Sun Guard to the east.",
        {"s": "ss_obelisk", "n": "ss_north_gate", "w": "ss_archive", "e": "ss_barracks"},
        npcs=["zahrin"], safe=True),
    "ss_archive": R(
        "Sunspire: The Archive of Sand", "Sunspire",
        "Clay tablets, papyrus scrolls and bound books fill a cool, dim hall to the ceiling: the "
        "memory of every empire that rose and fell in the desert. A thin archivist with ink on his "
        "nose peers at you over a crumbling map.",
        {"e": "ss_palace"}, npcs=["mehrun"], safe=True),
    "ss_barracks": R(
        "Sunspire: The Barracks of the Sun Guard", "Sunspire",
        "The Sun Guard drill in a courtyard of hot sand, their crescent greatswords flashing. Their "
        "captain watches from the shade of a colonnade, a map of the northern desert unrolled on "
        "the table beside her.",
        {"w": "ss_palace"}, npcs=["idrisa"], safe=True),
    "ss_north_gate": R(
        "Sunspire: The North Gate", "Sunspire",
        "The north gate of Sunspire is kept shut and barred, and opened only for those with the "
        "Emira's leave. Beyond it lies the deep desert, the Valley of the Kings, and things the "
        "city would rather forget.",
        {"s": "ss_palace", "n": "northern_dunes"}, safe=True),
}
