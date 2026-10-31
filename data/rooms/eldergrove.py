"""The Eldergrove, the ancient elven forest south and west of Brightwater (20-34)."""
from data.rooms.common import R

ROOMS = {
    # ------------------------------------------------- the western arm, up to the Westmarch quarry (20-26)
    "westwood_verge": R(
        "The Westwood Verge", "Eldergrove",
        "Beyond the quarry, the land drops into the edge of a forest so old that its trees are wider "
        "than houses. The air turns green and still, birdsong falls away, and something large crashes "
        "through the undergrowth nearby.",
        {"n": "quarry_depths", "s": "old_greenway"},
        spawns=[("thornback_boar", 2), ("centaur_outrider", 1)], level=(20, 21)),
    "old_greenway": R(
        "The Old Greenway", "Eldergrove",
        "A broad ride runs south between the trees, kept open by centaur hooves rather than any axe. "
        "Painted skulls of deer hang from the branches to mark the herd's land, and hoofbeats drum "
        "somewhere out of sight.",
        {"n": "westwood_verge", "s": "owlwood"},
        spawns=[("centaur_outrider", 3)], level=(21, 22)),
    "owlwood": R(
        "The Owlwood", "Eldergrove",
        "Dead oaks stand among the living here, hollowed out and riddled with holes as big as doors. "
        "Pellets of fur and bone litter the ground beneath them. Huge grey shapes sit motionless on "
        "the branches, and their heads turn to follow you.",
        {"n": "old_greenway", "e": "centaur_run", "s": "mossy_stones"},
        spawns=[("dusk_owl", 2), ("centaur_outrider", 1)], level=(22, 23)),
    "centaur_run": R(
        "The Centaur Run", "Eldergrove",
        "A long glade of trampled grass where the centaurs race and fight for rank. Spears are planted "
        "in a ring at its centre, hung with ribbons and scalps, and a herd of painted riders wheels "
        "to face you.",
        {"w": "owlwood", "s": "troll_hollow"},
        spawns=[("centaur_outrider", 3)], level=(22, 23)),
    "troll_hollow": R(
        "Troll Hollow", "Eldergrove",
        "A sunken hollow choked with roots, where wood trolls have dug their dens under the biggest "
        "trees. The smell is appalling. Gnawed bones and the remains of a centaur lie by the nearest "
        "den, and something inside is snoring.",
        {"n": "centaur_run", "w": "mossy_stones"},
        spawns=[("wood_troll", 2)], level=(23, 24)),
    "mossy_stones": R(
        "The Mossy Stones", "Eldergrove",
        "A ring of standing stones, so overgrown with moss that they look like green giants frozen "
        "mid-dance, stands in a clearing. The elves raised them before Elandor fell. Owls watch from "
        "the stones, and a troll squats at the centre, scratching.",
        {"n": "owlwood", "e": "troll_hollow", "s": "briar_maze"},
        spawns=[("wood_troll", 1), ("dusk_owl", 1)], level=(23, 24)),
    "briar_maze": R(
        "The Briar Maze", "Eldergrove",
        "Walls of bramble taller than a man twist into a maze of narrow, thorny passages. Tiny lights "
        "flit along the tops of the briars, giggling, and every path seems to lead back to where you "
        "started.",
        {"n": "mossy_stones", "s": "stag_walk"},
        spawns=[("thorn_sprite", 3)], level=(24, 25)),
    "stag_walk": R(
        "The Stag Walk", "Eldergrove",
        "Huge white stags move in silence between pillars of silver-barked trees, browsing on the "
        "high branches. The elves say they are sacred, and woe to the hunter who takes one without "
        "leave. To the south, the green begins to turn grey.",
        {"n": "briar_maze", "s": "weeping_pines"},
        spawns=[("greatstag", 2), ("thorn_sprite", 1)], level=(25, 26)),
    # ------------------------------------------------- the western blight (26-30)
    "weeping_pines": R(
        "The Weeping Pines", "Eldergrove",
        "The pines here weep black sap that pools on the ground and smells of rot. Grey fungus climbs "
        "the trunks in brackets like stairs, and one of the trees nearby is slowly, painfully pulling "
        "its roots out of the earth.",
        {"n": "stag_walk", "s": "rotting_brake"},
        spawns=[("blighted_treant", 1), ("greatstag", 1)], level=(26, 27)),
    "rotting_brake": R(
        "The Rotting Brake", "Eldergrove",
        "A thicket of dead and dying trees, black and soft as wet paper. Every step sinks into rot. "
        "Treants walk here, or what is left of them, groaning like ships in a storm.",
        {"n": "weeping_pines", "s": "druids_ring"},
        spawns=[("blighted_treant", 2)], level=(27, 28)),
    "druids_ring": R(
        "The Druids' Ring", "Eldergrove",
        "A circle of oaks once sacred to the old druids has been turned to the blight's service. "
        "Fungus-bearded figures tend fires that burn green, and offerings of rotten fruit lie at the "
        "foot of each tree. A pale path leads east toward Silverbough.",
        {"n": "rotting_brake", "e": "silver_approach", "s": "fungal_barrows"},
        spawns=[("rotwood_druid", 1), ("blighted_treant", 1)], level=(28, 29)),
    "silver_approach": R(
        "The Silver Approach", "Eldergrove",
        "The blight falls back here, held off by a line of silver-barked trees that the elves have "
        "sung into a living wall. Lanterns hang in the branches to the east, where the gates of "
        "Silverbough stand among the roots of the great trees.",
        {"w": "druids_ring", "e": "sb_rootgate"},
        spawns=[("greatstag", 2)], level=(26, 27)),
    "fungal_barrows": R(
        "The Fungal Barrows", "Eldergrove",
        "Old elven barrows rise here, swallowed by fungus that glows a faint green in the gloom. The "
        "rotwood druids dig among them for something, and grey wolves with green eyes nose through "
        "the spoil.",
        {"n": "druids_ring"},
        spawns=[("rotwood_druid", 2), ("blight_wolf", 1)], level=(29, 30)),
    # ------------------------------------------------- the eastern grove, from the Whispering Woods (20-27)
    "grove_verge": R(
        "The Grove Verge", "Eldergrove",
        "The Old South Way passes under an arch formed by two trees grown together, and the Whispering "
        "Woods give way to the Eldergrove. Everything is suddenly bigger: ferns like trees, trees like "
        "towers, and boar tracks as wide as shields.",
        {"n": "old_south_way", "w": "silver_road", "s": "sprite_dells"},
        spawns=[("thornback_boar", 2), ("centaur_outrider", 1)], level=(20, 21)),
    "silver_road": R(
        "The Silver Road", "Eldergrove",
        "A road of pale stone, swept clean, runs west beneath the great trees, its edges lined with "
        "silver lamps on slender poles. Centaurs watch from the shadows, and owls hunt overhead. The "
        "Dawnbridge of Silverbough lies at the road's end.",
        {"e": "grove_verge", "w": "sb_dawnbridge"},
        spawns=[("centaur_outrider", 2), ("dusk_owl", 1)], level=(21, 22)),
    "sprite_dells": R(
        "The Sprite Dells", "Eldergrove",
        "A tumble of small green dells, each with its own spring and its own ring of toadstools. "
        "Laughter like breaking twigs follows you from dell to dell, and something gnarled and green "
        "is drinking from the largest spring.",
        {"n": "grove_verge", "s": "whitestag_glade"},
        spawns=[("thorn_sprite", 2), ("wood_troll", 1)], level=(24, 25)),
    "whitestag_glade": R(
        "The Whitestag Glade", "Eldergrove",
        "A wide glade where the greatstags gather to rut, the ground torn up by hooves and antlers. "
        "At its western edge, the trees are black, and a treant stands among them like a gallows.",
        {"n": "sprite_dells", "w": "wolfrot_den"},
        spawns=[("greatstag", 2), ("blighted_treant", 1)], level=(26, 27)),
    # ------------------------------------------------- the blighted south (29-34)
    "blighted_glade": R(
        "The Blighted Glade", "Eldergrove",
        "Beyond the Thornward Gate, the blight is everywhere. The grass is grey ash, the trees are "
        "black and weeping, and the air is thick with drifting spores. Treants lurch through the "
        "murk, tended by druids who sing to them like children.",
        {"n": "sb_thornward", "e": "withered_hollow", "s": "gloaming_mere"},
        spawns=[("blighted_treant", 2), ("rotwood_druid", 1)], level=(29, 30)),
    "withered_hollow": R(
        "The Withered Hollow", "Eldergrove",
        "A hollow of dead bracken and bare, white-barked trees, like a forest of bones. Blight wolves "
        "lope through it in a silent pack, their eyes glowing green.",
        {"w": "blighted_glade", "e": "wolfrot_den"},
        spawns=[("blight_wolf", 2), ("blighted_treant", 1)], level=(30, 31)),
    "wolfrot_den": R(
        "The Wolfrot Den", "Eldergrove",
        "The roots of a fallen giant have made a cave, and the blight wolves have made it their den. "
        "Bones and fungus carpet the floor, and the pack's growling fills the dark.",
        {"w": "withered_hollow", "e": "whitestag_glade"},
        spawns=[("blight_wolf", 3)], level=(31, 32)),
    "gloaming_mere": R(
        "The Gloaming Mere", "Eldergrove",
        "A black lake lies under trees so dense that it is always dusk. Dryads stand knee-deep in the "
        "water, singing to the dying trees they are bound to, and the song makes your eyes heavy. "
        "To the south, a green fire burns at the heart of the blight.",
        {"n": "blighted_glade", "s": "heart_of_blight"},
        spawns=[("gloom_dryad", 2), ("rotwood_druid", 1)], level=(32, 34)),
    "heart_of_blight": R(
        "The Heart of the Blight", "Eldergrove",
        "The oldest tree in the world stands here, black and hollow, its trunk split open around a "
        "heart of green fire. Its roots heave the earth for a hundred paces, and the rotwood druids "
        "kneel to it. The great tree moves, and a voice like splitting timber fills the glade: "
        "'Little sapling. You will feed the grove.'",
        {"n": "gloaming_mere"},
        spawns=[("rotheart", 1)], level=(33, 33)),
}
