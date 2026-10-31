"""The Northlands: the King's Road and the Weathered Crossroads (safe)."""
from data.rooms.common import R

ROOMS = {
    "kings_road": R(
        "The King's Road", "The Northlands",
        "A paved road, its stones heaved by frost and roots, runs north between rolling hills. An old "
        "milestone reads 'Brightwater 1 league'. Crows wheel above a hill to the east.",
        {"s": "north_gate", "n": "crossroads", "e": "barrowfield"}, safe=True),
    "crossroads": R(
        "The Weathered Crossroads", "The Northlands",
        "Four roads meet beneath a lightning-struck oak, where a weathered signpost points in every "
        "direction: 'Mirefen' to the west, 'Ironspine Pass' to the north, 'Elandor (abandoned)' to "
        "the east, and 'Brightwater' to the south.",
        {"s": "kings_road", "w": "mire_edge", "n": "foothills", "e": "misty_hills"}, safe=True),
}
