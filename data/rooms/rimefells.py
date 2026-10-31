"""The Rimefells, the snowy western spur of the Ironspine around Hearthdeep (10-20)."""
from data.rooms.common import R

ROOMS = {
    "frostfoot_trail": R(
        "The Frostfoot Trail", "Rimefells",
        "A trail of packed snow climbs from the western hills into a land of white fells and black "
        "rock, marked every hundred paces by a dwarven cairn. Wolf tracks cross and recross the "
        "path, and the wind has a bite that finds every gap in your cloak.",
        {"s": "old_watchtower", "n": "snowbound_meadow"},
        spawns=[("snow_wolf", 3)], level=(10, 11)),
    "snowbound_meadow": R(
        "The Snowbound Meadow", "Rimefells",
        "A wide bowl of snow between the fells, where the tops of buried fence posts show this was "
        "once grazing land. To the north, great doors are carved into the mountainside: the gate of "
        "Hearthdeep. Goblin tracks lead off west, and a frozen waterfall glitters to the east.",
        {"s": "frostfoot_trail", "w": "frost_goblin_warren", "e": "icefall", "n": "hearthdeep_gate"},
        spawns=[("snow_wolf", 1), ("frost_goblin", 2)], level=(11, 12)),
    "frost_goblin_warren": R(
        "The Frost Goblin Warren", "Rimefells",
        "Snow caves are dug into a drift as high as a house, linked by tunnels and stinking of smoke "
        "and wet fur. Stolen dwarven pots and a broken cart lie half-buried outside. Blue-lipped "
        "goblins peer from every hole, clutching spears tipped with black ice.",
        {"e": "snowbound_meadow", "w": "rimewood"},
        spawns=[("frost_goblin", 3)], level=(12, 13)),
    "icefall": R(
        "The Icefall", "Rimefells",
        "A waterfall froze mid-plunge here long ago, forming a curtain of blue ice that hangs over a "
        "cliff. Behind it, glassy webs stretch across the mouths of small caves, and things of pale "
        "chitin wait motionless in the cold.",
        {"w": "snowbound_meadow"},
        spawns=[("ice_spider", 3)], level=(13, 14)),
    "rimewood": R(
        "The Rimewood", "Rimefells",
        "A forest of dark firs bowed under snow, so silent that every footfall sounds loud. Frost "
        "webs hang between the trunks like grey curtains. A trail climbs north toward caves in the "
        "fellside, where something large has left handprints in the snow.",
        {"e": "frost_goblin_warren", "n": "yeti_caves"},
        spawns=[("ice_spider", 2), ("frost_goblin", 1)], level=(14, 15)),
    "yeti_caves": R(
        "The Yeti Caves", "Rimefells",
        "Wide, low caves open in the fellside, their floors deep in old bones and tufts of white "
        "fur. The stink of beast is overwhelming. Something huge grunts in the dark, and a pair of "
        "small, angry eyes catches the light.",
        {"s": "rimewood", "n": "frozen_tarn"},
        spawns=[("yeti", 3)], level=(15, 16)),
    "frozen_tarn": R(
        "The Frozen Tarn", "Rimefells",
        "A mountain lake lies frozen so clear that you can see fish trapped in the ice far below. "
        "Motes of blue light drift over its surface in the still air, circling slowly, and the cold "
        "here is deeper than the cold of the fells.",
        {"s": "yeti_caves", "n": "howling_heights"},
        spawns=[("frost_wisp", 2), ("ice_spider", 1)], level=(16, 17)),
    "howling_heights": R(
        "The Howling Heights", "Rimefells",
        "Wind screams over a knife-edge ridge between two peaks, driving snow sideways in stinging "
        "sheets. Yetis hunt along the ridge in the white-out, and lights move in the storm that are "
        "not lanterns.",
        {"s": "frozen_tarn", "n": "giantstep_ridge"},
        spawns=[("yeti", 2), ("frost_wisp", 1)], level=(17, 18)),
    "giantstep_ridge": R(
        "Giantstep Ridge", "Rimefells",
        "The ridge rises in great natural steps of black rock, each one taller than a man, which the "
        "dwarves say were cut by giants in the first days of the world. Snow trolls have made their "
        "lairs among the steps, and gnawed bones lie everywhere.",
        {"s": "howling_heights"},
        spawns=[("snow_troll", 2), ("yeti", 1)], level=(18, 19)),
    "cairn_saddle": R(
        "The Cairn Saddle", "Rimefells",
        "A high saddle of land between the fells, crowned with hundreds of stone cairns raised over "
        "dwarves who fell defending the eastern road. The East Door of Hearthdeep lies to the west, "
        "and the pass runs on eastward toward the Mirefen.",
        {"w": "hearthdeep_east_door", "e": "high_pass"},
        spawns=[("snow_troll", 2), ("frost_wisp", 1)], level=(18, 19)),
    "high_pass": R(
        "The High Pass", "Rimefells",
        "The road to the east squeezes between walls of ice-glazed rock, so narrow that a laden mule "
        "would scrape both sides. Troll dung and the remains of a dwarven caravan lie in the snow. "
        "Far below to the east, mist hangs over the Mirefen.",
        {"w": "cairn_saddle", "e": "fenward_pass"},
        spawns=[("snow_troll", 2), ("yeti", 1)], level=(19, 20)),
    "fenward_pass": R(
        "The Fenward Descent", "Rimefells",
        "The pass drops steeply out of the snow into a land of rotting reeds and black water, where "
        "frost still rimes the dead trees. Pale lights drift up from the swamp below, and a troll "
        "squats in the snowmelt, watching the path.",
        {"w": "high_pass", "s": "bogwood_hollow"},
        spawns=[("snow_troll", 1), ("will_o_wisp", 2)], level=(19, 20)),
}
