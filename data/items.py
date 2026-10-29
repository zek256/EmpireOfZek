"""Items: weapons, armor, consumables and quest items.

level is the minimum character level required to equip an item.
"""

SLOTS = ["weapon", "shield", "head", "chest", "hands", "legs", "feet", "neck", "ring"]

ITEMS = {}


def weapon(iid, name, level, dmg, value, desc, **stats):
    ITEMS[iid] = {"id": iid, "name": name, "type": "weapon", "slot": "weapon", "level": level,
                  "dmg": dmg, "armor": 0, "stats": stats, "value": value, "desc": desc}


def armor(iid, name, slot, level, ac, value, desc, **stats):
    ITEMS[iid] = {"id": iid, "name": name, "type": "armor", "slot": slot, "level": level,
                  "armor": ac, "stats": stats, "value": value, "desc": desc}


def potion(iid, name, level, value, desc, heal=0, mana=0):
    ITEMS[iid] = {"id": iid, "name": name, "type": "consumable", "level": level,
                  "heal": heal, "mana": mana, "value": value, "desc": desc}


def misc(iid, name, value, desc, kind="junk"):
    ITEMS[iid] = {"id": iid, "name": name, "type": kind, "value": value, "desc": desc}


# ------------------------------------------------------------------ Weapons
weapon("rusty_shortsword", "a rusty shortsword", 1, (2, 5), 4,
       "A pitted, notched blade that has seen better days.")
weapon("worn_dagger", "a worn dagger", 1, (2, 4), 3,
       "A simple dagger with a leather-wrapped grip.", DEX=1)
weapon("oak_staff", "an oak staff", 1, (1, 4), 3,
       "A sturdy oaken staff, carved with simple runes.", INT=1, WIS=1)
weapon("training_mace", "a training mace", 1, (2, 5), 4,
       "A blunt, iron-banded club used by temple initiates.")
weapon("ash_shortbow", "an ash shortbow", 1, (2, 5), 4,
       "A light hunting bow of springy ash wood.")
weapon("iron_longsword", "an iron longsword", 5, (4, 9), 45,
       "A well-balanced longsword forged by Durgan Ironhand.", STR=1)
weapon("steel_dagger", "a steel dagger", 5, (4, 8), 40,
       "A keen steel dagger with a wicked edge.", DEX=2)
weapon("yew_longbow", "a yew longbow", 5, (4, 9), 45,
       "A tall bow of seasoned yew.", DEX=1)
weapon("runed_staff", "a runed staff", 5, (3, 7), 45,
       "A staff of blackwood inlaid with glowing silver runes.", INT=2, WIS=2, CHA=1)
weapon("iron_mace", "an iron flanged mace", 5, (4, 9), 45,
       "A heavy mace with cruel iron flanges.", STR=1, WIS=1)
weapon("bandit_cutlass", "Rask's notched cutlass", 8, (6, 12), 90,
       "The curved blade of the bandit chieftain, its edge notched from many fights.", STR=2, DEX=2)
weapon("bonecleaver", "a bonecleaver axe", 12, (9, 16), 140,
       "A brutal axe with a blade of blackened iron, pulled from a crypt guardian.", STR=3)
weapon("knights_blade", "a knight's broadsword", 14, (10, 18), 260,
       "A broadsword of fine steel bearing the crest of the Brightwater guard.", STR=3, CON=2)
weapon("serpentfang", "Serpentfang", 15, (10, 17), 280,
       "A curved dagger carved from a giant serpent's fang. It still drips venom.", DEX=5)
weapon("varnoth_scepter", "the Scepter of Varnoth", 15, (8, 14), 400,
       "A sceptre of yellowed bone crowned with a smouldering green gem.", INT=6, WIS=6, CHA=3)
weapon("bogwood_staff", "a bogwood staff", 18, (9, 16), 320,
       "Black, twisted wood from the heart of the Mirefen, humming with old power.", INT=6, WIS=6)
weapon("gristles_hexrod", "Gristle's Hexrod", 20, (10, 18), 550,
       "A crooked rod strung with tiny bones and charms. Wicked magic seeps from it.", INT=8, WIS=8, CHA=5)
weapon("mithril_sword", "a mithril longsword", 22, (15, 26), 600,
       "A shimmering blade of mithril, light as a feather and sharp as sorrow.", STR=4, DEX=4)
weapon("hunters_recurve", "a hunter's recurve bow", 22, (15, 26), 600,
       "A recurve bow of horn and sinew, made by mountain hunters.", DEX=6, WIS=2)
weapon("orcish_greataxe", "an orcish greataxe", 26, (19, 33), 750,
       "A massive double-bladed axe hung with clan totems.", STR=6, CON=2)
weapon("gorraks_warhammer", "Gorrak's Skullsplitter", 30, (23, 39), 1200,
       "The warlord's colossal warhammer. Its head is stained a deep rust-brown.", STR=8, CON=6)
