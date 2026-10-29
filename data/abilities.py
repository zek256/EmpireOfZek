"""Spells and class abilities.

Every entry is learned automatically when its class reaches `level`. After a
rebirth, abilities of previous classes are kept but only become usable once the
current level reaches the level at which they were first learned.

kind     - "spell" (costs mana, scales with level) or "ability" (free, cooldown-based)
cost     - base mana cost; actual cost = cost * (1 + 0.1 * (level - 1))
cooldown - rounds before it can be used again
target   - "enemy", "all" (every engaged enemy) or "self"

Effect power = base + lvl * character_level + scale * character_stat
"""


def DMG(base, lvl, scale, stat, element="arcane"):
    return {"type": "damage", "base": base, "lvl": lvl, "scale": scale, "stat": stat, "element": element}


def WEAPON(mult):
    return {"type": "weapon", "mult": mult}


def HEAL(base, lvl, scale, stat):
    return {"type": "heal", "base": base, "lvl": lvl, "scale": scale, "stat": stat}


def HEALPCT(pct):
    return {"type": "heal_pct", "pct": pct}


def HOT(base, lvl, scale, stat, turns, name):
    return {"type": "hot", "base": base, "lvl": lvl, "scale": scale, "stat": stat, "turns": turns, "name": name}


def DOT(base, lvl, scale, stat, turns, name, element="poison"):
    return {"type": "dot", "base": base, "lvl": lvl, "scale": scale, "stat": stat,
            "turns": turns, "name": name, "element": element}


def DRAIN(base, lvl, scale, stat, frac, element="shadow"):
    return {"type": "drain", "base": base, "lvl": lvl, "scale": scale, "stat": stat,
            "frac": frac, "element": element}


def SHIELD(base, lvl, scale, stat):
    return {"type": "shield", "base": base, "lvl": lvl, "scale": scale, "stat": stat}


def BUFF(name, turns, **mods):
    """mods: damage_pct, armor (flat), armor_lvl (per level), dodge, lifesteal."""
    return {"type": "buff", "name": name, "turns": turns, "mods": mods}


def STUN(turns, chance=1.0):
    return {"type": "stun", "turns": turns, "chance": chance}


def WEAKEN(pct, turns, name="Weakened"):
    return {"type": "weaken", "pct": pct, "turns": turns, "name": name}


def SUMMON(name, hp_base, hp_lvl, dmg_base, dmg_lvl, scale_stat, desc):
    return {"type": "summon", "name": name, "hp_base": hp_base, "hp_lvl": hp_lvl,
            "dmg_base": dmg_base, "dmg_lvl": dmg_lvl, "stat": scale_stat, "desc": desc}


ABILITIES = {}


def _add(aid, name, cls, level, kind, effects, cost=0, cooldown=0, target="enemy", desc="", msg=""):
    ABILITIES[aid] = {
        "id": aid, "name": name, "cls": cls, "level": level, "kind": kind, "cost": cost,
        "cooldown": cooldown, "target": target, "effects": effects, "desc": desc, "msg": msg,
    }


def spell(aid, name, cls, level, cost, effects, **kw):
    _add(aid, name, cls, level, "spell", effects, cost=cost, **kw)


def ability(aid, name, cls, level, cooldown, effects, **kw):
    _add(aid, name, cls, level, "ability", effects, cooldown=cooldown, **kw)


# ---------------------------------------------------------------- Warrior
ability("slam", "Slam", "warrior", 1, 3, [WEAPON(1.4), STUN(1, 0.3)],
        desc="A crushing shield-and-shoulder blow that may stun.",
        msg="You hurl your full weight into {t}!")
ability("battle_cry", "Battle Cry", "warrior", 5, 8, [BUFF("Battle Cry", 5, damage_pct=0.25)], target="self",
        desc="A thunderous roar that raises your damage by 25% for 5 rounds.",
        msg="You loose a bellowing war cry that shakes the very stones!")
ability("second_wind", "Second Wind", "warrior", 8, 15, [HEALPCT(0.35)], target="self",
        desc="Grit your teeth and fight on, recovering 35% of your health.",
        msg="You grit your teeth, draw a ragged breath, and find a second wind!")
