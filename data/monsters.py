"""Monster templates.

Base statistics are derived from level in world.MonsterInstance; the per-monster
multipliers (hp, dmg, armor, xp, gold) adjust that baseline.

specials: special attacks used with `chance` each round instead of a basic attack.
  big    - a heavy blow dealing `mult` x normal damage
  dot    - damage-over-time on the player (`mult` x normal damage per round for `turns`)
  stun   - stuns the player for `turns` rounds
  drain  - damage that heals the monster
  heal   - heals the monster for `mult` x its max hp
"""

MONSTERS = {}


def M(mid, name, level, desc, hp=1.0, dmg=1.0, armor=1.0, aggro=False, specials=None,
      loot=None, xp=1.0, gold=1.0, boss=False, element="physical"):
    MONSTERS[mid] = {
        "id": mid, "name": name, "level": level, "desc": desc, "hp": hp, "dmg": dmg,
        "armor": armor, "aggro": aggro, "specials": specials or [], "loot": loot or [],
        "xp": xp, "gold": gold, "boss": boss, "element": element,
    }


def big(name, chance, mult, msg):
    return {"type": "big", "name": name, "chance": chance, "mult": mult, "msg": msg}


def dot(name, chance, mult, turns, element, msg):
    return {"type": "dot", "name": name, "chance": chance, "mult": mult, "turns": turns,
            "element": element, "msg": msg}


def stun(name, chance, turns, msg):
    return {"type": "stun", "name": name, "chance": chance, "turns": turns, "msg": msg}


def drain(name, chance, mult, msg):
    return {"type": "drain", "name": name, "chance": chance, "mult": mult, "msg": msg}


def heal(name, chance, mult, msg):
    return {"type": "heal", "name": name, "chance": chance, "mult": mult, "msg": msg}


# ------------------------------------------------------------- Cellar & Meadow (1-5)
M("giant_rat", "a giant rat", 1, "A rat the size of a small dog, with yellow teeth and a hairless tail.",
  hp=0.6, dmg=0.7, loot=[("rat_tail", 0.5)], gold=0.3)
M("cellar_spider", "a bloated cellar spider", 2, "A pale, bloated spider that drops from the rafters.",
  hp=0.7, dmg=0.8, specials=[dot("Venomous Bite", 0.2, 0.3, 3, "poison", "sinks its fangs into you!")],
  loot=[("spider_silk", 0.3)], gold=0.3)
M("field_snake", "a field adder", 2, "A brown-and-gold adder coiled in the tall grass.",
  hp=0.7, dmg=0.8, specials=[dot("Venom", 0.25, 0.3, 3, "poison", "strikes, and venom burns in your veins!")])
M("wild_boar", "a wild boar", 3, "A bristling boar with wicked curved tusks and a foul temper.",
  hp=1.0, dmg=0.9, specials=[big("Gore", 0.2, 1.6, "lowers its head and gores you!")], gold=0.2)
M("kobold_scavenger", "a kobold scavenger", 3, "A yapping, dog-faced kobold clutching a rusty knife.",
  hp=0.9, dmg=0.9, loot=[("leather_gloves", 0.08), ("leather_leggings", 0.08)], gold=1.2)
M("kobold_trapper", "a kobold trapper", 4, "A wiry kobold draped in snares and smelling of wet dog.",
  hp=0.9, dmg=1.0, aggro=True, specials=[stun("Net Toss", 0.15, 1, "hurls a weighted net over you!")],
  loot=[("leather_jerkin", 0.08), ("iron_buckler", 0.06)], gold=1.3)

# ------------------------------------------------------------- Whispering Woods (4-10)
M("grey_wolf", "a grey wolf", 4, "A lean grey wolf with hungry amber eyes.",
  hp=0.9, dmg=1.0, loot=[("wolf_pelt", 0.65)], gold=0.2)
