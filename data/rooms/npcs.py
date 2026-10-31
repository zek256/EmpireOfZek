"""Non-player characters: shopkeepers and quest givers."""

NPCS = {
    "bram": {
        "name": "Bram the innkeeper", "keywords": ["bram", "innkeeper", "barkeep"],
        "desc": "A stout, red-bearded man with a stained apron and a booming laugh.",
        "greeting": "'Welcome to the Gilded Griffin, friend! Rest your bones, the beds are soft and "
                    "the ale is cold. Type REST to sleep here in safety.'",
        "quests": ["cellar_rats"],
    },
    "aveline": {
        "name": "Sister Aveline", "keywords": ["aveline", "sister", "priestess"],
        "desc": "A serene priestess in white and gold robes, a sun-disc upon her brow. Her eyes are kind but tired.",
        "greeting": "'May the Dawnfather light your path, traveller. Should you fall, it is here you "
                    "shall awaken.'",
        "quests": ["bone_king", "bog_hag", "salt_wraiths"],
    },
    "durgan": {
        "name": "Durgan Ironhand", "keywords": ["durgan", "smith", "blacksmith"],
        "desc": "A broad, soot-streaked smith with forearms like oak branches and a braided grey beard.",
        "greeting": "'Need steel? You've come to the right forge. Type LIST to see my wares. For finer "
                    "work than mine, you'll want my sister Brakka in Hearthdeep - out the West Gate and "
                    "north into the snow.'",
        "shop": ["iron_longsword", "steel_dagger", "yew_longbow", "runed_staff", "iron_mace",
                 "knights_blade", "leather_jerkin", "leather_gloves", "leather_leggings",
                 "iron_buckler", "studded_gloves", "chain_shirt", "iron_helm", "chain_leggings",
                 "iron_boots", "knight_breastplate", "steel_kite_shield", "plate_gauntlets",
                 "hardened_leather_cap", "studded_leggings", "chain_mittens", "studded_jerkin",
                 "steel_greathelm", "steel_sabatons"],
    },
    "elowen": {
        "name": "Elowen Silverthread", "keywords": ["elowen", "silverthread", "enchantress", "tailor"],
        "desc": "A tall, silver-haired high elf in robes of shifting violet, with ink-stained fingers and "
                "eyes that seem to read the magic in everything they rest upon.",
        "greeting": "'Steel is for those who cannot think their way out of trouble. For the rest of us, "
                    "there is silk, starlight and a well-chosen wand. Type LIST to see my wares.'",
        "shop": ["linen_robe", "apprentice_hood", "silk_gloves", "felt_slippers", "woven_trousers",
                 "copper_focus_ring", "wand_of_sparks", "moonstone_pendant", "acolyte_robe",
                 "crystal_orb", "spellweave_hood", "willow_staff", "enchanted_gloves",
                 "mystic_leggings", "spellbinder_robe", "runebound_slippers", "sapphire_ring",
                 "archivist_robe", "warded_grimoire"],
        "quests": ["blight_spreads"],
    },
    "mirela": {
        "name": "Mirela the alchemist", "keywords": ["mirela", "alchemist", "shopkeeper"],
        "desc": "A spry old woman with spectacles perched on her nose and purple-stained fingers.",
        "greeting": "'Potions, tinctures, elixirs! Something for every ache, dearie. Type LIST to browse.'",
        "shop": ["minor_healing_potion", "minor_mana_potion", "healing_potion", "mana_potion",
                 "greater_healing_potion", "greater_mana_potion", "supreme_healing_potion",
                 "supreme_mana_potion", "ring_of_vigor"],
    },
    "halvard": {
        "name": "Captain Halvard", "keywords": ["halvard", "captain", "guard"],
        "desc": "A grizzled veteran in a blue tabard, his face crossed with old scars.",
        "greeting": "'Keep your blade sharp, citizen. The roads aren't safe these days.'",
        "quests": ["wolf_pelts", "bandit_chief", "frost_goblins", "orc_warlord"],
    },
    # ------------------------------------------------------------------- Westmarch
    "haverick": {
        "name": "Farmer Wil Haverick", "keywords": ["wil", "haverick", "farmer"],
        "desc": "A sunburnt, broad-handed farmer with straw in his hair and a pitchfork he plainly means to use.",
        "greeting": "'Thornbury's a quiet place, or it was. Mind the goblins on the road west.'",
        "quests": ["goblin_raiders"],
    },
    # ------------------------------------------------------------------- Hearthdeep
    "orla": {
        "name": "Captain Orla Frostbeard", "keywords": ["orla", "frostbeard", "captain"],
        "desc": "A stocky dwarf in rime-crusted mail, her beard braided with iron rings and her eyes as hard as flint.",
        "greeting": "'The Gatewatch keeps the snow out and the trouble with it. Mostly.'",
        "quests": ["yeti_menace"],
    },
    "brakka": {
        "name": "Brakka Ironhand", "keywords": ["brakka", "ironhand", "smith", "blacksmith"],
        "desc": "A broad dwarf with arms like anvils and a braided red beard tucked into her leather apron. "
                "She has her brother Durgan's nose and none of his patience.",
        "greeting": "'Dwarven steel, the best under the mountain. My brother sells the cheap stuff down in "
                    "Brightwater. Type LIST to see real work.'",
        "shop": ["dwarven_war_axe", "dwarven_chainmail", "dwarven_crossbow", "runeforged_hammer",
                 "dwarven_helm", "dwarven_boots", "dwarven_greataxe", "dwarven_greaves",
                 "mithril_sword", "hunters_recurve", "dwarven_plate", "runed_shield",
                 "mithril_hauberk", "delvers_gloves", "delvers_cap", "delvers_leggings",
                 "dwarven_mail_gloves", "delvers_jerkin", "dwarven_greathelm", "runeforged_sabatons"],
    },
    "tamsin": {
        "name": "Tamsin Runecutter", "keywords": ["tamsin", "runecutter", "carver"],
        "desc": "A white-bearded old dwarf with a jeweller's loupe screwed into one eye and stone dust in every wrinkle.",
        "greeting": "'Runes, friend. Cut deep and cut true, they'll outlast the mountain. Type LIST to see "
                    "what I've carved.'",
        "shop": ["runestone_ring", "runecarved_staff", "runecutter_gloves", "deepwool_robe",
                 "starsilk_hood", "wand_of_embers", "rune_amulet", "runecutter_boots",
                 "tome_of_warding", "runed_codex"],
    },
    "gilda": {
        "name": "Gilda Barrelbrew", "keywords": ["gilda", "barrelbrew", "brewer", "alewife"],
        "desc": "A round, rosy dwarf with a towel over her shoulder, who brews the hold's ale and, in the back, its potions.",
        "greeting": "'Sit, sit! Ale's dark, fire's warm, and the beds are carved right into the rock. Potions "
                    "are behind the bar, type LIST.'",
        "shop": ["minor_healing_potion", "minor_mana_potion", "healing_potion", "mana_potion",
                 "greater_healing_potion", "greater_mana_potion"],
    },
    "hargrim": {
        "name": "Thane Hargrim Stonebrow", "keywords": ["hargrim", "stonebrow", "thane", "king"],
        "desc": "An old dwarf in a coat of gilded mail, his white beard tucked into a belt of gold links. "
                "He looks like he has not slept in a month.",
        "greeting": "'Hearthdeep welcomes you, stranger. We have had few enough visitors since the mines went dark.'",
        "quests": ["stonewake"],
    },
    # ------------------------------------------------------------------- Silverbough
    "saelwyn": {
        "name": "Speaker Saelwyn Dawnleaf", "keywords": ["saelwyn", "dawnleaf", "speaker"],
        "desc": "A tall elf of great age, though only her eyes show it, in a robe the green of new leaves. "
                "A circlet of living silver twigs rests on her brow.",
        "greeting": "'Be welcome under the boughs, child of the short-lived. Few of your kind find their way here.'",
        "quests": ["heart_of_blight"],
    },
    "faelan": {
        "name": "Warden-Captain Faelan Thornbow", "keywords": ["faelan", "thornbow", "warden", "captain"],
        "desc": "A lean elf in mottled green leathers, a longbow over his shoulder and a fresh scar across his jaw.",
        "greeting": "'The wardens hold the Thornward Gate. Every month we hold it a little closer to home.'",
        "quests": ["stag_antlers", "rotwood_druids"],
    },
    "ilyra": {
        "name": "Ilyra Leafsong", "keywords": ["ilyra", "leafsong", "smith", "bladesmith"],
        "desc": "A silver-haired elven smith who hums as she works, her hands scarred white from a century at the forge.",
        "greeting": "'Steel sung into shape holds its edge for a thousand years. Type LIST to see my work.'",
        "shop": ["elven_saber", "elven_mail", "silverleaf_bow", "leafsteel_helm", "wardens_boots",
                 "silverbark_shield", "elven_glaive", "wardens_gauntlets", "leafsteel_greaves",
                 "wardens_hood", "wardens_leggings", "leafsteel_gauntlets", "leafsteel_boots",
                 "wardens_jerkin"],
    },
    "caelum": {
        "name": "Master Caelum Moonweave", "keywords": ["caelum", "moonweave", "weaver", "master"],
        "desc": "A soft-spoken elf with ink-black hair and silver thread wound around his fingers like rings.",
        "greeting": "'Moonlight, spun fine and woven tight, turns a blade better than you would think. Type LIST.'",
        "shop": ["moonweave_robe", "dawnwood_staff", "moonweave_gloves", "starleaf_circlet",
                 "moonweave_leggings", "silverleaf_pendant", "moonweave_slippers", "moonstone_ring",
                 "moonlit_orb"],
    },
    "merewyn": {
        "name": "Merewyn of the Silverleaf", "keywords": ["merewyn", "innkeeper", "host"],
        "desc": "A cheerful elf with flour on her sleeves and a sprig of rosemary tucked behind one pointed ear.",
        "greeting": "'Rest, eat, and if the wardens have sent you south, take a potion or two. Type LIST.'",
        "shop": ["healing_potion", "mana_potion", "greater_healing_potion", "greater_mana_potion"],
    },
    # ------------------------------------------------------------------- Dustway
    "marta": {
        "name": "Old Marta", "keywords": ["marta", "keeper", "waystation"],
        "desc": "A leathery old woman in a dusty coat with a loaded crossbow resting across her knees. "
                "She has kept this waystation for forty years and buried two husbands behind it.",
        "greeting": "'Last roof before the Badlands. Pay for your water, mind your manners, and don't feed the hyenas.'",
        "quests": ["dust_highwaymen", "yellowtooth"],
    },
    # ------------------------------------------------------------------- Sunspire
    "zahrin": {
        "name": "Emira Zahrin of Sunspire", "keywords": ["zahrin", "emira", "ruler", "queen"],
        "desc": "A woman of middle years in robes of white and gold, with a sun-disc on her brow and the "
                "steady eyes of someone who has ruled a city in the desert for twenty years.",
        "greeting": "'Sunspire welcomes every traveller who comes in peace and pays the gate tax.'",
        "quests": ["sand_king"],
    },
    "idrisa": {
        "name": "Sun-Captain Idrisa", "keywords": ["idrisa", "captain", "guard"],
        "desc": "A tall, scarred woman in golden scale, a crescent greatsword across her back and sand in every crease of her face.",
        "greeting": "'The Sun Guard holds the walls. What's beyond them is everyone's problem.'",
        "quests": ["sand_giants"],
    },
    "mehrun": {
        "name": "Archivist Mehrun", "keywords": ["mehrun", "archivist", "scholar"],
        "desc": "A thin, stooped man with ink on his nose and spectacles pushed up into his white hair.",
        "greeting": "'Every grain of sand out there was once a mountain, or a city. I write down which.'",
        "quests": ["desert_glass"],
    },
    "zahir": {
        "name": "Zahir the Bladewright", "keywords": ["zahir", "bladewright", "smith"],
        "desc": "A broad, bald smith with a beard braided with gold wire, whose sunsteel is famous from here to the sea.",
        "greeting": "'Sunsteel, folded a thousand times, quenched in the oasis at dawn. Type LIST.'",
        "shop": ["sunsteel_scimitar", "dune_recurve", "sunsteel_mail", "sunsteel_helm",
                 "sunsteel_greaves", "sand_strider_boots", "sunsteel_gauntlets", "sunburst_shield",
                 "crescent_greatsword", "sandrunner_hood", "sandrunner_leggings",
                 "sandrunner_jerkin", "sandrunner_gloves", "sunsteel_boots", "sunsteel_warhelm",
                 "sunsteel_sabatons", "sunsteel_breastplate"],
    },
    "amsa": {
        "name": "Amsa Silkwind", "keywords": ["amsa", "silkwind", "enchanter", "merchant"],
        "desc": "A small, bright-eyed old woman sitting cross-legged on a heap of silks, a hookah bubbling beside her.",
        "greeting": "'Silk for the wise, child, and gold for the old woman. Type LIST.'",
        "shop": ["desert_silk_robe", "silkwind_turban", "oasis_pearl_ring", "sunfire_staff",
                 "silkwind_gloves", "silkwind_trousers", "obelisk_amulet", "silkwind_slippers",
                 "sunstone_ring", "sunlit_codex"],
    },
    "nadim": {
        "name": "Nadim the Caravan-Master", "keywords": ["nadim", "caravan", "master", "host"],
        "desc": "A cheerful, round man in a striped robe who has crossed the desert more times than he can count.",
        "greeting": "'Water, a bed, and a potion for the road! The desert takes the unprepared. Type LIST.'",
        "shop": ["healing_potion", "mana_potion", "greater_healing_potion", "greater_mana_potion",
                 "supreme_healing_potion", "supreme_mana_potion"],
    },
    # ------------------------------------------------------------------- Planes of the Gods
    "herald": {
        "name": "the Herald of the Gods", "keywords": ["herald", "messenger"],
        "desc": "A tall figure in white with folded wings of gold and a face too calm to read.",
        "greeting": "'Welcome, mortal, to the Threshold. Beyond these gates lie the realms of the gods "
                    "who serve Lord Zek. Four trials open around us: the Sky to the north, "
                    "the Wild to the west, the Dread to the east, and to the south the gods' own prison, "
                    "where Stalworth Lightbearer keeps the law. Beyond each lies one of the four "
                    "elements: Air beyond the Sky, Earth beyond the Wild, Fire beyond the Dread, and "
                    "Water beyond the prison. When the four elemental lords have fallen to you, the "
                    "Door of Time above us will open. And before the throne of Zek may stand "
                    "only one who has walked every path to its end. Go carefully. These realms were "
                    "not made for those who have lived only once.'",
    },
}
