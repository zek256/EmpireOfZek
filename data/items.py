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

# ------------------------------------------------------------------ Caster gear (sold by Elowen Silverthread)
# Light on armor, heavy on INT/WIS/CHA. The best caster gear still drops from monsters and bosses.
armor("linen_robe", "a linen robe", "chest", 1, 2, 8, "A plain robe of undyed linen, the uniform of every apprentice.", INT=1, WIS=1)
armor("apprentice_hood", "an apprentice's hood", "head", 2, 1, 12, "A soft grey hood embroidered with a single silver rune.", INT=1, WIS=1)
armor("silk_gloves", "silk gloves", "hands", 3, 1, 15, "Thin gloves of black silk that never snag a spell.", INT=1, CHA=1)
armor("felt_slippers", "felt slippers", "feet", 3, 1, 15, "Quiet slippers favoured by librarians and thieves alike.", WIS=1, DEX=1)
armor("woven_trousers", "woven trousers", "legs", 4, 2, 20, "Loose trousers of tightly woven blue wool.", INT=1, WIS=1)
armor("copper_focus_ring", "a copper focus ring", "ring", 5, 0, 45, "A copper band etched with a spiral that draws the mind inward.", INT=2, WIS=2)
weapon("wand_of_sparks", "a wand of sparks", 6, (3, 7), 60, "A birch wand that crackles with tiny sparks when gripped.", INT=3, CHA=1)
armor("moonstone_pendant", "a moonstone pendant", "neck", 8, 1, 90, "A milky moonstone that glows faintly at night.", INT=2, WIS=2, CHA=2)
armor("acolyte_robe", "an acolyte's robe", "chest", 8, 5, 95, "A robe of deep blue wool trimmed with silver thread.", INT=2, WIS=3)
armor("crystal_orb", "a crystal orb", "shield", 10, 1, 120, "A palm-sized orb of clear crystal, held in the off hand to focus the will.", INT=3, WIS=3)
armor("spellweave_hood", "a spellweave hood", "head", 10, 3, 115, "A deep hood whose weave shifts colour when magic is near.", INT=3, WIS=2)
weapon("willow_staff", "a willow staff", 12, (7, 13), 200, "A pale, supple staff cut from a sacred willow.", INT=4, WIS=4, CHA=2)
armor("enchanted_gloves", "enchanted gloves", "hands", 12, 3, 140, "Grey gloves whose fingertips glow when a spell is cast.", INT=3, WIS=3)
armor("mystic_leggings", "mystic leggings", "legs", 14, 5, 200, "Leggings of violet cloth stitched with warding sigils.", INT=3, WIS=3)
armor("spellbinder_robe", "a spellbinder's robe", "chest", 14, 8, 260, "A heavy robe whose lining is written with a thousand tiny runes.", INT=4, WIS=4)
armor("runebound_slippers", "runebound slippers", "feet", 16, 4, 240, "Slippers that leave faint glowing runes where they step.", INT=3, WIS=2, DEX=2)
armor("sapphire_ring", "a sapphire ring", "ring", 18, 0, 400, "A ring set with a deep blue sapphire that hums softly.", INT=4, WIS=4)
armor("archivist_robe", "an archivist's robe", "chest", 20, 12, 600, "The formal robe of a master of the Brightwater archives.", INT=6, WIS=6, CHA=2)
armor("starsilk_hood", "a starsilk hood", "head", 22, 7, 550, "A hood of midnight silk sewn with tiny points of starlight.", INT=5, WIS=5)
weapon("wand_of_embers", "a wand of embers", 22, (13, 22), 650, "A wand of charred oak with a glowing coal set in its tip.", INT=7, WIS=4, CHA=3)
armor("tome_of_warding", "a tome of warding", "shield", 24, 5, 800, "A heavy spellbook chained to the wrist, its pages humming with protective wards.", INT=6, WIS=6, CON=2)

# ------------------------------------------------------------------ Hearthdeep (dwarven gear, levels 10-24)
# Sold by Brakka Ironhand (arms and armour) and Tamsin Runecutter (rune-gear for casters).
weapon("dwarven_war_axe", "a dwarven war axe", 12, (9, 16), 160,
       "A broad-bladed axe of dark dwarven steel, its haft wrapped in braided leather.", STR=3, CON=1)
weapon("dwarven_crossbow", "a dwarven crossbow", 14, (10, 17), 240,
       "A compact crossbow with a steel prod and a crank of polished brass.", DEX=4)