M("giant_spider", "a giant forest spider", 5, "A hairy black spider as large as a pony, its fangs dripping.",
  hp=1.0, dmg=1.0, aggro=True, specials=[dot("Venomous Bite", 0.25, 0.35, 3, "poison", "sinks its dripping fangs into you!")],
  loot=[("spider_silk", 0.6)], gold=0.3)
M("dire_wolf", "a dire wolf", 7, "A massive black wolf, its shoulders as high as a man's chest.",
  hp=1.1, dmg=1.1, aggro=True, specials=[big("Savage Maul", 0.2, 1.7, "seizes you in its jaws and shakes you savagely!")],
  loot=[("wolf_pelt", 0.5), ("wolfhide_boots", 0.06)], gold=0.3)
M("bandit_scout", "a bandit scout", 6, "A hooded bandit with a short bow and a shifty gaze.",
  hp=0.9, dmg=1.0, loot=[("steel_dagger", 0.06), ("wolfhide_boots", 0.06), ("studded_gloves", 0.06)], gold=1.5)
M("bandit_cutthroat", "a bandit cutthroat", 8, "A scarred brigand in mismatched leathers, twin knives in hand.",
  hp=1.0, dmg=1.1, aggro=True, specials=[dot("Bleeding Cut", 0.2, 0.35, 3, "bleed", "opens a deep, bleeding gash across your arm!")],
  loot=[("iron_longsword", 0.05), ("iron_helm", 0.05), ("chain_shirt", 0.04)], gold=1.6)
M("bandit_archer", "a bandit archer", 8, "A bandit perched behind a barricade, arrow nocked.",
  hp=0.9, dmg=1.15, aggro=True, loot=[("yew_longbow", 0.06), ("iron_helm", 0.05)], gold=1.6)
M("bandit_chieftain", "Rask the Bandit Chieftain", 10,
  "A towering, one-eyed brute in a stolen noble's coat, his cutlass dark with old blood.",
  hp=2.4, dmg=1.15, armor=1.3, aggro=True, boss=True, xp=4.0, gold=4.0,
  specials=[big("Brutal Slash", 0.25, 1.8, "swings his cutlass in a brutal, two-handed slash!"),
            stun("Pommel Strike", 0.12, 1, "cracks you across the skull with his pommel!")],
  loot=[("bandit_cutlass", 1.0), ("chain_shirt", 0.5), ("ring_of_vigor", 0.4)])

# ------------------------------------------------------------- Barrowfield & Crypt (9-17)
M("restless_zombie", "a restless zombie", 9, "A shambling corpse in a rotted burial shroud, moaning softly.",
  hp=1.2, dmg=0.95, aggro=True, specials=[dot("Grave Rot", 0.2, 0.3, 4, "disease", "claws you with filthy, rotting nails!")],
  loot=[("bone_dust", 0.3)], gold=0.8)
M("carrion_ghoul", "a carrion ghoul", 10, "A grey-skinned ghoul crouched over an opened grave, its claws long and black.",
  hp=1.0, dmg=1.1, specials=[stun("Paralysing Claw", 0.15, 1, "rakes you with paralysing claws!")],
  loot=[("bone_dust", 0.4), ("chain_leggings", 0.05)], gold=1.0)
M("crypt_bat", "a swarm of crypt bats", 11, "A shrieking cloud of red-eyed bats.",
  hp=0.7, dmg=0.9, aggro=True, gold=0.2)
M("skeleton_warrior", "a skeleton warrior", 12, "A skeleton in corroded mail, still clutching its ancient sword.",
  hp=1.1, dmg=1.05, armor=1.5, aggro=True, loot=[("bone_dust", 0.4), ("iron_boots", 0.05), ("bonecleaver", 0.04)], gold=1.0)
M("bone_guardian", "a bone guardian", 13, "A hulking construct of fused skeletons that guards the deeper halls.",
  hp=1.5, dmg=1.1, armor=2.0, specials=[big("Crushing Blow", 0.2, 1.7, "brings its bone-fists down upon you!")],
  loot=[("bonecleaver", 0.1), ("bone_helm", 0.1), ("bone_dust", 0.5)], gold=1.2, xp=1.3)
