"""The Planes of the Gods, above the Temple of the Dawn (51-60).

Tier one (Sky, Growth, Fear) opens from the Threshold. Each leads on to elemental planes: Sky to Air,
Growth to Earth and Water, Fear to Fire. The Door of Time opens once all four elemental lords are
slain, and Lord Zek's throne only for a character who has lived every class to level 50.
"""
from data.rooms.common import R

ELEMENTAL_LORDS = ["lord_fire", "lord_water", "lord_earth", "lord_air"]

ROOMS = {
    # ================================================================= THE THRESHOLD (safe)
    "threshold_stair": R(
        "The Stair of Dawn", "Threshold of the Gods",
        "A stair of white light climbs from behind the altar of the Temple of the Dawn into a sky with "
        "no ground beneath it. Far below, Brightwater is a toy town. Above, gates of light stand open "
        "on worlds that are not this one, and to the south a single door of bronze stands shut.",
        {"d": "temple", "n": "threshold_court", "s": "time_gate"}, safe=True),
    "threshold_court": R(
        "The Threshold of the Gods", "Threshold of the Gods",
        "A court of white stone floats in an endless golden sky. Three gates stand open around it: "
        "north onto a storm of clouds, west onto a forest older than the world, and east onto a "
        "darkness that whispers your name. A herald in white waits beside a fountain of light.",
        {"s": "threshold_stair", "n": "sky_gate", "w": "growth_gate", "e": "fear_gate"},
        npcs=["herald"], safe=True),

    # ================================================================= PLANE OF SKY (51-55)
    "sky_gate": R(
        "Plane of Sky: The Cloudgate", "Plane of Sky",
        "You step through the gate onto a cloud that holds your weight like stone. Islands of white "
        "rock drift in an endless blue, linked by bridges of rainbow light. Eagles bigger than ships "
        "wheel overhead, lightning crawling along their wings.",
        {"s": "threshold_court", "n": "sky_isles"},
        spawns=[("storm_eagle", 2)], level=(51, 52)),
    "sky_isles": R(
        "Plane of Sky: The Floating Isles", "Plane of Sky",
        "A cluster of floating islands is joined by bridges of light, each isle crowned with a temple "
        "of white marble. Sentinels of stone stand at every bridge. North, the greatest isle carries "
        "a hall whose roof is a single cloud.",
        {"s": "sky_gate", "w": "sky_aerie", "e": "sky_storm", "n": "sky_hall"},
        spawns=[("storm_eagle", 1), ("cloud_sentinel", 1)], level=(52, 53)),
    "sky_aerie": R(
        "Plane of Sky: The Great Aerie", "Plane of Sky",
        "A floating crag is woven over with nests the size of houses, built from the masts of ships "
        "and the trunks of trees. Storm eagles screech and take wing at your approach.",
        {"e": "sky_isles"},
        spawns=[("storm_eagle", 3)], level=(51, 52)),
    "sky_storm": R(
        "Plane of Sky: The Stormfront", "Plane of Sky",
        "A wall of black cloud rolls across the sky, flickering with lightning. Rain falls upward here, "
        "and the sentinels stand in it unmoving. A path of cloud climbs north toward the peak of the "
        "storm.",
        {"w": "sky_isles", "n": "sky_thunder"},
        spawns=[("cloud_sentinel", 2), ("storm_eagle", 1)], level=(53, 54)),
    "sky_thunder": R(
        "Plane of Sky: Thunderpeak", "Plane of Sky",
        "At the top of the storm, a peak of black cloud is struck by lightning every few heartbeats. "
        "The air tastes of iron. Above it, the sky tears open onto a place of pure wind: the Plane "
        "of Air.",
        {"s": "sky_storm", "n": "air_gate"},
        spawns=[("cloud_sentinel", 2), ("storm_eagle", 1)], level=(53, 54)),
    "sky_hall": R(
        "Plane of Sky: The Hall of the Sky-Warden", "Plane of Sky",
        "A hall of white pillars open to the sky, its roof a single cloud. On a throne of silver mist "
        "sits a woman of storm with wings of cloud and a bow of lightning across her knees. 'Few "
        "mortals reach my hall,' says Caelestra. 'Fewer leave it. Show me why the king should "
        "know your name.'",
        {"s": "sky_isles"},
        spawns=[("caelestra", 1)], level=(55, 55)),

    # ================================================================= PLANE OF GROWTH (51-55)
    "growth_gate": R(
        "Plane of Growth: The Greengate", "Plane of Growth",
        "Beyond the gate lies a forest from before the first winter, its trees so vast that their "
        "crowns are lost in green light. The air is warm and thick with pollen. Somewhere a horn "
        "sounds, and white hounds bay in answer.",
        {"e": "threshold_court", "w": "growth_garden"},
        spawns=[("wild_hunt_hound", 2)], level=(51, 52)),
    "growth_garden": R(
        "Plane of Growth: The First Garden", "Plane of Growth",
        "A garden where every plant that has ever grown grows at once, flowers the size of shields "
        "beside trees heavy with fruit of every season. The hounds of the wild hunt run between the "
        "beds, and an ancient oak walks among them.",
        {"e": "growth_gate", "w": "growth_canopy", "n": "growth_thicket"},
        spawns=[("wild_hunt_hound", 2), ("ancient_treant", 1)], level=(52, 53)),
    "growth_thicket": R(
        "Plane of Growth: The Elder Thicket", "Plane of Growth",
        "Trunks crowd so close that you must squeeze between them, and some of the trunks move to let "
        "you pass, or not. Names of gods no one remembers are carved in the bark.",
        {"s": "growth_garden", "w": "growth_orchard"},
        spawns=[("ancient_treant", 2)], level=(53, 54)),
    "growth_orchard": R(
        "Plane of Growth: The Endless Orchard", "Plane of Growth",
        "Rows of fruit trees run to the horizon, their branches heavy with golden apples. To the west, "
        "the orchard ends at a shore of bright water that stretches into another world: the Plane "
        "of Water.",
        {"e": "growth_thicket", "s": "growth_canopy", "w": "water_gate"},
        spawns=[("ancient_treant", 1), ("wild_hunt_hound", 2)], level=(53, 54)),
    "growth_canopy": R(
        "Plane of Growth: The Root Canopy", "Plane of Growth",
        "Roots as thick as rivers arch overhead, forming a vault of living wood. Below, they plunge "
        "down into the dark, toward a deep place of stone: the Plane of Earth. West, green light "
        "pours from a great hollow tree.",
        {"e": "growth_garden", "n": "growth_orchard", "w": "growth_heart", "s": "earth_gate"},
        spawns=[("wild_hunt_hound", 1), ("ancient_treant", 1)], level=(53, 54)),
    "growth_heart": R(
        "Plane of Growth: The Heart of the Wild", "Plane of Growth",
        "Inside the hollow of the oldest tree, a woman as tall as the tree itself sits among its "
        "roots, crowned with antlers, her hair a forest. 'Everything that grows, I grew,' says "
        "Verdis. 'Grow, little one, or be cut down.'",
        {"e": "growth_canopy"},
        spawns=[("verdis", 1)], level=(55, 55)),

    # ================================================================= PLANE OF FEAR (51-55)
    "fear_gate": R(
        "Plane of Fear: The Dreadgate", "Plane of Fear",
        "Beyond the gate is a twilight that never ends, under a sky full of eyes. Black horses with "
        "manes of cold fire graze on grey grass, and look up at you, and smile.",
        {"w": "threshold_court", "e": "fear_road"},
        spawns=[("nightmare_steed", 2)], level=(51, 52)),
    "fear_road": R(
        "Plane of Fear: The Road of Nightmares", "Plane of Fear",
        "A road of cobbles runs between houses that look like the house you grew up in, except that "
        "every door is open and every window is dark. Someone calls your name from inside.",
        {"w": "fear_gate", "n": "fear_halls", "e": "fear_crossing"},
        spawns=[("nightmare_steed", 2), ("dread_wraith", 1)], level=(52, 53)),
    "fear_halls": R(
        "Plane of Fear: The Screaming Halls", "Plane of Fear",
        "A maze of narrow halls where the walls scream, quietly, all the time. Tall shadows walk "
        "the halls, wearing faces you know.",
        {"s": "fear_road", "e": "fear_mirrors"},
        spawns=[("dread_wraith", 2)], level=(53, 54)),
    "fear_mirrors": R(
        "Plane of Fear: The Hall of Mirrors", "Plane of Fear",
        "Every wall is a mirror, and in every mirror you are dying in a different way. Some of the "
        "reflections step out of the glass.",
        {"w": "fear_halls", "s": "fear_crossing"},
        spawns=[("dread_wraith", 2), ("nightmare_steed", 1)], level=(53, 54)),
    "fear_crossing": R(
        "Plane of Fear: The Crossroads of Dread", "Plane of Fear",
        "Four roads meet at a gallows where someone you love is hanging. It is not real. You know it "
        "is not real. South, the twilight burns red, opening on a world of fire. East, a throne "
        "waits in the dark.",
        {"w": "fear_road", "n": "fear_mirrors", "e": "fear_throne", "s": "fire_gate"},
        spawns=[("nightmare_steed", 2)], level=(53, 54)),
    "fear_throne": R(
        "Plane of Fear: The Throne of Dread", "Plane of Fear",
        "A throne of black glass stands in a darkness so total that you cannot see your own hand. "
        "Then a hundred faces light up in the dark, every one of them someone you have lost. 'I am "
        "Vhaal,' they say together. 'And I know you.'",
        {"w": "fear_crossing"},
        spawns=[("vhaal", 1)], level=(55, 55)),

    # ================================================================= PLANE OF FIRE (54-58)
    "fire_gate": R(
        "Plane of Fire: The Burning Gate", "Plane of Fire",
        "You step out of the twilight onto a plain of black glass beneath a sky of flame. The heat "
        "would kill a lesser being in a breath. Spirits of fire with brass bracers turn their burning "
        "eyes on you.",
        {"n": "fear_crossing", "s": "fire_lava"},
        spawns=[("efreet", 2)], level=(54, 55)),
    "fire_lava": R(
        "Plane of Fire: The Sea of Lava", "Plane of Fire",
        "A sea of molten rock stretches to every horizon, crossed by causeways of black glass. Birds of "
        "living fire skim the surface, and the efreet bathe in it.",
        {"n": "fire_gate", "w": "fire_cinders", "e": "fire_pyre", "s": "fire_furnace"},
        spawns=[("efreet", 1), ("pyre_phoenix", 1)], level=(55, 56)),
    "fire_cinders": R(
        "Plane of Fire: The Cinder Fields", "Plane of Fire",
        "Fields of white-hot cinders drift like snow in a wind of fire. The efreet hunt here in "
        "packs, laughing.",
        {"e": "fire_lava"},
        spawns=[("efreet", 2)], level=(55, 56)),
    "fire_pyre": R(
        "Plane of Fire: The Phoenix Pyre", "Plane of Fire",
        "A mountain of burning wood that never burns away, where the phoenixes come to die and be "
        "reborn. Eggs of fire crack open in the flames.",
        {"w": "fire_lava"},
        spawns=[("pyre_phoenix", 2)], level=(56, 57)),
    "fire_furnace": R(
        "Plane of Fire: The Great Furnace", "Plane of Fire",
        "A furnace the size of a city roars in the heart of the plane, and the light of it is too "
        "bright to look at. South, in the white heart of the flame, something vast is waiting.",
        {"n": "fire_lava", "s": "fire_throne"},
        spawns=[("pyre_phoenix", 1), ("efreet", 1)], level=(56, 57)),
    "fire_throne": R(
        "Plane of Fire: The Throne of Flame", "Plane of Fire",
        "At the heart of the Great Furnace, on a throne of white-hot stone, sits a giant with a crown "
        "of fire and a hammer that is a captive star. Ignaros rises. 'Burn bright,' he says, 'and I "
        "will remember your light.'",
        {"n": "fire_furnace"},
        spawns=[("lord_fire", 1)], level=(58, 58)),

    # ================================================================= PLANE OF WATER (54-58)
    "water_gate": R(
        "Plane of Water: The Bright Shore", "Plane of Water",
        "The orchard ends at a shore of white sand, and the sea beyond is the Plane of Water: an "
        "ocean without a bottom or a far shore, where you can somehow breathe. Waves with cold eyes "
        "roll in toward you.",
        {"e": "growth_orchard", "w": "water_shallows"},
        spawns=[("tide_elemental", 2)], level=(54, 55)),
    "water_shallows": R(
        "Plane of Water: The Endless Shallows", "Plane of Water",
        "Blue-green water stretches in every direction, waist-deep and warm. Reefs rise to the north, "
        "kelp forests sway to the south, and to the west the sea floor drops away into a blackness "
        "that goes down forever.",
        {"e": "water_gate", "w": "water_abyss", "n": "water_reef", "s": "water_kelp"},
        spawns=[("tide_elemental", 1), ("abyssal_kraken", 1)], level=(55, 56)),
    "water_reef": R(
        "Plane of Water: The Coral Cathedral", "Plane of Water",
        "A reef has grown into the shape of a vast cathedral, with spires of coral and windows of "
        "living fish. Tide elementals move through its aisles like a congregation.",
        {"s": "water_shallows"},
        spawns=[("tide_elemental", 2)], level=(55, 56)),
    "water_kelp": R(
        "Plane of Water: The Kelp Forest", "Plane of Water",
        "Kelp as tall as the trees of the Eldergrove sways in a slow current, dimming the light to "
        "green. Tentacles as thick as towers coil between the stalks.",
        {"n": "water_shallows"},
        spawns=[("abyssal_kraken", 1), ("tide_elemental", 1)], level=(56, 57)),
    "water_abyss": R(
        "Plane of Water: The Abyss", "Plane of Water",
        "You sink into the lightless deep, where the cold is crushing and the only light comes from "
        "the eyes of things that should not exist. Krakens drift past like thunderclouds. Further "
        "west, a palace of green sea-glass glows on the edge of the abyss.",
        {"e": "water_shallows", "w": "water_throne"},
        spawns=[("abyssal_kraken", 2)], level=(56, 57)),
    "water_throne": R(
        "Plane of Water: The Palace of the Tides", "Plane of Water",
        "A palace of green sea-glass stands on the brink of the abyss, its halls flooded with silver "
        "light. On a throne of pearl sits a crowned giant with a trident of coral. 'The tide takes "
        "all things,' says Nerevos. 'Let us see if it takes you.'",
        {"e": "water_abyss"},
        spawns=[("lord_water", 1)], level=(58, 58)),

    # ================================================================= PLANE OF EARTH (54-58)
    "earth_gate": R(
        "Plane of Earth: The Root Descent", "Plane of Earth",
        "The roots of the Plane of Growth plunge down through solid rock, and you follow them into "
        "the Plane of Earth, a world of stone without a sky. Shapes of living granite step out of "
        "the walls.",
        {"n": "growth_canopy", "s": "earth_caverns"},
        spawns=[("granite_elemental", 2)], level=(54, 55)),
    "earth_caverns": R(
        "Plane of Earth: The Endless Caverns", "Plane of Earth",
        "Caverns open one into another without end, lit by veins of glowing ore. Crystal glitters to "
        "the west, great roots grip the stone to the east, and a deeper dark lies to the south.",
        {"n": "earth_gate", "w": "earth_crystal", "e": "earth_root", "s": "earth_deeps"},
        spawns=[("granite_elemental", 1), ("crystal_basilisk", 1)], level=(55, 56)),
    "earth_crystal": R(
        "Plane of Earth: The Crystal Gardens", "Plane of Earth",
        "Crystals as tall as towers grow in a cavern of blinding light, and statues of glass stand "
        "among them: everything the basilisks have ever looked at.",
        {"e": "earth_caverns"},
        spawns=[("crystal_basilisk", 2)], level=(56, 57)),
    "earth_root": R(
        "Plane of Earth: The Root of the World", "Plane of Earth",
        "The deepest roots of the world tree pierce the stone here, older than mountains, and granite "
        "elementals tend them like gardeners.",
        {"w": "earth_caverns"},
        spawns=[("granite_elemental", 2)], level=(55, 56)),
    "earth_deeps": R(
        "Plane of Earth: The Grinding Deeps", "Plane of Earth",
        "The walls of the deeps move, slowly, grinding against each other with a sound that you feel "
        "in your teeth. Basilisks of living crystal pick their way across the shifting floor. South, "
        "a mountain is waiting.",
        {"n": "earth_caverns", "s": "earth_throne"},
        spawns=[("crystal_basilisk", 2), ("granite_elemental", 1)], level=(56, 57)),
    "earth_throne": R(
        "Plane of Earth: The Heart of the Mountain", "Plane of Earth",
        "A cavern so vast that you cannot see its walls, and at its heart a mountain that is not a "
        "mountain. It opens two crystal eyes. 'I was here before your world,' says Ulmathra, 'and I "
        "will be here after it. Strike, and be remembered.'",
        {"n": "earth_deeps"},
        spawns=[("lord_earth", 1)], level=(58, 58)),

    # ================================================================= PLANE OF AIR (54-58)
    "air_gate": R(
        "Plane of Air: The Windgate", "Plane of Air",
        "Above the storm there is no ground at all, only a sky of silver wind that holds you up like "
        "water. Columns of black cloud howl past, crackling with lightning.",
        {"s": "sky_thunder", "n": "air_cyclone"},
        spawns=[("storm_elemental", 2)], level=(54, 55)),
    "air_cyclone": R(
        "Plane of Air: The Eye of the Cyclone", "Plane of Air",
        "You stand in the calm eye of a cyclone a hundred leagues across, its walls a spinning storm. "
        "Birds the size of clouds circle overhead, and a silver crown of lightning flickers far to "
        "the north.",
        {"s": "air_gate", "w": "air_vortex", "e": "air_spires", "n": "air_throne"},
        spawns=[("storm_elemental", 1), ("thunderbird", 1)], level=(55, 56)),
    "air_vortex": R(
        "Plane of Air: The Howling Vortex", "Plane of Air",
        "A whirlpool of wind spins down into nothing, dragging lightning with it. The storm elementals "
        "ride its walls like children on a swing.",
        {"e": "air_cyclone"},
        spawns=[("storm_elemental", 2)], level=(55, 56)),
    "air_spires": R(
        "Plane of Air: The Cloud Spires", "Plane of Air",
        "Spires of solid cloud rise from nowhere into nowhere, and thunderbirds nest on their tops. "
        "The sound of their wings is the sound of a storm breaking.",
        {"w": "air_cyclone", "n": "air_heights"},
        spawns=[("thunderbird", 2)], level=(56, 57)),
    "air_heights": R(
        "Plane of Air: The Highest Heights", "Plane of Air",
        "Above the spires, the air grows so thin that it glitters. Lightning walks here on legs of "
        "light, and the thunderbirds circle in a great ring.",
        {"s": "air_spires"},
        spawns=[("thunderbird", 2), ("storm_elemental", 1)], level=(56, 57)),
    "air_throne": R(
        "Plane of Air: The Court of the Winds", "Plane of Air",
        "Four winds meet in a court with no floor and no walls, and in the middle of them stands a "
        "shape of silver storm with a crown of lightning. 'Never still,' says Zephyrion, 'never "
        "caught. Catch me, and the king will hear of it.'",
        {"s": "air_cyclone"},
        spawns=[("lord_air", 1)], level=(58, 58)),

    # ================================================================= PLANE OF TIME (57-60)
    "time_gate": R(
        "The Door of Time", "Plane of Time",
        "Beyond the bronze door lies a hall of silence where every clock that was ever made hangs on "
        "the walls, each telling a different hour. The door shuts behind you without a sound. South, "
        "the Plane of Time turns like a great wheel.",
        {"n": "threshold_stair", "s": "time_hourglass"}, safe=True,
        gate={"kills": ELEMENTAL_LORDS,
              "msg": "The bronze door is carved with four sigils: a flame, a wave, a mountain and a "
                     "whirlwind. It will not open until the four elemental lords have fallen to you."}),
    "time_hourglass": R(
        "Plane of Time: The Great Hourglass", "Plane of Time",
        "You stand inside an hourglass the size of a mountain, on a floor of golden sand that pours "
        "upward toward a sky of stars. Knights of brass and crystal march through the falling sand, "
        "leaving afterimages behind them.",
        {"n": "time_gate", "w": "time_past", "e": "time_future", "s": "time_eternity"},
        spawns=[("chronal_sentinel", 2)], level=(57, 58)),
    "time_past": R(
        "Plane of Time: The Halls of the Past", "Plane of Time",
        "Every moment that has ever happened is kept here, frozen in glass, in halls that go on "
        "forever. You see Elandor whole and Pyraxis young. Golems of glass and bronze guard the "
        "moments jealously.",
        {"e": "time_hourglass"},
        spawns=[("hourglass_golem", 2)], level=(58, 58)),
    "time_future": R(
        "Plane of Time: The Shores of Tomorrow", "Plane of Time",
        "A grey shore at the edge of everything that has not happened yet. Figures walk out of the "
        "mist toward you, and every one of them is you, older, or stranger, or worse.",
        {"w": "time_hourglass"},
        spawns=[("paradox", 2)], level=(59, 59)),
    "time_eternity": R(
        "Plane of Time: The Stair of Eternity", "Plane of Time",
        "A stair climbs through every age of the world at once: you pass the first dawn, the fall of "
        "Elandor, and a Brightwater that has not been built yet. At its top stands a door of white "
        "gold, carved with a crown.",
        {"n": "time_hourglass", "s": "zek_throne"},
        spawns=[("chronal_sentinel", 1), ("hourglass_golem", 1), ("paradox", 1)], level=(58, 59)),
    "zek_throne": R(
        "The Throne of Zek", "Plane of Time",
        "A hall at the end of time, its walls the night sky as it will be on the last day. On a throne "
        "carved from the first moment sits the king of the gods. His face is every face, and his "
        "eyes hold every dawn. Lord Zek rises, and lifts the sword called Eternity. 'You have walked "
        "every path,' he says. 'Now walk the last.'",
        {"n": "time_eternity"},
        spawns=[("lord_zek", 1)], level=(60, 60),
        gate={"all_classes": True,
              "msg": "The white-gold door does not move. A voice older than the stars speaks from beyond "
                     "it: 'Only one who has walked every path to its end may stand before the throne.'"}),
}
