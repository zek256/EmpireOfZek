"""Barrowfield and the Crypt of Varnoth below it (9-17)."""
from data.rooms.common import R

ROOMS = {
    "barrowfield": R(
        "Barrowfield Graveyard", "Barrowfield",
        "Leaning headstones and grassy burial mounds cover the hillside. Many graves gape open, the "
        "earth clawed away from within. A cold mist clings to the ground even at midday.",
        {"w": "kings_road", "e": "barrow_chapel"},
        spawns=[("restless_zombie", 3), ("carrion_ghoul", 1)], level=(9, 10)),
    "barrow_chapel": R(
        "The Ruined Chapel", "Barrowfield",
        "A roofless chapel of black stone stands at the top of the hill. Its altar has been defaced with "
        "sigils of a grinning skull. A stair behind the altar descends into darkness, and a foul wind "
        "rises from below.",
        {"w": "barrowfield", "d": "crypt_entry"},
        spawns=[("carrion_ghoul", 2), ("restless_zombie", 1)], level=(10, 11)),
    "crypt_entry": R(
        "Crypt of Varnoth: Entry Stair", "Crypt of Varnoth",
        "Worn steps spiral down into a vaulted antechamber. The air is cold and dry and tastes of dust. "
        "Niches in the walls hold ancient skulls whose eye sockets seem to follow you.",
        {"u": "barrow_chapel", "n": "crypt_hall"},
        spawns=[("crypt_bat", 2), ("skeleton_warrior", 1)], level=(11, 12)),
    "crypt_hall": R(
        "Crypt of Varnoth: Hall of the Fallen", "Crypt of Varnoth",
        "A long hall lined with stone sarcophagi, their lids carved with sleeping knights. Several lids "
        "have been pushed aside from within. Green witchlight flickers in iron braziers.",
        {"s": "crypt_entry", "e": "crypt_ossuary", "n": "crypt_catacombs"},
        spawns=[("skeleton_warrior", 3)], level=(12, 13)),
    "crypt_ossuary": R(
        "Crypt of Varnoth: The Ossuary", "Crypt of Varnoth",
        "Every surface of this chamber is built from bones: walls of femurs, pillars of skulls, a "
        "chandelier of ribcages. In the centre, something enormous made of bones stirs.",
        {"w": "crypt_hall"},
        spawns=[("bone_guardian", 2), ("skeleton_warrior", 1)], level=(13, 14)),
    "crypt_catacombs": R(
        "Crypt of Varnoth: The Weeping Catacombs", "Crypt of Varnoth",
        "Narrow tunnels twist away in every direction. Faint, mournful weeping echoes from nowhere and "
        "everywhere. Your breath frosts in the air.",
        {"s": "crypt_hall", "n": "crypt_shrine"},
        spawns=[("wailing_spirit", 3)], level=(14, 15)),
    "crypt_shrine": R(
        "Crypt of Varnoth: Shrine of the Bone King", "Crypt of Varnoth",
        "Black candles burn before an altar heaped with offerings of bone and blood. Robed cultists "
        "chant beneath a mosaic of a crowned skeleton. Great doors of iron lie to the north.",
        {"s": "crypt_catacombs", "n": "crypt_sanctum"},
        spawns=[("crypt_cultist", 3), ("wailing_spirit", 1)], level=(14, 16)),
    "crypt_sanctum": R(
        "Crypt of Varnoth: The Bone Throne", "Crypt of Varnoth",
        "A vast circular chamber. Upon a throne of skulls sits a crowned skeleton in rotting royal robes. "
        "As you enter, green fire kindles in its eyes and a voice like grinding stones fills the room: "
        "'Another soul... for my collection.'",
        {"s": "crypt_shrine"},
        spawns=[("varnoth", 1)], level=(17, 17)),
}