M("wailing_spirit", "a wailing spirit", 14, "The translucent shade of a weeping woman, drifting just above the floor.",
  hp=0.9, dmg=1.1, armor=0.5, aggro=True, specials=[drain("Life Drain", 0.25, 1.0, "passes through you, and your life drains away!")],
  loot=[("grave_shroud", 0.05)], gold=0.8)
M("crypt_cultist", "a cultist of Varnoth", 14, "A gaunt man in black robes, his face painted like a skull.",
  hp=1.0, dmg=1.05, aggro=True, specials=[heal("Dark Mending", 0.15, 0.25, "chants, and dark energy mends his wounds."),
                                          dot("Curse of Decay", 0.15, 0.35, 3, "shadow", "points at you and hisses a curse of decay!")],
  loot=[("grave_shroud", 0.08), ("healing_potion", 0.2)], gold=1.8)
M("varnoth", "Varnoth the Bone King", 17,
  "A towering lich-lord in a crown of rusted iron, green witchfire burning in his empty eye sockets.",
  hp=2.3, dmg=1.15, armor=1.6, aggro=True, boss=True, xp=5.0, gold=5.0,
  specials=[drain("Soul Rend", 0.2, 1.0, "tears at your very soul with a skeletal hand!"),
            dot("Grave Curse", 0.15, 0.4, 4, "shadow", "curses you with the chill of the grave!"),
            heal("Phylactery Pulse", 0.08, 0.15, "draws power from his hidden phylactery and his bones knit together!")],
  loot=[("varnoth_scepter", 0.6), ("grave_shroud", 0.5), ("bone_helm", 0.5), ("knights_blade", 0.4)])

# ------------------------------------------------------------- Mirefen (15-22)
M("bog_lurker", "a bog lurker", 15, "A scaly green thing that rises dripping from the black water.",
  hp=1.1, dmg=1.05, aggro=True, loot=[("mirescale_vest", 0.04), ("bog_pearl", 0.15)], gold=0.5)
M("lizardman_warrior", "a lizardman warrior", 16, "A hissing lizardman with a bone-tipped spear and a shield of turtle shell.",
  hp=1.1, dmg=1.1, armor=1.4, aggro=True, loot=[("steel_kite_shield", 0.05), ("bog_pearl", 0.15)], gold=1.4)
M("swamp_troll", "a swamp troll", 17, "A hulking, moss-covered troll whose wounds close as you watch.",
  hp=1.5, dmg=1.15, specials=[heal("Regenerate", 0.15, 0.15, "regenerates, its wounds bubbling closed!")],
  loot=[("plate_gauntlets", 0.05), ("bog_pearl", 0.2)], gold=1.3, xp=1.3)
M("will_o_wisp", "a will-o'-the-wisp", 18, "A drifting, flickering ball of pale light that hums an eerie tune.",
  hp=0.7, dmg=1.2, armor=0.3, specials=[stun("Bewitching Glow", 0.2, 1, "flares brightly, and you stand transfixed!")],
  loot=[("bog_pearl", 0.3), ("mana_potion", 0.2)], gold=0.6)
M("mire_serpent", "a mire serpent", 19, "A huge olive-green serpent, thick as a tree trunk, sliding through the reeds.",
  hp=1.3, dmg=1.15, aggro=True, specials=[dot("Venomous Fangs", 0.25, 0.4, 4, "poison", "strikes like lightning, venom searing through you!")],
  loot=[("serpentfang", 0.06), ("bogwood_staff", 0.05)], gold=0.8)