weapon("runeforged_hammer", "a runeforged hammer", 16, (11, 19), 320,
       "A warhammer whose head is cut with a single glowing rune of striking.", STR=3, CON=2, WIS=1)
weapon("runecarved_staff", "a runecarved staff", 16, (9, 16), 300,
       "A staff of black mountain ash, carved from end to end with dwarven runes of warding.", INT=5, WIS=5)
weapon("dwarven_greataxe", "a dwarven greataxe", 20, (13, 24), 520,
       "A two-handed axe heavy enough to split a boulder, edged with a strip of mithril.", STR=5, CON=2)
weapon("stonewake_hammer", "the Stonewake Hammer", 21, (15, 25), 700,
       "A maul of living granite torn from the Stonewake itself. It hums when it strikes stone.", STR=5, CON=4)
armor("dwarven_chainmail", "dwarven chainmail", "chest", 12, 12, 220, "Fine, heavy mail of tiny riveted rings.", CON=2)
armor("runestone_ring", "a runestone ring", "ring", 14, 0, 240, "A band of grey stone set with a single carved rune.", INT=3, WIS=3)
armor("dwarven_helm", "a dwarven helm", "head", 16, 8, 260, "A round steel helm with cheek-guards and a braided crest.", CON=2)
armor("dwarven_boots", "dwarven iron boots", "feet", 18, 8, 380, "Heavy hobnailed boots with steel toecaps, made for mountain rock.", CON=2)
armor("runecutter_gloves", "runecutter's gloves", "hands", 18, 4, 380, "Thick gloves whose fingertips are stitched with tiny runes of focus.", INT=4, WIS=3)
armor("deepwool_robe", "a deepwool robe", "chest", 18, 11, 450, "A heavy robe of grey mountain wool, lined with rune-stitched silk.", INT=5, WIS=5)
armor("dwarven_greaves", "dwarven greaves", "legs", 20, 12, 500, "Overlapping plates of dwarven steel that guard the legs.", CON=3)
armor("deepheart_amulet", "the Deepheart Amulet", "neck", 21, 4, 700,
      "A crystal from the deepest seam of Deepdelve, glowing faintly on an iron chain.", CON=4, STR=3, WIS=2)
armor("dwarven_plate", "dwarven plate", "chest", 22, 22, 800, "A full suit of dwarven plate, every rivet stamped with a maker's rune.", CON=4, STR=1)
armor("runed_shield", "a runed dwarven shield", "shield", 22, 15, 700, "A round steel shield with a rune of warding at its boss.", CON=3)
armor("rune_amulet", "a rune amulet", "neck", 22, 3, 650, "A disc of silver-veined stone carved with a rune of the deep.", INT=4, WIS=4, CON=2)
armor("runecutter_boots", "runecutter's boots", "feet", 22, 6, 550, "Soft boots whose soles are carved with runes of sure footing.", INT=3, WIS=3, DEX=2)

# ------------------------------------------------------------------ Silverbough (elven gear, levels 24-36)
# Sold by Ilyra Leafsong (arms and armour) and Caelum Moonweave (caster gear).
weapon("elven_saber", "an elven saber", 24, (17, 28), 750,
       "A slender curved blade of leafsteel, so light it seems to move on its own.", STR=3, DEX=5)
weapon("silverleaf_bow", "a silverleaf bow", 26, (18, 30), 850,
       "A recurved bow of pale wood inlaid with silver leaves along its limbs.", DEX=7, WIS=2)
weapon("dawnwood_staff", "a dawnwood staff", 28, (15, 26), 1050,
       "A staff cut from a tree that only grows where the first light of morning falls.", INT=8, WIS=8)
weapon("elven_glaive", "an elven glaive", 32, (24, 40), 1500,
       "A long-hafted blade of the Silverbough wardens, edged like a crescent moon.", STR=6, DEX=4)
weapon("thornheart", "Thornheart", 33, (25, 42), 1700,
       "A greatsword of living blackwood grown from Rotheart's core. Thorns still sprout along its back.", STR=7, CON=4)
