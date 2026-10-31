"""Quests. Talk to the giver to accept; talk again once the objective is met to turn in.

type "kill"    - slay `count` of monster `target`
type "collect" - bring `count` of item `target` (removed on turn-in)
"""

QUESTS = {
    "cellar_rats": {
        "name": "Vermin in the Cellar", "giver": "bram", "type": "kill", "target": "giant_rat", "count": 6,
        "min_level": 1, "prereq": None,
        "offer": "'Ah, an adventurer! Just what I need. Rats, see, giant ones, big as hounds, have gotten "
                 "into my cellar and they're eating me out of house and home. Clear out six of the brutes "
                 "and I'll make it worth your while. The trapdoor's just behind the bar - go DOWN.'",
        "progress": "'Still hear them squeaking down there... ({n}/{count} rats slain)'",
        "complete": "'Ha! The cellar's quiet at last! Here, take these, and drinks are on the house.'",
        "reward": {"xp": 160, "gold": 25, "items": ["minor_healing_potion", "minor_healing_potion", "minor_mana_potion"]},
    },
    "wolf_pelts": {
        "name": "Wolves at the Gate", "giver": "halvard", "type": "collect", "target": "wolf_pelt", "count": 4,
        "min_level": 3, "prereq": None,
        "offer": "'Wolves from the Whispering Woods have been taking sheep from the southern farms. "
                 "My men are stretched thin. Bring me four grey wolf pelts as proof you've thinned the "
                 "pack. The woods lie south of town, past Willowbrook Crossing.'",
        "progress": "'Four pelts, that's the bargain. You have {n}.'",
        "complete": "'Good, thick pelts. The farmers will sleep easier. Take these gloves - they served me well.'",
        "reward": {"xp": 550, "gold": 60, "items": ["studded_gloves", "healing_potion"]},
    },
    "bandit_chief": {
        "name": "The Bandit Chieftain", "giver": "halvard", "type": "kill", "target": "bandit_chieftain", "count": 1,
        "min_level": 6, "prereq": "wolf_pelts",
        "offer": "'You've proven yourself. Now for the real trouble: a brute called Rask has gathered a "
                 "gang of cutthroats in a palisade camp deep in the Whispering Woods. They've been "
                 "robbing every caravan on the south road. End him.'",
        "progress": "'Rask still breathes. His camp lies at the far southern end of the deep woods.'",
        "complete": "'Rask is dead? By the Dawn! You've done this town a great service. Take this mail "
                    "from the armoury - and my thanks.'",
        "reward": {"xp": 2200, "gold": 200, "items": ["chain_shirt", "healing_potion", "healing_potion"]},
    },
    "bone_king": {
        "name": "The Bone King", "giver": "aveline", "type": "kill", "target": "varnoth", "count": 1,
        "min_level": 10, "prereq": None,
        "offer": "'A great evil has woken beneath Barrowfield, east of the King's Road. Varnoth, a "
                 "lich who was buried there a thousand years ago, is raising the dead. His cult grows "
                 "bolder every night. Descend into his crypt beneath the ruined chapel and destroy him. "
                 "The light goes with you.'",
        "progress": "'The dead still walk at Barrowfield. Varnoth must be destroyed.'",
        "complete": "'I felt it - the darkness beneath Barrowfield has lifted! Wear this amulet, blessed "
                    "at the altar of the Dawn. You are truly a champion of the light.'",
        "reward": {"xp": 9000, "gold": 500, "items": ["amulet_of_the_dawn", "healing_potion", "mana_potion"]},
    },
    "bog_hag": {
        "name": "The Hag of the Mirefen", "giver": "aveline", "type": "kill", "target": "bog_hag", "count": 1,
        "min_level": 17, "prereq": "bone_king",
        "offer": "'There is another evil I must ask you to face. Children have been vanishing from the "
                 "villages near the Mirefen, west of the crossroads. The lizardfolk whisper of a hag "
                 "called Old Mother Gristle who lives deep in the swamp. Find her. Put an end to it.'",
        "progress": "'Old Mother Gristle still haunts the Mirefen. Her hut lies past the serpent pools.'",
        "complete": "'The children have come home! Bless you. The temple's coffers are yours to share.'",
        "reward": {"xp": 30000, "gold": 1200, "items": ["greater_healing_potion", "greater_healing_potion", "greater_mana_potion"]},
    },
    "frost_goblins": {
        "name": "Trouble in the Rimefells", "giver": "halvard", "type": "kill", "target": "frost_goblin", "count": 8,
        "min_level": 11, "prereq": None,
        "offer": "'A rider came down from the dwarves of Hearthdeep. Frost goblins are raiding their road "
                 "and the Thane has asked Brightwater for help. Head out the West Gate, through the "
                 "Westmarch and north past the old watchtower into the Rimefells. Kill eight of the "
                 "little devils, and make yourself known to the dwarves while you're there.'",
        "progress": "'The dwarves still count goblin raids. ({n}/{count} frost goblins slain)'",
        "complete": "'The Thane sends his thanks, and so do I. Take this dwarven mail, it came down with "
                    "the rider.'",
        "reward": {"xp": 6000, "gold": 200, "items": ["dwarven_chainmail", "healing_potion", "healing_potion"]},
    },
    "orc_warlord": {
        "name": "The Skullsplitter Horde", "giver": "halvard", "type": "kill", "target": "warlord_gorrak", "count": 1,
        "min_level": 25, "prereq": "bandit_chief",
        "offer": "'Scouts report an orc horde massing in the Ironspine, under a warlord called Gorrak "
                 "Skullsplitter. If he marches south, Brightwater will burn. Strike first. Find his "
                 "warcamp east of Ironspine Pass and bring him down.'",
        "progress": "'The war-drums still sound in the mountains. Gorrak lives.'",
        "complete": "'Gorrak is slain and the horde is scattering! The King himself will hear of this.'",
        "reward": {"xp": 90000, "gold": 3000, "items": ["greater_healing_potion", "greater_healing_potion", "tower_shield"]},
    },

    # ------------------------------------------------------------------ Westmarch
    "goblin_raiders": {
        "name": "Goblins in the Henhouse", "giver": "haverick", "type": "kill", "target": "hill_goblin", "count": 6,
        "min_level": 5, "prereq": None,
        "offer": "'Goblins! Out of the old quarry, every night, stealing hens, pigs, washing off the line, "
                 "my second-best boots. I've had enough. Go up to the quarry west of here and thin them "
                 "out, six of the hill goblins at least, and I'll see you right.'",
        "progress": "'Still hearing them up at the quarry of a night. ({n}/{count} hill goblins slain)'",
        "complete": "'Quiet as a churchyard last night! Here, take this helm, my grandad wore it at the "
                    "Battle of the Ford and never needed it once.'",
        "reward": {"xp": 1500, "gold": 60, "items": ["iron_helm", "healing_potion"]},
    },

    "salt_wraiths": {
        "name": "The Thirsting Dead", "giver": "aveline", "type": "kill", "target": "salt_wraith", "count": 8,
        "min_level": 36, "prereq": None,
        "offer": "'A plea has reached the temple from the Emira of Sunspire, the golden city beyond the "
                 "Badlands. The dead are rising on the salt flats north of her city's western oasis, "
                 "and her people dare not fetch water. Take the Dustway east from the East Gate, cross "
                 "the Badlands, and lay eight of the salt wraiths to rest.'",
        "progress": "'The dead still thirst on the salt flats. ({n}/{count} salt wraiths laid to rest)'",
        "complete": "'The Emira has written to thank the temple, and you. Take this from our treasury, "
                    "and go to Sunspire again; I think they have need of you still.'",
        "reward": {"xp": 30000, "gold": 1500, "items": ["obelisk_amulet", "supreme_healing_potion"]},
    },
    "blight_spreads": {
        "name": "The Blight Spreads", "giver": "elowen", "type": "kill", "target": "blighted_treant", "count": 6,
        "min_level": 24, "prereq": None,
        "offer": "'A letter came from my kin in Silverbough, the elven city deep in the Eldergrove. A blight "
                 "is eating the forest from the south, and the trees themselves walk now, rotten and "
                 "angry. Go south past the Dire Wolf Den and take the Old South Way. Fell six of the "
                 "blighted treants, and tell the Speaker that Elowen sent you.'",
        "progress": "'The grove still sickens. ({n}/{count} blighted treants felled)'",
        "complete": "'My sister writes that the wardens speak of you already. Take this, woven in "
                    "Silverbough, and go back to them. They need you more than I do.'",
        "reward": {"xp": 15000, "gold": 400, "items": ["silverleaf_pendant", "greater_healing_potion"]},
    },

    # ------------------------------------------------------------------ Hearthdeep
    "yeti_menace": {
        "name": "Fur for the Gatewatch", "giver": "orla", "type": "collect", "target": "yeti_fur", "count": 6,
        "min_level": 15, "prereq": None,
        "offer": "'Yetis have come down out of the high caves, bold as you like, and my sentries are "
                 "freezing at their posts. Two birds, one axe: go north of the Rimewood to the yeti caves "
                 "and bring me six hanks of yeti fur. We'll line the sentries' cloaks with it.'",
        "progress": "'Six hanks, and the Gatewatch will stop complaining. You have {n}.'",
        "complete": "'Ha! Good thick fur. My sentries will sing your name, badly. Take these boots, "
                    "they'll keep your feet on the rock.'",
        "reward": {"xp": 12000, "gold": 350, "items": ["dwarven_boots", "healing_potion", "healing_potion"]},
    },
    "stonewake": {
        "name": "The Stonewake", "giver": "hargrim", "type": "kill", "target": "ghaldrek", "count": 1,
        "min_level": 18, "prereq": None,
        "offer": "'Our miners dug too deep in Deepdelve. They broke into a vault no dwarf ever cut, and "
                 "something woke. The miners came back grey and silent and went down again, and none "
                 "have come up since. The old songs call it the Stonewake. Take the lift down, find what "
                 "they woke, and put it back to sleep. Forever.'",
        "progress": "'The mountain still groans in the night. The Stonewake lives.'",
        "complete": "'The groaning has stopped. By my beard, you did it. The lost miners can rest now, "
                    "and Hearthdeep owes you a debt. Take these greaves from my own armoury.'",
        "reward": {"xp": 25000, "gold": 1000, "items": ["dwarven_greaves", "greater_healing_potion",
                                                        "greater_healing_potion"]},
    },

    # ------------------------------------------------------------------ Silverbough
    "stag_antlers": {
        "name": "The Sacred Herd", "giver": "faelan", "type": "collect", "target": "stag_antler", "count": 5,
        "min_level": 24, "prereq": None,
        "offer": "'The blight is creeping into the greatstags. Once it takes them, they turn on the herd. "
                 "The Speaker has given leave to cull the sick ones before it spreads. Bring me five "
                 "antlers from the stags of the Stag Walk or the Whitestag Glade. It is a sad duty, but "
                 "a necessary one.'",
        "progress": "'Five antlers, and the herd may yet survive. You have {n}.'",
        "complete": "'It is done, then. The herd will remember, even if we would rather forget. Take "
                    "these boots, and walk the grove as a warden does.'",
        "reward": {"xp": 15000, "gold": 400, "items": ["wardens_boots", "greater_healing_potion"]},
    },
    "rotwood_druids": {
        "name": "The Rotwood Circle", "giver": "faelan", "type": "kill", "target": "rotwood_druid", "count": 8,
        "min_level": 27, "prereq": "stag_antlers",
        "offer": "'The blight does not spread on its own. Druids who have given themselves to it are "
                 "tending it, feeding it, singing the treants awake. They gather at the Druids' Ring, "
                 "the Fungal Barrows and beyond the Thornward Gate. Kill eight of them.'",
        "progress": "'The rotwood circle still sings. ({n}/{count} rotwood druids slain)'",
        "complete": "'Eight fewer voices singing the rot. The grove is quieter. Take these gauntlets, "
                    "the wardens' own.'",
        "reward": {"xp": 25000, "gold": 800, "items": ["wardens_gauntlets", "greater_healing_potion",
                                                       "greater_healing_potion"]},
    },
    "heart_of_blight": {
        "name": "The Heart of the Blight", "giver": "saelwyn", "type": "kill", "target": "rotheart", "count": 1,
        "min_level": 30, "prereq": None,
        "offer": "'The blight has a heart. It is Rotheart, the oldest tree in the world, who sheltered "
                 "our people when Elandor fell. Something has poisoned him, and his rot flows out through "
                 "every root in the grove. It grieves me past words to ask it. Go through the Thornward "
                 "Gate, past the Gloaming Mere, and end him.'",
        "progress": "'Rotheart still burns at the heart of the blight. The grove is dying.'",
        "complete": "'I felt him go. The green is already coming back into the leaves. You have saved "
                    "the Eldergrove, and Silverbough will not forget your name while a single tree stands.'",
        "reward": {"xp": 70000, "gold": 2500, "items": ["moonstone_ring", "greater_healing_potion",
                                                        "greater_healing_potion"]},
    },

    # ------------------------------------------------------------------ Dustway
    "dust_highwaymen": {
        "name": "Highway Robbery", "giver": "marta", "type": "kill", "target": "highwayman", "count": 6,
        "min_level": 9, "prereq": None,
        "offer": "'Highwaymen on Gallows Hill, bold as brass, robbing every cart that comes through the "
                 "Dry Ford. My guests stop coming, I stop eating. Kill six of them and I'll pay you "
                 "out of what they'd have taken.'",
        "progress": "'Still masks on Gallows Hill. ({n}/{count} highwaymen dealt with)'",
        "complete": "'Ha! The carters are singing again. Here's your pay, and a little something from "
                    "under the bar.'",
        "reward": {"xp": 3500, "gold": 150, "items": ["chain_leggings", "healing_potion"]},
    },
    "yellowtooth": {
        "name": "The Laughing Warlord", "giver": "marta", "type": "kill", "target": "yellowtooth", "count": 1,
        "min_level": 23, "prereq": "dust_highwaymen",
        "offer": "'The gnolls of the Badlands have a warlord now, a grey old monster called Yellowtooth. "
                 "Since he took the pack, they don't just scavenge, they raid. Three caravans this "
                 "season, every soul eaten. His den's at the far end of the canyons, past the Howling "
                 "Pit. Bring him down.'",
        "progress": "'You can hear him laughing on the wind some nights. Yellowtooth lives.'",
        "complete": "'Dead? Truly? Forty years I've kept this house, and that's the best news I've had "
                    "in all of them. The caravans will come back. Take all of this, you've earned it.'",
        "reward": {"xp": 35000, "gold": 1500, "items": ["greater_healing_potion", "greater_healing_potion",
                                                        "runed_shield"]},
    },

    # ------------------------------------------------------------------ Sunspire
    "desert_glass": {
        "name": "Glass from the Sands", "giver": "mehrun", "type": "collect", "target": "desert_glass", "count": 5,
        "min_level": 40, "prereq": None,
        "offer": "'Desert glass! The sand was melted by something, long ago, and I believe the glass "
                 "remembers what. Bring me five shards. The scorpions of the Glass Waste swallow it, "
                 "the mirage-cats roll in it, and the salt wraiths clutch it like coins. Five shards, "
                 "and I will pay well.'",
        "progress": "'Five shards, please. You have {n}.'",
        "complete": "'Look at the colour! There was fire here once like nothing on this earth. You have "
                    "done the archive a great service. Take this ring, it was found in these sands.'",
        "reward": {"xp": 35000, "gold": 1500, "items": ["sunstone_ring", "supreme_mana_potion"]},
    },
    "sand_giants": {
        "name": "Giants on the Causeway", "giver": "idrisa", "type": "kill", "target": "sand_giant", "count": 6,
        "min_level": 44, "prereq": None,
        "offer": "'The sand giants of the Causeway have started raiding the northern caravans, and they "
                 "throw pillars at my patrols like children throwing stones. Go out the North Gate, west "
                 "to the Giants' Causeway and the Valley of the Kings, and kill six of them.'",
        "progress": "'The giants still hold the Causeway. ({n}/{count} sand giants slain)'",
        "complete": "'Six giants! The Sun Guard will drink to you tonight. Take this blade, the Guard's "
                    "own pattern.'",
        "reward": {"xp": 45000, "gold": 2000, "items": ["crescent_greatsword", "supreme_healing_potion",
                                                        "supreme_healing_potion"]},
    },
    "sand_king": {
        "name": "The Last Sand King", "giver": "zahrin", "type": "kill", "target": "ussreth", "count": 1,
        "min_level": 45, "prereq": None,
        "offer": "'Three thousand years ago, the Sand Kings ruled all of this desert, and the last of them "
                 "was buried in a black pyramid north of here with ten thousand slaves. Robbers broke "
                 "his seal last spring. Now the dead walk, the scarabs swarm, and my people sicken. The "
                 "pyramid lies beyond the Valley of the Kings. Go down into the tomb, and give Ussreth "
                 "the rest he will not take.'",
        "progress": "'The sickness spreads. Ussreth still walks in his tomb.'",
        "complete": "'The sickness is lifting already. Sunspire owes you its life. Whatever you need "
                    "in this city, it is yours, and your name will be cut into the Obelisk.'",
        "reward": {"xp": 150000, "gold": 5000, "items": ["supreme_healing_potion", "supreme_healing_potion",
                                                         "supreme_mana_potion"]},
    },
}