ability("cleave", "Cleave", "warrior", 12, 3, [WEAPON(1.1)], target="all",
        desc="A wide sweeping strike that hits every engaged foe.",
        msg="You whirl your weapon in a great arc!")
ability("shield_wall", "Shield Wall", "warrior", 20, 8, [BUFF("Shield Wall", 4, armor=20, armor_lvl=3)], target="self",
        desc="Brace behind your guard, greatly increasing armor for 4 rounds.",
        msg="You set your feet and become an immovable wall of iron.")
ability("rampage", "Rampage", "warrior", 30, 4, [WEAPON(2.6)],
        desc="A furious flurry of blows against a single foe.",
        msg="Red rage fills your vision as you rampage against {t}!")
ability("avatar_of_war", "Avatar of War", "warrior", 42, 12,
        [BUFF("Avatar of War", 5, damage_pct=0.6, armor_lvl=2), HEALPCT(0.3)], target="self",
        desc="Become an avatar of battle: heal 30% and gain +60% damage for 5 rounds.",
        msg="The spirits of a thousand fallen champions pour into you!")

# ---------------------------------------------------------------- Cleric
spell("minor_healing", "Minor Healing", "cleric", 1, 6, [HEAL(12, 2.5, 0.6, "WIS")], target="self",
      desc="A gentle prayer that mends wounds.", msg="Soft golden light knits your wounds closed.")
spell("smite", "Smite", "cleric", 3, 6, [DMG(8, 1.6, 0.45, "WIS", "holy")],
      desc="Call down a lance of holy light upon a foe.", msg="A shaft of searing radiance strikes {t}!")
spell("divine_aegis", "Divine Aegis", "cleric", 8, 12, [SHIELD(15, 3, 1.0, "WIS")], cooldown=6, target="self",
      desc="A shimmering ward that absorbs damage.", msg="A dome of pale gold light surrounds you.")
spell("greater_healing", "Greater Healing", "cleric", 15, 18, [HEAL(35, 6, 1.1, "WIS")], target="self",
      desc="A powerful prayer of restoration.", msg="The Dawnfather's warmth floods through your body.")
spell("holy_wrath", "Holy Wrath", "cleric", 25, 30, [DMG(20, 2.5, 0.6, "WIS", "holy")], cooldown=3, target="all",
      desc="Holy fire erupts around you, burning every foe.", msg="Pillars of holy fire erupt from the ground!")
spell("resurgence", "Resurgence", "cleric", 35, 28, [HOT(15, 2.2, 0.35, "WIS", 5, "Resurgence")], cooldown=6, target="self",
      desc="Steady divine renewal over 5 rounds.", msg="A radiant halo settles upon your brow.")
spell("sunburst", "Sunburst", "cleric", 45, 60, [DMG(60, 4.5, 1.3, "WIS", "holy"), STUN(1, 0.5)], cooldown=5,
      desc="Call down the noonday sun upon a single foe.", msg="The sky splits and the noonday sun descends upon {t}!")

# ---------------------------------------------------------------- Wizard
spell("magic_missile", "Magic Missile", "wizard", 1, 5, [DMG(6, 1.5, 0.45, "INT", "arcane")],
      desc="Darts of pure force that never miss.", msg="Three darts of violet force streak toward {t}!")
spell("frost_bolt", "Frost Bolt", "wizard", 5, 9, [DMG(10, 2.0, 0.5, "INT", "frost"), STUN(1, 0.3)],
      desc="A shard of ice that may freeze its target solid.", msg="A jagged shard of ice hurtles at {t}!")
spell("mana_shield", "Mana Shield", "wizard", 10, 14, [SHIELD(15, 3, 0.9, "INT")], cooldown=6, target="self",
      desc="Weave raw mana into a barrier that absorbs damage.", msg="Shimmering blue runes orbit you protectively.")
spell("fireball", "Fireball", "wizard", 16, 24, [DMG(15, 2.2, 0.6, "INT", "fire")], cooldown=2, target="all",
      desc="An exploding sphere of flame that engulfs every foe.", msg="A roaring ball of fire blossoms among your enemies!")
spell("lightning_lance", "Lightning Lance", "wizard", 26, 32, [DMG(30, 3.6, 1.05, "INT", "lightning")], cooldown=2,
      desc="A crackling spear of lightning.", msg="Thunder booms as a lance of lightning impales {t}!")