armor("elven_mail", "elven mail", "chest", 26, 22, 900, "A coat of fine leafsteel scales that whispers when you move.", DEX=3, CON=2)
armor("moonweave_robe", "a moonweave robe", "chest", 26, 14, 950, "A robe of silver-grey silk that shimmers like moonlight on water.", INT=6, WIS=6, CHA=2)
armor("leafsteel_helm", "a leafsteel helm", "head", 28, 12, 950, "A tall, narrow elven helm with cheek-guards shaped like leaves.", DEX=2, CON=2)
armor("moonweave_gloves", "moonweave gloves", "hands", 28, 5, 900, "Fingerless gloves of moonweave silk, cool to the touch.", INT=5, WIS=4)
armor("wardens_boots", "warden's boots", "feet", 30, 10, 1200, "Soft-soled boots of the Silverbough wardens, made to walk without a sound.", DEX=4)
armor("silverbark_shield", "a silverbark shield", "shield", 30, 20, 1300, "A kite shield of silver bark over leafsteel, light and very hard.", CON=3, DEX=2)
armor("starleaf_circlet", "a starleaf circlet", "head", 30, 9, 1200, "A circlet of woven silver leaves with a tiny star caught at its brow.", INT=6, WIS=5)
armor("moonweave_leggings", "moonweave leggings", "legs", 30, 8, 1100, "Leggings of silver-grey silk stitched with tiny crescent moons.", INT=5, WIS=5)
armor("wardens_gauntlets", "warden's gauntlets", "hands", 32, 12, 1500, "Leafsteel gauntlets that flex like a second skin.", DEX=4, STR=2)
armor("silverleaf_pendant", "a silverleaf pendant", "neck", 32, 4, 1500, "A single silver leaf that never tarnishes, on a chain of fine elven links.", INT=5, WIS=5, CHA=3)
armor("crown_of_thorns", "the Crown of Thorns", "head", 33, 14, 1800, "A circlet of black thorns cut from Rotheart's crown. It does not draw blood, quite.", CON=4, WIS=4, STR=3)
armor("eldergrove_amulet", "the Amulet of the Eldergrove", "neck", 33, 5, 1900, "An acorn of green crystal that pulses slowly, like a sleeping heart.", CON=3, WIS=5, DEX=3)
armor("leafsteel_greaves", "leafsteel greaves", "legs", 34, 22, 1700, "Elven leg-plates of leafsteel, etched with climbing vines.", DEX=3, CON=3)
armor("moonweave_slippers", "moonweave slippers", "feet", 34, 7, 1500, "Slippers of moonweave that leave no footprints at all.", INT=5, WIS=4, DEX=3)
armor("moonstone_ring", "a Silverbough moonstone ring", "ring", 34, 0, 1600, "A ring of white gold set with a moonstone that glows at dusk.", INT=6, WIS=6)

# ------------------------------------------------------------------ The east: Badlands drops and Sunspire gear (levels 36-48)
# Sunspire gear is sold by Zahir the Bladewright (arms and armour) and Amsa Silkwind (caster gear).
weapon("yellowtooth_flail", "Yellowtooth's Flail", 26, (19, 32), 900,
       "A gnoll warlord's flail: three iron balls on chains, each crusted with old teeth.", STR=6, CON=2)
armor("gnoll_bone_necklace", "a gnoll warlord's necklace", "neck", 26, 4, 950,
      "A necklace of finger bones and yellowed fangs, strung by a gnoll who counted his victims.", STR=3, CON=3, DEX=2)
weapon("sunsteel_scimitar", "a sunsteel scimitar", 38, (28, 47), 2200,
       "A deeply curved blade of golden sunsteel, folded a thousand times in the forges of Sunspire.", STR=5, DEX=7)
armor("desert_silk_robe", "a desert silk robe", "chest", 38, 20, 2100, "Layered robes of saffron and indigo silk, cool in the worst of the sun.", INT=8, WIS=8, CHA=3)
armor("silkwind_turban", "a silkwind turban", "head", 38, 10, 2000, "A turban of fine silk pinned with a sapphire that glows when spells are cast.", INT=7, WIS=6)
armor("oasis_pearl_ring", "an oasis pearl ring", "ring", 38, 0, 2200, "A ring of pale gold set with a pearl from the sacred oasis.", INT=7, WIS=7)
weapon("dune_recurve", "a dune recurve bow", 40, (29, 48), 2400,
       "A short, powerful bow of horn and desert ash, made to be shot from the saddle.", DEX=10, WIS=3)
weapon("sunfire_staff", "a sunfire staff", 40, (21, 35), 2500,
       "A staff of black wood capped with a sun-disc of gold that blazes when it is raised.", INT=11, WIS=11)