weapon("frostbrand", "Frostbrand", 30, (22, 37), 1200,
       "A blade of blue steel rimed with frost that never melts.", STR=5, DEX=5, INT=3)
weapon("frostweave_staff", "a frostweave staff", 30, (17, 28), 1100,
       "A staff of pale wood sheathed in ever-cold ice crystals.", INT=9, WIS=9)
weapon("elven_longbow", "an Elandorian longbow", 33, (24, 40), 1500,
       "A graceful bow of white wood, strung with silver thread.", DEX=9, WIS=3)
weapon("elandor_runeblade", "an Elandorian runeblade", 36, (27, 45), 1800,
       "An ancient elven sword whose runes glow faintly at dusk.", STR=7, DEX=7, CHA=3)
weapon("staff_of_stars", "the Staff of Stars", 38, (20, 34), 2000,
       "A staff of midnight crystal in which tiny stars slowly turn.", INT=12, WIS=12, CHA=5)
weapon("seluvars_wand", "Seluvar's Hollow Wand", 40, (22, 36), 3000,
       "The wand of the hollow archmage. It whispers forgotten words.", INT=16, WIS=10, CHA=8)
weapon("sunforged_mace", "the Sunforged Mace", 43, (31, 51), 3200,
       "A mace forged in dragonfire and blessed beneath the noon sun.", STR=8, WIS=10)
weapon("obsidian_blade", "an obsidian greatblade", 45, (33, 55), 3600,
       "A greatsword of volcanic glass, hot to the touch.", STR=10, DEX=5, CON=4)
weapon("dragonbone_staff", "a dragonbone staff", 47, (26, 42), 4200,
       "A staff of polished dragonbone that crackles with ancient fire.", INT=18, WIS=18, CHA=6)
weapon("pyraxis_fang", "Fang of Pyraxis", 50, (42, 68), 9000,
       "A sword ground from a fang of the Eternal Flame itself. It burns with inner light.",
       STR=12, DEX=12, CON=8, INT=8, WIS=8, CHA=8)

# ------------------------------------------------------------------ Armor
armor("padded_tunic", "a padded tunic", "chest", 1, 3, 4, "A quilted cloth tunic that turns aside the odd blow.")
armor("leather_cap", "a leather cap", "head", 1, 1, 3, "A simple cap of boiled leather.")
armor("leather_boots", "leather boots", "feet", 1, 1, 3, "Sturdy boots fit for the road.")
armor("wooden_shield", "a wooden shield", "shield", 1, 2, 4, "A round shield of planks bound with iron.")
armor("leather_gloves", "leather gloves", "hands", 2, 1, 6, "Supple leather gloves.")
armor("leather_leggings", "leather leggings", "legs", 2, 2, 8, "Leggings of tough boiled leather.")
armor("leather_jerkin", "a leather jerkin", "chest", 3, 5, 20, "A jerkin of thick, studded leather.")
armor("iron_buckler", "an iron buckler", "shield", 4, 4, 25, "A small round shield of beaten iron.")
armor("studded_gloves", "studded gloves", "hands", 5, 3, 30, "Leather gloves studded with iron rivets.", STR=1)
armor("wolfhide_boots", "wolfhide boots", "feet", 5, 3, 30, "Warm boots of grey wolf hide.", DEX=1)
armor("chain_shirt", "a chain shirt", "chest", 8, 9, 90, "A shirt of riveted iron rings.", CON=1)
armor("iron_helm", "an iron helm", "head", 8, 4, 70, "A plain iron helm with a nasal guard.")
armor("chain_leggings", "chain leggings", "legs", 10, 7, 110, "Leggings of fine iron mail.")
armor("ring_of_vigor", "a ring of vigor", "ring", 10, 0, 150, "A copper ring that hums with life.", CON=3, STR=1)
armor("amulet_of_the_dawn", "the Amulet of the Dawn", "neck", 12, 2, 300,
      "A golden sun-disc on a fine chain, blessed by the temple.", WIS=3, CHA=3, CON=2)
armor("bone_helm", "a bone-crested helm", "head", 13, 7, 160, "A helm adorned with the skull of some great beast.", CON=2)
armor("grave_shroud", "a grave-warden's shroud", "chest", 14, 10, 250,
      "A dark robe stitched with silver wards against the dead.", INT=3, WIS=3)