spell("meteor", "Meteor", "wizard", 40, 75, [DMG(60, 4.0, 1.3, "INT", "fire")], cooldown=5, target="all",
      desc="Call a blazing star down from the heavens.", msg="The heavens burn as a meteor crashes down upon your foes!")

# ---------------------------------------------------------------- Necromancer
spell("lifetap", "Lifetap", "necromancer", 1, 5, [DRAIN(6, 1.4, 0.4, "INT", 0.35)],
      desc="Steal life from a foe to mend your own.", msg="Ghostly tendrils draw the life from {t}.")
spell("raise_skeleton", "Raise Skeleton", "necromancer", 4, 18,
      [SUMMON("a rattling skeleton", 20, 6, 2, 1.3, "INT", "A clattering skeleton with empty, burning eyes.")],
      cooldown=10, target="self",
      desc="Raise a skeletal servant to fight for you.", msg="Bones claw their way up from the earth and assemble!")
spell("plague", "Plague", "necromancer", 10, 12, [DOT(5, 1.1, 0.25, "INT", 5, "Plague", "disease")],
      desc="Infect a foe with a wasting disease.", msg="A sickly green miasma seeps into {t}.")
spell("bone_spear", "Bone Spear", "necromancer", 18, 22, [DMG(18, 2.8, 0.8, "INT", "shadow")],
      desc="Hurl a spear of sharpened bone.", msg="A spear of jagged bone erupts from your palm toward {t}!")
spell("siphon_soul", "Siphon Soul", "necromancer", 28, 34, [DRAIN(25, 3.0, 0.9, "INT", 0.6)], cooldown=3,
      desc="Tear out a fragment of a foe's soul and devour it.", msg="You reach into {t} and tear free a shrieking wisp of soul!")
spell("bone_colossus", "Raise Bone Colossus", "necromancer", 38, 55,
      [SUMMON("a towering bone colossus", 60, 14, 6, 2.6, "INT", "A hulking giant of fused bones, ten feet tall.")],
      cooldown=15, target="self",
      desc="Raise a towering colossus of fused bone.", msg="The ground heaves as a colossus of bone rises screaming from the earth!")
spell("wail_of_the_damned", "Wail of the Damned", "necromancer", 46, 60,
      [DMG(40, 3.2, 1.0, "INT", "shadow"), WEAKEN(0.3, 4, "Terrified")], cooldown=5, target="all",
      desc="Unleash the screams of the dead, harming and terrifying all foes.", msg="The howls of a thousand damned souls burst from your throat!")

# ---------------------------------------------------------------- Shaman
spell("frost_shock", "Frost Shock", "shaman", 1, 5, [DMG(6, 1.45, 0.42, "WIS", "frost")],
      desc="A biting blast of spirit-frost.", msg="Spirit-frost crackles across {t}!")
spell("ancestral_mending", "Ancestral Mending", "shaman", 3, 6, [HEAL(10, 2.2, 0.55, "WIS")], target="self",
      desc="Your ancestors mend your wounds.", msg="Whispering ancestors lay spectral hands upon you.")
spell("spirit_wolf", "Spirit Wolf", "shaman", 8, 20,
      [SUMMON("a spectral spirit wolf", 20, 6, 3, 1.3, "WIS", "A translucent blue wolf with eyes like stars.")],
      cooldown=10, target="self",
      desc="Summon a wolf from the spirit world.", msg="A ghostly howl answers your call, and a spirit wolf bounds to your side!")
spell("spirit_of_the_bear", "Spirit of the Bear", "shaman", 15, 15,
      [BUFF("Spirit of the Bear", 6, damage_pct=0.2, armor=10, armor_lvl=1.5)], cooldown=10, target="self",
      desc="The great bear's strength fills you (+20% damage, +armor).", msg="The great Bear-Spirit's strength swells within you.")
spell("serpent_venom", "Venom of the Serpent", "shaman", 24, 24,
      [DOT(8, 1.5, 0.4, "WIS", 5, "Serpent Venom", "poison"), WEAKEN(0.2, 4, "Envenomed")],
      desc="Spirit-venom that poisons and weakens a foe.", msg="A spectral serpent sinks its fangs into {t}!")