armor("sunsteel_mail", "sunsteel mail", "chest", 40, 36, 2500, "Golden scale mail that turns blades and throws back the desert sun.", CON=6, DEX=3)
armor("sunsteel_helm", "a sunsteel helm", "head", 40, 18, 2200, "A spired helm of sunsteel with a veil of fine mail to keep out the sand.", CON=4, STR=2)
armor("sunsteel_greaves", "sunsteel greaves", "legs", 40, 26, 2300, "Greaves of sunsteel engraved with the rays of the sun.", CON=5, STR=2)
armor("sand_strider_boots", "sand-strider boots", "feet", 40, 13, 2200, "Wide-soled boots that carry you over soft sand without sinking.", DEX=5)
armor("silkwind_gloves", "silkwind gloves", "hands", 40, 6, 2100, "Gloves of silk so fine they seem to be made of breeze.", INT=6, WIS=6)
armor("silkwind_trousers", "silkwind trousers", "legs", 40, 10, 2100, "Loose trousers of layered silk, embroidered with stars.", INT=6, WIS=6)
armor("obelisk_amulet", "an amulet of the obelisk", "neck", 40, 6, 2600, "A tiny golden obelisk on a chain, said to be cut from the great obelisk itself.", INT=5, WIS=5, CON=4)
armor("sunsteel_gauntlets", "sunsteel gauntlets", "hands", 42, 15, 2400, "Gauntlets of sunsteel with knuckles shaped like rising suns.", STR=4, DEX=3)
armor("sunburst_shield", "a sunburst shield", "shield", 42, 24, 2500, "A round shield of polished sunsteel that flashes blindingly in the light.", CON=5)
armor("silkwind_slippers", "silkwind slippers", "feet", 42, 8, 2300, "Pointed slippers of embroidered silk that never fill with sand.", INT=6, WIS=5, DEX=3)
armor("sunstone_ring", "a sunstone ring", "ring", 42, 0, 2600, "A heavy gold ring set with an orange stone that is always warm.", STR=4, DEX=4, CON=4)
weapon("crescent_greatsword", "a crescent greatsword", 44, (33, 55), 3200,
       "A huge curved blade of sunsteel, worn across the back by the Sun Guard of Sunspire.", STR=9, DEX=4)
weapon("khopesh_of_ussreth", "the Khopesh of Ussreth", 48, (38, 62), 5500,
       "The hooked sword of the last Sand King, its bronze blade still sharp after three thousand years.", STR=11, DEX=8, CON=5)
weapon("scepter_of_the_sand_kings", "the Scepter of the Sand Kings", 48, (27, 44), 5000,
       "A sceptre of gold and lapis topped with a scarab of black glass, heavy with old and patient magic.", INT=17, WIS=15, CHA=8)
armor("burial_mask", "the Burial Mask of Ussreth", "head", 48, 26, 4800,
      "A golden death-mask with eyes of lapis. Wearing it, you hear the desert wind.", CON=6, STR=4, INT=4, WIS=4)

# ------------------------------------------------------------------ Mythic gear from the Planes of the Gods (level 50)
# Dropped only by the plane bosses and Lord Zek. Stronger than anything else in the world.
weapon("stormcaller_bow", "Stormcaller", 50, (46, 74), 12000,
       "A bow strung with a thread of lightning, taken from the Sky-Warden's own hand.", DEX=16, WIS=6, CON=6)
armor("cloudsilk_robes", "cloudsilk robes", "chest", 50, 30, 11000, "Robes woven from the clouds of the high heavens, weightless and cool.", INT=14, WIS=14, CHA=6)
weapon("wildmother_staff", "the Wildmother's Staff", 50, (30, 50), 12000,
       "A staff of living wood that still puts out leaves in spring.", INT=20, WIS=20, CHA=8)
armor("living_bark_greaves", "living bark greaves", "legs", 50, 36, 11000, "Greaves of bark that grows back over every scratch.", CON=10, STR=6)
weapon("dreadblade", "the Dreadblade", 50, (48, 78), 12500,
       "A black sword that whispers your worst fears to whoever it is pointed at.", STR=14, DEX=10)
