"""The Redrock Badlands, gnoll country east of the Dustway (18-27)."""
from data.rooms.common import R

ROOMS = {
    "canyon_mouth": R(
        "Redrock Canyon Mouth", "Redrock Badlands",
        "The Dustway ends where a red canyon opens in the rock like a wound. Gnoll warriors squat on "
        "the ledges above the entrance, watching the road. Trails branch north to a forest of stone "
        "spires, east onto glittering flats, and south toward the smell of old bones.",
        {"w": "badlands_edge", "e": "scorpion_flats", "n": "harpy_spires", "s": "bone_pits"},
        spawns=[("gnoll_warrior", 3)], level=(18, 19)),
    "harpy_spires": R(
        "The Harpy Spires", "Redrock Badlands",
        "Tall, thin towers of red rock rise like the fingers of a buried giant, their tops crusted "
        "with filthy nests. Harpies shriek and wheel above, and the ground between the spires is "
        "littered with things they have dropped.",
        {"s": "canyon_mouth", "e": "shattered_mesa"},
        spawns=[("harpy", 2), ("giant_scorpion", 1)], level=(21, 22)),
    "scorpion_flats": R(
        "The Scorpion Flats", "Redrock Badlands",
        "A dry lakebed of cracked red clay, baking under the sun. The cracks are wide enough to lose "
        "a foot in, and things move in them: scorpions as big as carts, their stingers held high.",
        {"w": "canyon_mouth", "e": "wyvern_ledges", "n": "shattered_mesa", "s": "gnoll_warcamp"},
        spawns=[("giant_scorpion", 3)], level=(20, 21)),
    "shattered_mesa": R(
        "The Shattered Mesa", "Redrock Badlands",
        "A flat-topped mesa has split into great blocks, as if something struck it from the sky. "
        "Whirling columns of red sand dance across its top with burning eyes, and wyverns circle "
        "overhead. Far to the north, beyond the badlands, the land turns to golden dunes.",
        {"w": "harpy_spires", "s": "scorpion_flats"},
        spawns=[("dust_devil", 2), ("canyon_wyvern", 1)], level=(24, 25)),
    "bone_pits": R(
        "The Bone Pits", "Redrock Badlands",
        "Pits dug in the canyon floor are filled with bones: cattle, horses, gnolls, and people. The "
        "gnoll bonecallers come here to speak with the spirits of the pack, and their whistles of "
        "human bone shriek in the wind.",
        {"n": "canyon_mouth", "e": "gnoll_warcamp"},
        spawns=[("gnoll_warrior", 2), ("gnoll_bonecaller", 1)], level=(22, 23)),
    "gnoll_warcamp": R(
        "The Gnoll Warcamp", "Redrock Badlands",
        "A camp of hide tents and bone fences fills a box canyon, loud with yammering and fights over "
        "scraps. Captured caravan wagons are drawn up in a ring, their cargo long since torn apart. "
        "A deeper howling rises from a pit to the east.",
        {"w": "bone_pits", "n": "scorpion_flats", "e": "howling_pit"},
        spawns=[("gnoll_warrior", 2), ("gnoll_bonecaller", 1)], level=(24, 25)),
    "wyvern_ledges": R(
        "The Wyvern Ledges", "Redrock Badlands",
        "A canyon wall rises in a hundred narrow ledges, each one a wyvern's roost, white with "
        "droppings and strewn with bones. The wyverns shriek and launch themselves into the air as "
        "you come into view.",
        {"w": "scorpion_flats", "s": "howling_pit", "e": "last_mesa"},
        spawns=[("canyon_wyvern", 2), ("harpy", 1)], level=(23, 24)),
    "howling_pit": R(
        "The Howling Pit", "Redrock Badlands",
        "A great round pit where the gnolls make captives fight for their amusement, ringed with "
        "bone seats. Orc sellswords hired by the warlord lounge on the seats, betting on the next "
        "bout. A cave mouth to the east is hung with a curtain of teeth.",
        {"w": "gnoll_warcamp", "n": "wyvern_ledges", "e": "yellowtooth_den"},
        spawns=[("orc_berserker", 2), ("gnoll_bonecaller", 1)], level=(25, 26)),
    "yellowtooth_den": R(
        "Yellowtooth's Den", "Redrock Badlands",
        "A cave strewn with loot from a hundred caravans: silks, spices, broken wagons and gold. On a "
        "throne of stacked shields sits a huge grey gnoll with one ear and a crown of human teeth. "
        "He begins to laugh, and does not stop.",
        {"w": "howling_pit"},
        spawns=[("yellowtooth", 1)], level=(26, 26)),
    "last_mesa": R(
        "The Last Mesa", "Redrock Badlands",
        "The final mesa of the badlands looks out over an ocean of golden dunes to the north. The "
        "wind off the desert is hot as an oven's breath, and whirlwinds of sand break off it and "
        "wander the rock like lost things.",
        {"w": "wyvern_ledges", "n": "dune_edge"},
        spawns=[("canyon_wyvern", 2), ("dust_devil", 1)], level=(26, 27)),
}