spell("chain_lightning", "Chain Lightning", "shaman", 34, 48, [DMG(35, 3.0, 0.9, "WIS", "lightning")], cooldown=3, target="all",
      desc="Lightning that leaps from foe to foe.", msg="Lightning arcs from your totem, leaping from foe to foe!")
spell("ancestral_avatar", "Ancestral Avatar", "shaman", 44, 55,
      [HEALPCT(0.45), BUFF("Ancestral Avatar", 5, damage_pct=0.4)], cooldown=12, target="self",
      desc="Become one with the ancestors: heal 45% and +40% damage.", msg="Your ancestors rise around you in a storm of spectral light!")

# ---------------------------------------------------------------- Druid
spell("thornlash", "Thornlash", "druid", 1, 5, [DMG(7, 1.6, 0.48, "WIS", "nature")],
      desc="A whip of thorny vines lashes a foe.", msg="Thorny vines burst from the earth and lash {t}!")
spell("regrowth", "Regrowth", "druid", 3, 7, [HEAL(10, 2.0, 0.5, "WIS"), HOT(4, 1.2, 0.25, "WIS", 5, "Regrowth")], target="self",
      desc="An instant heal followed by steady renewal.", msg="Green leaves unfurl across your skin, healing as they grow.")
spell("entangling_roots", "Entangling Roots", "druid", 8, 10, [DMG(5, 0.8, 0.2, "WIS", "nature"), STUN(2, 0.75)], cooldown=4,
      desc="Roots seize a foe and may hold it fast for 2 rounds.", msg="Gnarled roots erupt and coil around {t}!")
spell("moonfire", "Moonfire", "druid", 15, 18,
      [DMG(16, 2.4, 0.7, "WIS", "arcane"), DOT(5, 1.0, 0.25, "WIS", 4, "Moonfire", "arcane")],
      desc="Silver moonlight burns a foe and lingers.", msg="A column of silver moonfire engulfs {t}!")
spell("barkskin", "Barkskin", "druid", 22, 16, [BUFF("Barkskin", 6, armor=15, armor_lvl=2.5), HOT(5, 0.8, 0.15, "WIS", 6, "Barkskin")],
      cooldown=10, target="self",
      desc="Your skin hardens into living oak (+armor, slow healing).", msg="Your skin cracks and hardens into living oak bark.")
spell("starfall", "Starfall", "druid", 32, 45, [DMG(34, 3.2, 0.95, "WIS", "arcane")], cooldown=3, target="all",
      desc="Stars rain from the sky upon all foes.", msg="Shards of starlight rain down upon your enemies!")
spell("wrath_of_the_wild", "Wrath of the Wild", "druid", 44, 60, [DMG(55, 4.2, 1.25, "WIS", "nature"), HEALPCT(0.2)], cooldown=5,
      desc="The whole forest rises against a foe, and its strength flows into you.", msg="The forest itself rises in fury against {t}!")

# ---------------------------------------------------------------- Rogue
ability("backstab", "Backstab", "rogue", 1, 2, [WEAPON(1.7)],
        desc="Slip behind your foe and drive your blade home.", msg="You slip into {t}'s blind spot and strike!")
ability("poisoned_blade", "Poisoned Blade", "rogue", 5, 4, [WEAPON(1.0), DOT(4, 0.9, 0.2, "DEX", 4, "Deadly Poison", "poison")],
        desc="A strike with a venom-coated blade.", msg="Your venom-slick blade bites into {t}.")
ability("evasion", "Evasion", "rogue", 10, 8, [BUFF("Evasion", 3, dodge=0.4)], target="self",
        desc="Become nearly impossible to hit for 3 rounds (+40% dodge).", msg="You become a blur of motion.")
ability("kidney_shot", "Kidney Shot", "rogue", 18, 6, [WEAPON(1.0), STUN(2, 0.85)],
        desc="A crippling blow that stuns for 2 rounds.", msg="You drive a brutal blow into {t}'s kidney!")
ability("eviscerate", "Eviscerate", "rogue", 28, 4, [WEAPON(2.8)],
        desc="A vicious finishing strike.", msg="Your blades flash in a vicious, gutting strike against {t}!")
ability("shadow_dance", "Shadow Dance", "rogue", 40, 10, [BUFF("Shadow Dance", 4, damage_pct=0.5, dodge=0.25)], target="self",
        desc="Melt into the shadows: +50% damage and +25% dodge.", msg="The shadows embrace you like an old friend.")