armor("mask_of_dread", "the Mask of Dread", "head", 50, 28, 11000, "A faceless mask of black iron. Your enemies see in it whatever they fear most.", STR=6, DEX=6, CON=6)
weapon("lightbearers_oath", "the Lightbearer's Oath", 50, (48, 76), 12500,
       "Stalworth's longsword, its blade engraved with every law of the gods. It shines brightest on the guilty.",
       STR=12, WIS=10, CON=6)
armor("shield_of_judgement", "the Shield of Judgement", "shield", 50, 38, 12000,
      "A tower shield of white steel bearing the scales of justice. Blows that strike it feel judged.", CON=10, WIS=6)
weapon("flameheart_hammer", "Flameheart", 50, (50, 80), 13000,
       "A hammer forged in the heart of the Plane of Fire, its head a captive star.", STR=16, CON=8)
armor("gauntlets_of_the_pyre", "gauntlets of the pyre", "hands", 50, 22, 11000, "Gauntlets of red-gold that burn without heat.", STR=8, DEX=6, CON=4)
weapon("tidecaller", "Tidecaller", 50, (46, 74), 12500,
       "A trident of white coral and pearl. The tide turns when it is raised.", STR=10, DEX=10, WIS=6)
armor("pearl_of_the_deep", "the Pearl of the Deep", "ring", 50, 0, 11000, "A black pearl as big as an eye, set in a ring of sea-silver.", INT=12, WIS=12, CON=4)
armor("mountainheart_shield", "the Mountainheart Shield", "shield", 50, 40, 12000, "A shield cut from the living rock of the Plane of Earth.", CON=12, STR=4)
armor("stonestride_boots", "stonestride boots", "feet", 50, 22, 11000, "Boots of grey stone that weigh nothing on your feet and everything on your enemies'.", CON=8, STR=4)
armor("windwalker_boots", "windwalker boots", "feet", 50, 16, 11000, "Boots of silver feathers. Your feet barely touch the ground.", DEX=12, INT=4, WIS=4)
armor("band_of_four_winds", "the Band of the Four Winds", "ring", 50, 0, 11000, "A ring of four twisted strands of silver, each humming a different wind.", DEX=10, STR=6, CON=6)
weapon("eternity", "Eternity", 50, (55, 88), 20000,
       "The sword of Lord Zek. Its blade shows every moment it has ever cut.",
       STR=12, DEX=12, CON=12, INT=12, WIS=12, CHA=12)
armor("crown_of_zek", "the Crown of Zek", "head", 50, 32, 18000, "A crown of white gold that weighs nothing and holds the light of every dawn.",
      STR=10, DEX=10, CON=10, INT=10, WIS=10, CHA=10)
armor("hourglass_amulet", "the Hourglass Amulet", "neck", 50, 12, 18000, "A tiny hourglass of crystal whose sand runs upward.",
      STR=12, DEX=12, CON=12, INT=12, WIS=12, CHA=12)

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
misc("yeti_fur", "a hank of yeti fur", 50, "Coarse white fur, warm enough to sleep in a snowdrift.")
misc("deep_crystal", "a deep crystal", 80, "A cloudy crystal from the depths of Deepdelve, faintly warm.")
misc("stag_antler", "a greatstag antler", 60, "A branching antler as wide as your outstretched arms.", kind="quest")
misc("blight_heartwood", "a lump of blighted heartwood", 120, "Black, oozing wood that is warm to the touch and smells of rot.")
misc("hyena_hide", "a spotted hyena hide", 20, "A coarse spotted hide that still smells of carrion.")
misc("scorpion_stinger", "a scorpion stinger", 120, "A curved stinger as long as a dagger, its venom sac dried hard.")
misc("desert_glass", "a shard of desert glass", 220, "Green glass fused from sand by some terrible heat, smooth as water.", kind="quest")
misc("ancient_scarab", "an ancient scarab", 400, "A carved scarab of lapis and gold from the tombs of the Sand Kings.")
misc("planar_shard", "a planar shard", 500, "A splinter of another world, humming with a power that does not belong here.")
misc("griffon_feather", "a griffon feather", 70, "A great barred flight feather, longer than your arm.")
misc("winter_wolf_pelt", "a winter wolf pelt", 110, "A thick white pelt that stays cold to the touch.")
misc("frost_shard", "a frost shard", 90, "A shard of ice that never melts.")
misc("elven_relic", "an elven relic", 160, "A small silver figurine of exquisite elven make.")
misc("dragon_scale", "a dragon scale", 300, "A scale the size of a dinner plate, red as embers.")