M("bog_hag", "Old Mother Gristle", 22,
  "A hunched, warty crone in a shawl of rotting moss, her eyes like lanterns and her teeth like needles.",
  hp=2.6, dmg=1.2, armor=1.3, aggro=True, boss=True, xp=5.0, gold=5.0,
  specials=[dot("Hex of Withering", 0.2, 0.45, 4, "shadow", "cackles and hurls a hex of withering at you!"),
            stun("Evil Eye", 0.12, 1, "fixes you with her evil eye, and your limbs lock!"),
            heal("Drink from the Cauldron", 0.1, 0.12, "slurps from a ladle of bubbling broth and cackles with renewed vigour!")],
  loot=[("gristles_hexrod", 0.6), ("hag_charm", 0.6), ("mirescale_vest", 0.4), ("bogwood_staff", 0.4)])

# ------------------------------------------------------------- Ironspine Mountains (20-31)
M("mountain_lion", "a mountain lion", 21, "A tawny great cat crouched on a ledge, tail twitching.",
  hp=1.0, dmg=1.15, aggro=True, specials=[dot("Rending Claws", 0.2, 0.35, 3, "bleed", "rakes you with rending claws!")], gold=0.4)
M("harpy", "a shrieking harpy", 22, "A filthy winged hag with talons of black iron.",
  hp=0.9, dmg=1.15, aggro=True, specials=[stun("Deafening Shriek", 0.15, 1, "lets loose a deafening shriek!")],
  loot=[("hunters_recurve", 0.04)], gold=1.0)
M("hill_giant", "a hill giant", 24, "A dull-eyed giant twice the height of a man, carrying a tree trunk as a club.",
  hp=1.7, dmg=1.25, specials=[big("Tree-Trunk Smash", 0.25, 1.8, "brings his tree-trunk club smashing down!")],
  loot=[("tower_shield", 0.05), ("greater_healing_potion", 0.15)], gold=1.5, xp=1.5)
M("orc_raider", "an orc raider", 24, "A grey-skinned orc in spiked leathers, hungry for loot and glory.",
  hp=1.1, dmg=1.1, aggro=True, loot=[("orc_tusk", 0.3), ("mithril_sword", 0.04), ("mithril_hauberk", 0.03)], gold=1.5)
M("orc_berserker", "an orc berserker", 26, "A foaming, tattooed orc wielding an axe in each hand.",
  hp=1.2, dmg=1.25, aggro=True, specials=[big("Frenzied Chop", 0.25, 1.7, "screams and chops at you in a frenzy!")],
  loot=[("orc_tusk", 0.3), ("orcish_greataxe", 0.06), ("orcish_helm", 0.05)], gold=1.5)
M("orc_shaman", "an orc shaman", 27, "A wizened orc draped in bones and feathers, chanting to the storm.",
  hp=1.0, dmg=1.15, aggro=True, specials=[heal("Spirit Mending", 0.15, 0.2, "chants to the spirits, and his wounds mend!"),
                                          dot("Searing Totem", 0.2, 0.4, 3, "fire", "calls down searing spirit-fire upon you!")],
  loot=[("orc_tusk", 0.3), ("greater_mana_potion", 0.2), ("frostweave_staff", 0.04)], gold=1.8)
M("orc_warbeast", "an orc warbeast", 28, "A massive armoured boar-beast ridden into battle by the orc clans.",
  hp=1.6, dmg=1.2, armor=1.5, specials=[stun("Trample", 0.15, 1, "tramples you underfoot!")],
  loot=[("orc_tusk", 0.5)], gold=0.8, xp=1.4)
M("warlord_gorrak", "Warlord Gorrak Skullsplitter", 31,
  "A mountain of scarred green muscle in blackened plate, wearing a cloak of human scalps.",
  hp=2.7, dmg=1.25, armor=1.6, aggro=True, boss=True, xp=5.0, gold=5.0,
  specials=[big("Skullsplitter", 0.25, 2.0, "brings his warhammer down in a skull-splitting overhead blow!"),
            stun("War Stomp", 0.12, 1, "stomps, and the ground shakes you off your feet!"),
            heal("Bloodlust", 0.08, 0.1, "roars with bloodlust, his wounds forgotten!")],
  loot=[("gorraks_warhammer", 0.6), ("warlord_gauntlets", 0.6), ("orcish_helm", 0.5), ("tower_shield", 0.3)])