ability("assassinate", "Assassinate", "rogue", 48, 6, [WEAPON(4.2)],
        desc="A single perfect, lethal strike.", msg="Time seems to stop as you find the perfect opening in {t}'s guard...")

# ---------------------------------------------------------------- Ranger
ability("aimed_shot", "Aimed Shot", "ranger", 1, 2, [WEAPON(1.6)],
        desc="A carefully aimed strike at a vital spot.", msg="You draw a slow breath, take aim at {t}, and loose!")
spell("hunters_mend", "Hunter's Mend", "ranger", 4, 6, [HEAL(9, 2.0, 0.45, "WIS")], target="self",
      desc="Woodland lore and a whispered prayer mend your wounds.", msg="You murmur an old woodland prayer and your wounds close.")
ability("multishot", "Multishot", "ranger", 10, 3, [WEAPON(0.95)], target="all",
        desc="A volley that strikes every engaged foe.", msg="You loose a fan of arrows at your enemies!")
spell("bonded_wolf", "Call Bonded Wolf", "ranger", 16, 20,
      [SUMMON("a grey timber wolf", 25, 7, 3, 1.5, "WIS", "A loyal grey wolf, scarred and keen-eyed.")],
      cooldown=10, target="self",
      desc="Call your loyal animal companion to your side.", msg="You whistle sharply, and a grey wolf lopes out of the brush to your side.")
ability("serpent_sting", "Serpent Sting", "ranger", 24, 4, [WEAPON(0.9), DOT(8, 1.4, 0.3, "DEX", 5, "Serpent Sting", "poison")],
        desc="A venomed arrow that poisons for 5 rounds.", msg="A green-fletched arrow strikes {t}, its venom spreading.")
ability("rain_of_arrows", "Rain of Arrows", "ranger", 34, 4, [WEAPON(1.6)], target="all",
        desc="Darken the sky with arrows.", msg="The sky darkens as your arrows rain down!")
ability("deadeye", "Deadeye", "ranger", 45, 5, [WEAPON(3.6)],
        desc="A legendary shot that finds the heart.", msg="The world narrows to a single point on {t}. You release.")

# ---------------------------------------------------------------- Paladin
ability("holy_strike", "Holy Strike", "paladin", 1, 2, [WEAPON(1.2), DMG(3, 1.0, 0.3, "WIS", "holy")],
        desc="A weapon strike wreathed in holy light.", msg="Your weapon blazes with holy light as you strike {t}!")
ability("lay_on_hands", "Lay on Hands", "paladin", 5, 20, [HEALPCT(0.6)], target="self",
        desc="A miraculous touch that restores 60% of your health.", msg="You press a glowing hand to your heart and feel your strength return.")
spell("blessing_of_might", "Blessing of Might", "paladin", 10, 10, [BUFF("Blessing of Might", 6, damage_pct=0.25)], cooldown=6, target="self",
      desc="The Dawnfather blesses your arm (+25% damage).", msg="Golden light blesses your sword-arm.")
spell("divine_shield", "Divine Shield", "paladin", 18, 22, [SHIELD(20, 4, 1.0, "WIS")], cooldown=10, target="self",
      desc="An unbreakable ward of faith.", msg="A radiant shield of faith flares into being around you.")
ability("hammer_of_justice", "Hammer of Justice", "paladin", 26, 6, [WEAPON(1.6), STUN(2, 0.9)],
        desc="A hammer-blow of divine judgment that stuns.", msg="A spectral hammer of light descends with your blow upon {t}!")
spell("consecration", "Consecration", "paladin", 36, 38, [DMG(25, 2.6, 0.7, "WIS", "holy"), HEAL(10, 1.5, 0.3, "WIS")], cooldown=3, target="all",
      desc="Hallow the ground, burning foes and healing you.", msg="The ground beneath you blazes with consecrated light!")
ability("avenging_wrath", "Avenging Wrath", "paladin", 46, 12, [BUFF("Avenging Wrath", 5, damage_pct=0.6), HEALPCT(0.3)], target="self",
        desc="Golden wings of wrath: heal 30% and +60% damage.", msg="Golden wings of light unfurl from your back!")

