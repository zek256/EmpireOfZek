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
}