armor("iron_boots", "iron-shod boots", "feet", 12, 5, 120, "Heavy boots capped with iron.")
armor("knight_breastplate", "a knight's breastplate", "chest", 18, 18, 500, "A gleaming steel breastplate.", CON=3)
armor("mirescale_vest", "a mirescale vest", "chest", 17, 15, 450, "A vest of green scales from a bog lurker.", DEX=3)
armor("hag_charm", "a hag's charm", "neck", 20, 3, 600, "A knot of hair, bone and something that still twitches.", INT=5, WIS=5)
armor("steel_kite_shield", "a steel kite shield", "shield", 18, 12, 450, "A tall shield of polished steel.", CON=2)
armor("plate_gauntlets", "plate gauntlets", "hands", 20, 8, 450, "Articulated steel gauntlets.", STR=2)
armor("mithril_hauberk", "a mithril hauberk", "chest", 24, 24, 900, "Elegant mithril mail, light and strong.", CON=4, DEX=2)
armor("orcish_helm", "a horned orcish helm", "head", 26, 12, 700, "A brutal horned helm of black iron.", STR=3, CON=3)
armor("tower_shield", "an iron tower shield", "shield", 28, 18, 900, "A massive shield as tall as a dwarf.", CON=4)
armor("warlord_gauntlets", "the Warlord's Gauntlets", "hands", 30, 12, 1300, "Spiked gauntlets stained with old blood.", STR=5, CON=3)
armor("frostgiant_greaves", "frost giant greaves", "legs", 30, 18, 1200, "Leg plates of rime-covered giant iron.", CON=5)
armor("frost_ring", "a ring of winter", "ring", 30, 0, 1300, "A ring of ice that never melts.", INT=5, WIS=5, DEX=3)
armor("elandor_robes", "robes of Elandor", "chest", 35, 22, 1800, "Robes of silver silk woven with protective sigils.", INT=8, WIS=8, CHA=4)
armor("elandor_plate", "Elandorian plate", "chest", 36, 34, 2000, "Gleaming elven plate engraved with leaves and stars.", STR=4, CON=6)
armor("starlight_circlet", "a starlight circlet", "head", 36, 14, 1800, "A silver circlet set with a single pale gem.", INT=6, WIS=6, CHA=4)
armor("archmage_ring", "the Ring of the Archmage", "ring", 40, 0, 3000, "A ring of black crystal once worn by Seluvar.", INT=10, WIS=6)
armor("obsidian_greaves", "obsidian greaves", "legs", 44, 30, 2800, "Greaves of black volcanic glass.", CON=6, STR=4)
armor("ember_ring", "an ember ring", "ring", 44, 0, 2800, "A ring holding a coal that never dies.", STR=6, DEX=6, CON=4)
armor("ashen_crown", "the Ashen Crown", "head", 46, 24, 3500, "A crown of blackened gold, still warm.",
      STR=3, DEX=3, CON=3, INT=3, WIS=3, CHA=3)
armor("drakehide_boots", "drakehide boots", "feet", 45, 16, 2600, "Boots of red drake leather that resist all flame.", DEX=5)
armor("dragonscale_mail", "Dragonscale Mail", "chest", 48, 52, 7000, "Armor crafted from the scales of Pyraxis.", CON=12, STR=6, DEX=6)
armor("heart_of_flame", "the Heart of Flame", "neck", 50, 10, 8000, "A pendant holding a fragment of a dragon's heart.",
      STR=8, DEX=8, CON=8, INT=8, WIS=8, CHA=8)

# ------------------------------------------------------------------ Consumables
potion("minor_healing_potion", "a minor healing potion", 1, 10, "A small vial of red liquid.", heal=45)
potion("minor_mana_potion", "a minor mana potion", 1, 12, "A small vial of shimmering blue liquid.", mana=30)
potion("healing_potion", "a healing potion", 10, 45, "A flask of glowing red liquid.", heal=180)
potion("mana_potion", "a mana potion", 10, 50, "A flask of swirling blue liquid.", mana=120)
potion("greater_healing_potion", "a greater healing potion", 25, 140, "A crystal flask of bright crimson elixir.", heal=550)
potion("greater_mana_potion", "a greater mana potion", 25, 150, "A crystal flask of deep sapphire elixir.", mana=350)
potion("supreme_healing_potion", "a supreme healing potion", 40, 350, "A phial of liquid sunlight.", heal=1400)
potion("supreme_mana_potion", "a supreme mana potion", 40, 380, "A phial of liquid starlight.", mana=800)

# ------------------------------------------------------------------ Quest items / trophies
misc("wolf_pelt", "a grey wolf pelt", 6, "A thick grey pelt, still smelling of the forest.", kind="quest")
misc("rat_tail", "a rat tail", 1, "A long, scaly rat tail. Disgusting.")
misc("spider_silk", "a bundle of spider silk", 8, "Strong, sticky silk from a giant spider.")
misc("bone_dust", "a pouch of bone dust", 15, "Fine grey dust ground from ancient bones.")
misc("bog_pearl", "a bog pearl", 60, "A murky green pearl found in the Mirefen.")
misc("orc_tusk", "an orc tusk", 40, "A yellowed tusk, prized by bone-carvers.")
misc("frost_shard", "a frost shard", 90, "A shard of ice that never melts.")
misc("elven_relic", "an elven relic", 160, "A small silver figurine of exquisite elven make.")
misc("dragon_scale", "a dragon scale", 300, "A scale the size of a dinner plate, red as embers.")
