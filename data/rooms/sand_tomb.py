"""The Tomb of the Sand Kings, below the Sunken Pyramid (45-48)."""
from data.rooms.common import R

ROOMS = {
    "tomb_antechamber": R(
        "Tomb: The Sealed Antechamber", "Tomb of the Sand Kings",
        "The stair ends in a chamber of black stone painted with processions of priests and jackals, "
        "the colours as bright as the day they were laid down. The seal on the inner door has been "
        "broken from the inside. Something clicks and skitters in the dark.",
        {"u": "sunken_pyramid", "n": "tomb_embalmers"},
        spawns=[("tomb_guardian", 1), ("scarab_swarm", 1)], level=(45, 46)),
    "tomb_embalmers": R(
        "Tomb: The Hall of Embalmers", "Tomb of the Sand Kings",
        "Stone tables run the length of a long hall, each with channels cut to drain away what the "
        "embalmers did not need. Jars with the heads of animals stand in rows. Withered priests move "
        "between the tables, still at their work after three thousand years.",
        {"s": "tomb_antechamber", "w": "tomb_scarab_pits", "e": "tomb_treasury", "n": "tomb_gallery"},
        spawns=[("mummy_priest", 2), ("scarab_swarm", 1)], level=(46, 47)),
    "tomb_scarab_pits": R(
        "Tomb: The Scarab Pits", "Tomb of the Sand Kings",
        "A narrow walkway crosses a chamber whose floor is a glittering, heaving carpet of black and "
        "gold beetles, rustling like dry leaves. The tomb-builders kept them as guardians. They are "
        "still hungry.",
        {"e": "tomb_embalmers"},
        spawns=[("scarab_swarm", 3)], level=(45, 46)),
    "tomb_treasury": R(
        "Tomb: The Treasury of the Kings", "Tomb of the Sand Kings",
        "Chests of gold, chariots of gilded wood, and statues of kings in lapis and electrum fill a "
        "vaulted chamber. Basalt guardians with the heads of jackals stand among the treasure, and "
        "they have noticed you.",
        {"w": "tomb_embalmers"},
        spawns=[("tomb_guardian", 2)], level=(47, 48)),
    "tomb_gallery": R(
        "Tomb: The Gallery of the Dead Kings", "Tomb of the Sand Kings",
        "A long gallery lined with the sarcophagi of the Sand Kings, each one carved with its face. "
        "The lids of all but the last are shattered. A great door of gold at the far end is carved "
        "with a single word in a dead tongue, and you know without being told that it means REST.",
        {"s": "tomb_embalmers", "n": "tomb_burial_chamber"},
        spawns=[("mummy_priest", 1), ("tomb_guardian", 1)], level=(47, 48)),
    "tomb_burial_chamber": R(
        "Tomb: The Burial Chamber of Ussreth", "Tomb of the Sand Kings",
        "A chamber of gold beneath a ceiling painted with the stars as they were three thousand years "
        "ago. A sarcophagus stands open in the centre, and a figure in a golden mask sits upon it, "
        "sand pouring from the joints of its armour. 'You walk in the house of a king,' it says. "
        "'Kneel, and be buried with me.'",
        {"s": "tomb_gallery"},
        spawns=[("ussreth", 1)], level=(48, 48)),
}