# ---------------------------------------------------------------- Shadow Knight
ability("shadow_strike", "Shadow Strike", "shadow knight", 1, 2, [WEAPON(1.2), DRAIN(3, 1.0, 0.3, "INT", 0.6)],
        desc="A strike that drinks a sip of your foe's life.", msg="Your blade, wreathed in shadow, drinks from {t}!")
spell("disease_cloud", "Disease Cloud", "shadow knight", 4, 6, [DOT(4, 1.0, 0.25, "INT", 5, "Disease Cloud", "disease")],
      desc="A cloud of festering disease.", msg="A cloud of festering spores billows around {t}.")
spell("dread_aura", "Dread Aura", "shadow knight", 10, 12, [WEAKEN(0.25, 5, "Dread")], target="all", cooldown=6,
      desc="Your aura of terror weakens all foes (-25% damage).", msg="An aura of soul-chilling dread pours from you.")
ability("harm_touch", "Harm Touch", "shadow knight", 18, 20, [DMG(40, 5.0, 1.5, "INT", "shadow")],
        desc="Channel death itself through your touch.", msg="You lay a hand upon {t} and death itself flows through it!")
spell("vampiric_embrace", "Vampiric Embrace", "shadow knight", 26, 24, [BUFF("Vampiric Embrace", 6, lifesteal=0.25)], cooldown=8, target="self",
      desc="Your attacks heal you for 25% of damage dealt.", msg="Your veins run black with a vampiric hunger.")
spell("death_coil", "Death Coil", "shadow knight", 34, 32, [DRAIN(30, 3.2, 0.9, "INT", 0.8)], cooldown=3,
      desc="A coil of death that drains a foe.", msg="A shrieking coil of black fire lashes {t}!")
ability("unholy_frenzy", "Unholy Frenzy", "shadow knight", 44, 12, [BUFF("Unholy Frenzy", 5, damage_pct=0.5, lifesteal=0.3)], target="self",
        desc="An unholy frenzy: +50% damage and 30% lifesteal.", msg="An unholy frenzy seizes you, and you laugh with a voice not your own!")

# ---------------------------------------------------------------- Bard
spell("discordant_note", "Discordant Note", "bard", 1, 5, [DMG(7, 1.6, 0.5, "CHA", "sonic")],
      desc="A jarring note that rattles a foe's skull.", msg="You strike a jarring, discordant note at {t}!")
spell("ballad_of_mending", "Ballad of Mending", "bard", 3, 7, [HEAL(5, 1.0, 0.25, "CHA"), HOT(4, 1.0, 0.22, "CHA", 5, "Ballad of Mending")], target="self",
      desc="A soothing ballad that heals over time.", msg="You hum a soothing ballad and your wounds begin to close.")
spell("lullaby", "Lullaby", "bard", 8, 10, [STUN(2, 0.75)], cooldown=5,
      desc="A sweet lullaby that may put a foe to sleep for 2 rounds.", msg="You sing a gentle lullaby to {t}...")
spell("war_march", "War March", "bard", 15, 15, [BUFF("War March", 8, damage_pct=0.25, armor=8, armor_lvl=1.0)], cooldown=10, target="self",
      desc="A rousing march (+25% damage, +armor).", msg="You strike up a rousing war march!")
spell("dirge_of_despair", "Dirge of Despair", "bard", 24, 26, [DOT(9, 1.6, 0.4, "CHA", 4, "Dirge", "sonic"), WEAKEN(0.25, 4, "Despair")], target="all",
      desc="A mournful dirge that saps the will of all foes.", msg="You sing a dirge of such sorrow that your foes falter.")
spell("crescendo", "Crescendo", "bard", 34, 45, [DMG(34, 3.2, 0.95, "CHA", "sonic")], cooldown=3, target="all",
      desc="A shattering crescendo of sound.", msg="Your song swells to a shattering crescendo!")
spell("legends_anthem", "Legend's Anthem", "bard", 44, 55, [BUFF("Legend's Anthem", 6, damage_pct=0.45), HOT(20, 2.0, 0.4, "CHA", 6, "Legend's Anthem")],
      cooldown=12, target="self",
      desc="The anthem of legends (+45% damage and strong healing).", msg="You sing the Anthem of Legends, and the air itself trembles!")
