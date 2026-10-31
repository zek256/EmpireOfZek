"""Silverbough, the elven city in the Eldergrove (safe)."""
from data.rooms.common import R

ROOMS = {
    "sb_rootgate": R(
        "Silverbough: The Rootgate", "Silverbough",
        "The western gate of Silverbough is no gate at all, but the roots of two great trees grown "
        "together into an arch, guarded by elven wardens in green and silver. A smithy rings to the "
        "north, and a weaver's hall glows to the south.",
        {"w": "silver_approach", "e": "sb_court", "n": "sb_leafsong", "s": "sb_moonweave"}, safe=True),
    "sb_dawnbridge": R(
        "Silverbough: The Dawnbridge", "Silverbough",
        "A bridge of living branches arches over a stream into the city, catching the first light of "
        "morning through a gap in the canopy. Lanterns of silver glass hang from its rails. An inn "
        "stands to the north and the wardens' lodge to the south.",
        {"e": "silver_road", "w": "sb_court", "n": "sb_inn", "s": "sb_wardens"}, safe=True),
    "sb_court": R(
        "Silverbough: The Heartwood Court", "Silverbough",
        "A wide court of white flagstones lies at the foot of the greatest tree in the city, whose "
        "trunk is hollowed into halls and stairways that climb out of sight. Elves in pale silk pass "
        "quietly by. The Speaker's hall lies north, and the Thornward Gate south.",
        {"w": "sb_rootgate", "e": "sb_dawnbridge", "n": "sb_speaker", "s": "sb_thornward"}, safe=True),
    "sb_speaker": R(
        "Silverbough: The Hall of the Speaker", "Silverbough",
        "A hall grown rather than built, its walls of living wood curving up into a vault of leaves. "
        "Light falls in green shafts on a simple chair of white wood where the Speaker of Silverbough "
        "sits. A spiral stair winds up the trunk to the north.",
        {"s": "sb_court", "n": "sb_starwatch"}, npcs=["saelwyn"], safe=True),
    "sb_starwatch": R(
        "Silverbough: The Starwatch", "Silverbough",
        "A platform high in the crown of the great tree looks out over a sea of leaves. To the "
        "north you can see the Whispering Woods and the far smoke of Brightwater; to the south, "
        "a stain of grey spreading through the green, with a green fire burning at its heart.",
        {"s": "sb_speaker"}, safe=True),
    "sb_leafsong": R(
        "Silverbough: Leafsong Forge", "Silverbough",
        "A forge of white stone where elven smiths sing as they work, and the steel takes the shape "
        "of the song. Sabers, glaives and coats of leaf-scale hang on the walls like works of art.",
        {"s": "sb_rootgate"}, npcs=["ilyra"], safe=True),
    "sb_moonweave": R(
        "Silverbough: The Moonweave Hall", "Silverbough",
        "Looms of silver wood fill a long hall where weavers spin cloth from moonlight, or so they "
        "claim. Robes, gloves and slippers of shimmering grey silk are laid out on tables, and a "
        "rack of pale staves stands by the door.",
        {"n": "sb_rootgate"}, npcs=["caelum"], safe=True),
    "sb_inn": R(
        "Silverbough: The Silverleaf Inn", "Silverbough",
        "An inn built in the branches of a great tree, its rooms like nests linked by rope walks. A "
        "fire burns in a hearth of white stone, and the elves sing quietly over cups of green wine. "
        "Here you may rest in safety.",
        {"s": "sb_dawnbridge"}, npcs=["merewyn"], safe=True),
    "sb_wardens": R(
        "Silverbough: The Wardens' Lodge", "Silverbough",
        "A lodge of rough timber, the only building in Silverbough that looks like it was made with "
        "an axe. Bows and spears hang on the walls, and a map of the Eldergrove is painted on a "
        "stretched deerhide, its southern half smeared with grey.",
        {"n": "sb_dawnbridge"}, npcs=["faelan"], safe=True),
    "sb_thornward": R(
        "Silverbough: The Thornward Gate", "Silverbough",
        "The southern gate is a wall of silver thorns grown thick as a man's arm, opened only when "
        "the wardens ride out. Beyond it, the forest is grey and dead. The wardens on the gate look "
        "very tired.",
        {"n": "sb_court", "s": "blighted_glade"}, safe=True),
}