# ------------------------------------------------------------- Frost Caverns (29-35)
M("ice_wraith", "an ice wraith", 30, "A shrieking spectre of blue frost, its touch colder than death.",
  hp=1.0, dmg=1.2, armor=0.6, aggro=True, specials=[drain("Frozen Touch", 0.25, 1.0, "passes a frozen hand through your chest!")],
  loot=[("frost_shard", 0.3), ("frost_ring", 0.03)], gold=0.8)
M("frost_troll", "a frost troll", 32, "A white-furred troll with icicles hanging from its tusks.",
  hp=1.5, dmg=1.2, specials=[heal("Regenerate", 0.15, 0.12, "regenerates, frost sealing its wounds!")],
  loot=[("frost_shard", 0.3), ("frostgiant_greaves", 0.04)], gold=1.2, xp=1.3)
M("frost_giant", "a frost giant", 34, "A blue-skinned giant in rime-crusted mail, wielding a sword of ice.",
  hp=1.8, dmg=1.3, armor=1.5, specials=[big("Glacial Cleave", 0.25, 1.8, "cleaves at you with a sword of solid ice!"),
                                        stun("Frost Nova", 0.1, 1, "exhales a blast of frost that freezes you in place!")],
  loot=[("frostbrand", 0.06), ("frostgiant_greaves", 0.08), ("frost_shard", 0.5)], gold=2.0, xp=1.7)

# ------------------------------------------------------------- Ruins of Elandor (32-41)
M("phantom_sentinel", "a phantom sentinel", 33, "The ghost of an elven guardsman, still at his post after a thousand years.",
  hp=1.1, dmg=1.2, armor=1.2, aggro=True, loot=[("elven_relic", 0.2), ("elandor_runeblade", 0.03)], gold=1.0)
M("ruin_stalker", "a ruin stalker", 34, "A sleek, six-legged predator with chitinous plates and mirror-bright eyes.",
  hp=1.2, dmg=1.25, aggro=True, specials=[dot("Barbed Tail", 0.2, 0.4, 3, "poison", "lashes you with its barbed tail!")],
  loot=[("elven_relic", 0.1)], gold=0.8)
M("spectral_mage", "a spectral mage", 36, "A translucent elven sorcerer in flowing robes, endlessly reading a book of light.",
  hp=0.9, dmg=1.3, armor=0.5, specials=[dot("Arcane Burn", 0.25, 0.45, 3, "arcane", "hurls a bolt of searing arcane fire!"),
                                        stun("Time Lock", 0.12, 1, "gestures, and time freezes around you!")],
  loot=[("elven_relic", 0.25), ("elandor_robes", 0.04), ("staff_of_stars", 0.03), ("starlight_circlet", 0.03)], gold=1.5)
M("living_statue", "a living statue", 37, "A marble statue of an elven hero that grinds slowly to life.",
  hp=2.0, dmg=1.25, armor=2.5, specials=[big("Marble Fist", 0.25, 1.8, "smashes you with a fist of solid marble!")],
  loot=[("elandor_plate", 0.05), ("elven_relic", 0.3)], gold=1.0, xp=1.6)
M("seluvar", "Seluvar the Hollow Archmage", 41,
  "An elven archmage whose body is long gone. Only robes, a crown of stars and two burning eyes remain.",
  hp=2.7, dmg=1.25, armor=1.0, aggro=True, boss=True, xp=5.0, gold=5.0,
  specials=[dot("Starfire", 0.22, 0.45, 4, "arcane", "calls down a column of starfire upon you!"),
            stun("Temporal Prison", 0.12, 1, "traps you in a prison of frozen time!"),
            drain("Hollowing", 0.15, 1.2, "hollows you out, drinking your essence!")],
  loot=[("seluvars_wand", 0.6), ("archmage_ring", 0.6), ("elandor_robes", 0.4), ("starlight_circlet", 0.4), ("elven_longbow", 0.3)])

