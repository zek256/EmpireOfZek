"""The Whispering Woods (4-10)."""
from data.rooms.common import R

ROOMS = {
    "woods_edge": R(
        "Edge of the Whispering Woods", "Whispering Woods",
        "Ancient oaks close overhead, their leaves murmuring in a wind you cannot feel. Shafts of green "
        "light fall across the mossy trail. Somewhere deeper in, a wolf howls.",
        {"n": "meadow_crossing", "s": "woods_deep", "w": "spider_hollow"},
        spawns=[("grey_wolf", 3)], level=(4, 5)),
    "spider_hollow": R(
        "Spider Hollow", "Whispering Woods",
        "Grey webs as thick as sailcloth drape between the trees, heavy with cocooned shapes. The air "
        "is still and smells of rot. Many-legged shadows shift high in the canopy.",
        {"e": "woods_edge"},
        spawns=[("giant_spider", 3)], level=(5, 6)),
    "woods_deep": R(
        "The Deep Woods", "Whispering Woods",
        "The trees here are vast and gnarled, their roots coiled like sleeping serpents. Little light "
        "reaches the forest floor. You notice boot-prints and the remains of a cookfire: bandits.",
        {"n": "woods_edge", "s": "bandit_approach", "e": "wolf_den"},
        spawns=[("bandit_scout", 2), ("grey_wolf", 2)], level=(5, 7)),
    "wolf_den": R(
        "The Dire Wolf Den", "Whispering Woods",
        "A rocky hollow beneath a fallen giant of an oak. Gnawed bones and tufts of black fur are "
        "everywhere. Yellow eyes gleam from the darkness of the den. A deer trail slips away south "
        "into a gully choked with ferns.",
        {"w": "woods_deep", "s": "fern_gully"},
        spawns=[("dire_wolf", 3)], level=(7, 8)),
    "fern_gully": R(
        "Fern Gully", "Whispering Woods",
        "A deep, damp gully where ferns grow higher than your head and a stream runs unseen beneath "
        "them. Claw marks score the bark of the trees, far higher than any wolf could reach.",
        {"n": "wolf_den", "s": "old_south_way"},
        spawns=[("dire_wolf", 1), ("brown_bear", 2)], level=(8, 9)),
    "old_south_way": R(
        "The Old South Way", "Whispering Woods",
        "Mossy flagstones show through the leaf-litter here, the remains of a road the elves built "
        "when the woods were young. A worn waystone carved with a silver leaf points south, where "
        "the trees grow vast and ancient: the Eldergrove.",
        {"n": "fern_gully", "s": "grove_verge"},
        spawns=[("brown_bear", 2)], level=(9, 10)),
    "bandit_approach": R(
        "Bandit Palisade", "Whispering Woods",
        "A crude wall of sharpened logs blocks the trail, its gate hanging open. Skulls of deer, and "
        "worse, are spiked along the top. Archers watch from a rickety platform.",
        {"n": "woods_deep", "s": "bandit_camp"},
        spawns=[("bandit_archer", 2), ("bandit_cutthroat", 1)], level=(7, 9)),
    "bandit_camp": R(
        "The Bandit Camp", "Whispering Woods",
        "Tents of stolen canvas ring a bonfire. Crates bearing the seals of Brightwater merchants are "
        "stacked high. In the largest tent, a heavy figure lounges on a looted throne.",
        {"n": "bandit_approach"},
        spawns=[("bandit_cutthroat", 2), ("bandit_chieftain", 1)], level=(8, 10)),
}
