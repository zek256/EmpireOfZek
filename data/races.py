"""Playable races. Stats are the starting values before class modifiers.

Perks (all optional, default neutral):
  xp_mult    - multiplier on experience earned
  hp_mult    - multiplier on maximum hit points
  mana_mult  - multiplier on maximum mana
  dmg_mult   - multiplier on all outgoing damage
  crit       - flat bonus to critical strike chance
  dodge      - flat bonus to dodge chance
  regen_mult - multiplier on out-of-combat regeneration (trolls also regenerate in combat)
  immune     - damage elements this race ignores from damage-over-time effects
"""

RACES = {
    "human": {
        "name": "Human",
        "stats": {"STR": 10, "DEX": 10, "CON": 10, "INT": 10, "WIS": 10, "CHA": 12},
        "perks": {"xp_mult": 1.10},
        "perk_text": "Adaptable: +10% experience from all sources.",
        "desc": "The scattered kingdoms of Men are young, restless and ambitious. "
                "What humans lack in gifts they make up for in sheer determination.",
    },
    "high elf": {
        "name": "High Elf",
        "stats": {"STR": 8, "DEX": 11, "CON": 8, "INT": 13, "WIS": 13, "CHA": 12},
        "perks": {"mana_mult": 1.12},
        "perk_text": "Starborn: +12% maximum mana.",
        "desc": "Proud scions of the Silver Spire, the high elves remember the first "
                "dawn and the songs that were sung beneath it. Magic is their birthright.",
    },
    "elf": {
        "name": "Elf",
        "stats": {"STR": 9, "DEX": 13, "CON": 9, "INT": 11, "WIS": 11, "CHA": 10},
        "perks": {"dodge": 0.04, "crit": 0.02},
        "perk_text": "Fleetfoot: +4% dodge and +2% critical strike chance.",
        "desc": "The wood elves dwell beneath the green roof of the deep forests, swift "
                "as deer and patient as old oaks.",
    },
    "dark elf": {
        "name": "Dark Elf",
        "stats": {"STR": 9, "DEX": 12, "CON": 9, "INT": 13, "WIS": 10, "CHA": 9},
        "perks": {"crit": 0.05},
        "perk_text": "Cruel Precision: +5% critical strike chance.",
        "desc": "From the lightless cities of the Underdeep come the dark elves, "
                "cunning, ruthless, and wreathed in whispered sorceries.",
    },
    "gnome": {
        "name": "Gnome",
        "stats": {"STR": 7, "DEX": 12, "CON": 9, "INT": 14, "WIS": 10, "CHA": 10},
        "perks": {"mana_mult": 1.06, "dodge": 0.03},
        "perk_text": "Tinkerer's Wit: +6% maximum mana and +3% dodge.",
        "desc": "Small, clever and endlessly curious, gnomes delight in clockwork, "
                "riddles and any spell that goes 'bang'.",
    },
    "ogre": {
        "name": "Ogre",
        "stats": {"STR": 15, "DEX": 7, "CON": 15, "INT": 6, "WIS": 8, "CHA": 7},
        "perks": {"hp_mult": 1.12},
        "perk_text": "Thick Hide: +12% maximum hit points.",
        "desc": "Towering and slow of speech, ogres are mountains of muscle. Few things "
                "in the world can stand against an ogre's charge.",
    },
    "troll": {
        "name": "Troll",
        "stats": {"STR": 14, "DEX": 9, "CON": 14, "INT": 6, "WIS": 7, "CHA": 6},
        "perks": {"regen_mult": 2.0},
        "perk_text": "Regeneration: double out-of-combat regeneration, and slow healing during combat.",
        "desc": "Green-skinned and long of tusk, swamp trolls knit their wounds closed "
                "almost as quickly as they are dealt.",
    },
    "undead": {
        "name": "Undead",
        "stats": {"STR": 10, "DEX": 9, "CON": 11, "INT": 11, "WIS": 10, "CHA": 5},
        "perks": {"immune": ["poison", "disease"]},
        "perk_text": "Deathless: immune to poison and disease damage-over-time.",
        "desc": "Risen from the grave yet free of any master's will, the Forsaken walk "
                "the world in search of purpose, or vengeance.",
    },
    "orc": {
        "name": "Orc",
        "stats": {"STR": 13, "DEX": 10, "CON": 13, "INT": 7, "WIS": 8, "CHA": 7},
        "perks": {"dmg_mult": 1.06},
        "perk_text": "Bloodfury: +6% damage dealt.",
        "desc": "Born to the war-drums of the Ironspine clans, orcs prize strength, "
                "honour and a good fight above all else.",
    },
}

RACE_ORDER = ["human", "high elf", "elf", "dark elf", "gnome", "ogre", "troll", "undead", "orc"]