# ------------------------------------------------------------- Ashen Peaks & Dragon's Lair (40-52)
M("fire_elemental", "a fire elemental", 41, "A roaring pillar of living flame, vaguely human in shape.",
  hp=1.1, dmg=1.25, armor=0.8, aggro=True, specials=[dot("Immolate", 0.25, 0.45, 3, "fire", "engulfs you in roaring flames!")],
  loot=[("supreme_mana_potion", 0.1)], gold=0.8)
M("salamander", "a magma salamander", 42, "A huge red lizard whose skin glows like coals.",
  hp=1.2, dmg=1.25, aggro=True, specials=[dot("Burning Bite", 0.2, 0.4, 3, "fire", "bites you with searing jaws!")],
  loot=[("drakehide_boots", 0.03)], gold=0.8)
M("ash_drake", "an ash drake", 44, "A wingless young dragon, grey as cinders, smoke curling from its nostrils.",
  hp=1.5, dmg=1.3, armor=1.5, aggro=True, specials=[big("Cinder Breath", 0.25, 1.8, "breathes a gout of burning cinders over you!")],
  loot=[("dragon_scale", 0.2), ("drakehide_boots", 0.06), ("ember_ring", 0.03)], gold=1.5, xp=1.4)
M("dragonkin_guard", "a dragonkin guard", 45, "A scaled warrior of the dragon cult, wielding an obsidian glaive.",
  hp=1.3, dmg=1.3, armor=1.8, aggro=True, loot=[("obsidian_greaves", 0.05), ("obsidian_blade", 0.04), ("sunforged_mace", 0.03)], gold=2.0)
M("obsidian_golem", "an obsidian golem", 46, "A towering construct of black volcanic glass, magma glowing in its cracks.",
  hp=2.0, dmg=1.3, armor=3.0, specials=[big("Shattering Fist", 0.25, 1.9, "smashes you with a fist of volcanic glass!")],
  loot=[("obsidian_greaves", 0.08), ("obsidian_blade", 0.06)], gold=1.5, xp=1.7)
M("flame_demon", "a flame demon", 48, "A horned demon of fire and shadow with a whip of living flame.",
  hp=1.4, dmg=1.35, armor=1.5, aggro=True, specials=[dot("Hellfire Lash", 0.25, 0.5, 3, "fire", "lashes you with a whip of hellfire!"),
                                                     stun("Terrify", 0.1, 1, "roars, and terror roots you to the spot!")],
  loot=[("ashen_crown", 0.04), ("dragonbone_staff", 0.04), ("supreme_healing_potion", 0.15)], gold=2.0, xp=1.3)
M("magma_titan", "a magma titan", 50, "A colossus of molten rock, each footstep leaving a pool of fire.",
  hp=2.2, dmg=1.35, armor=2.0, specials=[big("Eruption", 0.25, 1.9, "erupts in a fountain of molten rock!")],
  loot=[("ember_ring", 0.08), ("dragon_scale", 0.4), ("ashen_crown", 0.05)], gold=2.5, xp=1.8)
M("pyraxis", "Pyraxis the Eternal Flame", 52,
  "An ancient red dragon, vast beyond belief, its scales like molten rubies and its eyes like twin suns.",
  hp=3.5, dmg=1.4, armor=2.0, aggro=True, boss=True, xp=6.0, gold=10.0,
  specials=[big("Dragonfire", 0.25, 2.2, "rears back and engulfs you in a torrent of dragonfire!"),
            dot("Searing Wounds", 0.15, 0.5, 4, "fire", "rakes you with claws that leave searing wounds!"),
            stun("Wing Buffet", 0.12, 1, "buffets you to the ground with a mighty wing!")],
  loot=[("pyraxis_fang", 0.7), ("dragonscale_mail", 0.7), ("heart_of_flame", 0.5), ("dragon_scale", 1.0)])
