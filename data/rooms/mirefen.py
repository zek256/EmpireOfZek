"""The Mirefen (15-22)."""
from data.rooms.common import R

ROOMS = {
    "mire_edge": R(
        "Edge of the Mirefen", "The Mirefen",
        "The road sinks into a land of black water, rotting reeds and twisted, moss-hung trees. "
        "Bubbles rise and burst with a stench of decay. Something large moves beneath the surface.",
        {"e": "crossroads", "w": "mire_deep", "s": "lizard_village"},
        spawns=[("bog_lurker", 3)], level=(15, 16)),
    "lizard_village": R(
        "Lizardfolk Stilt-Village", "The Mirefen",
        "Huts of reeds and mud perch on tall stilts above the water, connected by swaying rope bridges. "
        "Hissing voices fall silent as you approach, and spears are raised. A rope bridge sways off "
        "westward over the water, toward a drumming in the reeds.",
        {"n": "mire_edge", "w": "spawning_grounds"},
        spawns=[("lizardman_warrior", 4)], level=(16, 17)),
    "spawning_grounds": R(
        "The Spawning Grounds", "The Mirefen",
        "Clutches of leathery eggs lie half-buried in warm mud along the banks, watched over by "
        "lizardfolk shamans who rattle bone staves and chant to the swamp. A totem of stacked "
        "turtle shells rises from the shallows, crusted with offerings of fish and blood.",
        {"e": "lizard_village", "n": "mire_deep"},
        spawns=[("lizardman_shaman", 2), ("lizardman_warrior", 1)], level=(18, 19)),
    "mire_deep": R(
        "The Drowned Forest", "The Mirefen",
        "Dead trees rise from waist-deep water like the masts of sunken ships. Pale lights drift between "
        "them, beckoning. A huge shape, moss-covered and grunting, wades through the murk.",
        {"e": "mire_edge", "w": "serpent_pools", "s": "spawning_grounds", "n": "bogwood_hollow"},
        spawns=[("swamp_troll", 2), ("will_o_wisp", 2)], level=(17, 18)),
    "bogwood_hollow": R(
        "Bogwood Hollow", "The Mirefen",
        "Black water pools in a hollow ringed by bogwood trees, their bark gone soft and grey as a "
        "drowned man's skin. Logs lie half-sunk along the banks, and some of them have eyes. Will-o'-"
        "the-wisps bob above the water as if waiting for something. A steep path climbs north out "
        "of the swamp toward snow.",
        {"s": "mire_deep", "n": "fenward_pass"},
        spawns=[("fen_crocodile", 2), ("will_o_wisp", 1)], level=(20, 21)),
    "serpent_pools": R(
        "The Serpent Pools", "The Mirefen",
        "Steaming pools of green water are fringed with giant ferns. Great coils slide just beneath "
        "the surface. On a hummock to the north, smoke rises from a crooked chimney.",
        {"e": "mire_deep", "n": "hag_hut", "w": "leech_fens"},
        spawns=[("mire_serpent", 3)], level=(19, 20)),
    "leech_fens": R(
        "The Leech Fens", "The Mirefen",
        "The ground gives way entirely to a sucking brown fen, where every step sinks to the knee. "
        "Black shapes as long as boats undulate through the shallows, and the bleached bones of a "
        "drowned ox lie picked clean at the water's edge.",
        {"e": "serpent_pools"},
        spawns=[("giant_leech", 2), ("mire_serpent", 1)], level=(20, 21)),
    "hag_hut": R(
        "The Hag's Hut", "The Mirefen",
        "A crooked hut of black timber squats on chicken-like legs of twisted root. Inside, a cauldron "
        "bubbles with something that has eyes. Herbs, bones and caged birds hang from every rafter. "
        "A cackling voice greets you: 'Ooooh, fresh meat for Mother's pot!'",
        {"s": "serpent_pools"},
        spawns=[("bog_hag", 1)], level=(22, 22)),
}
