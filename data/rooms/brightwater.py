"""Brightwater, the town at the centre of the world (safe)."""
from data.rooms.common import R

ROOMS = {
    "town_square": R(
        "Brightwater Town Square", "Brightwater",
        "Cobblestones worn smooth by centuries of feet spread out around a great marble fountain, "
        "where a statue of the Dawnfather raises a sun-disc toward the sky. Merchants cry their wares, "
        "children chase pigeons, and the smell of fresh bread drifts from somewhere nearby. The Gilded "
        "Griffin Inn stands to the west, the Temple of the Dawn to the east, the market street runs "
        "north and the south road leads toward the gate.",
        {"n": "market_street", "w": "inn", "e": "temple", "s": "south_road"}, safe=True),
    "inn": R(
        "The Gilded Griffin Inn", "Brightwater",
        "A warm common room of dark oak beams and crackling hearthfire. Tankards clatter, a lute plays "
        "somewhere in the corner, and a gilded griffin carved above the bar watches over the patrons. "
        "A trapdoor behind the bar leads down into the cellar. Here you may rest in safety.",
        {"e": "town_square", "d": "cellar"}, npcs=["bram"], safe=True),
    "cellar": R(
        "The Inn Cellar", "Brightwater",
        "Damp stone walls sweat in the lamplight. Casks of ale and sacks of grain are stacked high, many "
        "of them gnawed open. Something squeaks and skitters in the shadows between the barrels.",
        {"u": "inn"}, spawns=[("giant_rat", 4), ("cellar_spider", 1)], level=(1, 2)),
    "temple": R(
        "The Temple of the Dawn", "Brightwater",
        "Sunlight pours through tall windows of stained glass, painting the white marble floor in gold "
        "and rose. Incense curls before a great altar where an eternal flame burns. Robed acolytes move "
        "softly between the pews. Those who fall in battle awaken here, under the Dawnfather's grace. "
        "Behind the altar, a stair of white light climbs up into nothing.",
        {"w": "town_square", "u": "threshold_stair"}, npcs=["aveline"], safe=True),
    "market_street": R(
        "Market Street", "Brightwater",
        "A bustling lane of timber-framed shops leans over the street. The ring of a hammer on an anvil "
        "sounds from the smithy to the west, and a cheerful painted sign to the east announces "
        "'Mirela's Sundries & Tinctures'. The north gate rises at the end of the street.",
        {"s": "town_square", "w": "smithy", "e": "general_store", "n": "north_gate"}, safe=True),
    "smithy": R(
        "Ironhand Smithy", "Brightwater",
        "Heat rolls off a roaring forge. Racks of swords, axes, maces and bows line the soot-blackened "
        "walls, and suits of mail hang from hooks like hollow knights. A broad-shouldered smith works "
        "the bellows.",
        {"e": "market_street"}, npcs=["durgan"], safe=True),
    "general_store": R(
        "Mirela's Sundries & Tinctures", "Brightwater",
        "Shelves crammed with jars, bottles, bundles of herbs and coils of rope rise to the ceiling. "
        "Bubbling alembics fill the shop with the scent of mint and sulphur.",
        {"w": "market_street"}, npcs=["mirela"], safe=True),
    "north_gate": R(
        "The North Gate", "Brightwater",
        "Twin towers of grey stone flank a great iron-bound gate. Guards in blue tabards stand watch, "
        "eyes on the King's Road that winds north into the hills. A sturdy barracks stands to the east, "
        "and a lane runs west along the inside of the wall to the West Gate.",
        {"s": "market_street", "n": "kings_road", "e": "barracks", "w": "west_gate"}, safe=True),
    "west_gate": R(
        "The West Gate", "Brightwater",
        "A squat gatehouse of weathered stone guards the town's western wall, its gates thrown open "
        "for the farm carts that rumble in each morning. Beyond lie the hedgerows and barley fields "
        "of the Westmarch, and far off on the horizon, white hills where the dwarves live.",
        {"e": "north_gate", "w": "westmarch_road"}, safe=True),
    "barracks": R(
        "The Guard Barracks", "Brightwater",
        "Rows of cots, racks of spears, and a long table strewn with maps. A map of the region is pinned "
        "to the wall, with red pins marking bandit sightings in the Whispering Woods.",
        {"w": "north_gate"}, npcs=["halvard"], safe=True),
    "south_road": R(
        "The South Road", "Brightwater",
        "Neat cottages with flower boxes line the road as it runs toward the low southern gate. To the "
        "west, a narrow shopfront of blue-painted wood hangs a silver sign of a needle threading a star. "
        "A lane runs east to the East Gate. Beyond the town wall, golden fields roll away toward a "
        "dark smudge of forest.",
        {"n": "town_square", "s": "meadow_path", "w": "silverthread", "e": "east_gate"}, safe=True),
    "east_gate": R(
        "The East Gate", "Brightwater",
        "A narrow gate in the eastern wall opens onto the Dustway, a pale road that runs arrow-straight "
        "toward a hazy, reddish horizon. Caravan drivers water their mules at a trough here, swapping "
        "stories of gnolls, highwaymen, and a city of gold beyond the sands.",
        {"w": "south_road", "e": "dustway_road"}, safe=True),
    "silverthread": R(
        "Silverthread Arcana", "Brightwater",
        "Bolts of shimmering cloth in midnight blue, violet and silver hang from the rafters, and glass "
        "cases hold wands, orbs and rings that glimmer with faint inner light. The air smells of lavender "
        "and candle wax. Behind a counter heaped with spellbooks, an elegant woman threads a needle "
        "that glows like a falling star.",
        {"e": "south_road"}, npcs=["elowen"], safe=True),
}
