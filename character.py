"""The player character: stats, levelling, abilities, equipment and rebirth."""
import random

from data.abilities import ABILITIES
from data.classes import CLASSES, STATS
from data.items import ARMOR_TIERS, FREE_KINDS, ITEMS, SLOTS
from data.races import RACES

MAX_LEVEL = 50


def xp_for_level(level):
    """Experience needed to advance from `level` to `level + 1` (the same in every life)."""
    return int(100 * level ** 1.5)


class Pet:
    def __init__(self, name, max_hp, dmg_min, dmg_max, desc=""):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.dmg_min = dmg_min
        self.dmg_max = dmg_max
        self.desc = desc

    def to_dict(self):
        return dict(self.__dict__)

    @classmethod
    def from_dict(cls, d):
        p = cls(d["name"], d["max_hp"], d["dmg_min"], d["dmg_max"], d.get("desc", ""))
        p.hp = d["hp"]
        return p


class Character:
    def __init__(self, name, race, cls):
        self.name = name
        self.race = race
        self.cls = cls
        self.level = 1
        self.xp = 0
        self.gold = 20
        self.past_lives = []  # [{"cls": id, "gains": {stat: amount}}]
        self.inventory = []   # item ids, duplicates allowed
        self.equipment = {s: None for s in SLOTS}
        self.quests = {}      # quest id -> {"status": "active"|"done", "count": n}
        self.effects = []     # buffs, shields, hots, dots, stuns
        self.cooldowns = {}   # ability id -> rounds remaining
        self.pet = None
        self.aliases = {}     # player-defined shortcut -> command line
        self.automap = False  # show a small map under every room description
        self.kills = 0
        self.deaths = 0
        self.boss_kills = []  # boss ids this character has ever slain (across all lives)
        for iid in CLASSES[cls]["gear"]:
            self.equipment[ITEMS[iid]["slot"]] = iid
        self.inventory += ["minor_healing_potion"] * 3
        self.hp = self.max_hp
        self.mana = self.max_mana

    # ------------------------------------------------------------------ data
    @property
    def cdata(self):
        return CLASSES[self.cls]

    @property
    def rdata(self):
        return RACES[self.race]

    def perk(self, key, default):
        return self.rdata["perks"].get(key, default)

    @property
    def class_name(self):
        return self.cdata["name"]

    @property
    def race_name(self):
        return self.rdata["name"]

    # ------------------------------------------------------------------ stats
    def rebirth_bonus(self, stat, level=None):
        """Permanent bonus from past lives, phased in as the current life levels up."""
        level = self.level if level is None else level
        total = sum(life["gains"].get(stat, 0) for life in self.past_lives)
        return int(total * level / MAX_LEVEL)

    def base_stat(self, stat, level=None):
        level = self.level if level is None else level
        c = self.cdata
        return (self.rdata["stats"][stat] + c["start"].get(stat, 0)
                + c["gains"].get(stat, 0) * (level - 1) + self.rebirth_bonus(stat, level))

    def gear_stat(self, stat):
        return sum(ITEMS[i]["stats"].get(stat, 0) for i in self.equipment.values() if i)

    def stat(self, stat):
        return self.base_stat(stat) + self.gear_stat(stat)

    def buff_mod(self, key):
        return sum(e.get("mods", {}).get(key, 0) for e in self.effects if e["type"] == "buff")

    @property
    def max_hp(self):
        c = self.cdata
        hp = 10 + (c["hp"] + 3) * self.level + self.stat("CON") * self.level * 0.2
        return int(hp * self.perk("hp_mult", 1.0))

    @property
    def max_mana(self):
        c = self.cdata
        mana = 15 + c["mana"] * self.level + self.stat(c["mana_stat"]) * self.level * 0.1
        return int(mana * self.perk("mana_mult", 1.0))

    @property
    def armor(self):
        a = sum(ITEMS[i].get("armor", 0) for i in self.equipment.values() if i)
        return int(a + self.stat("DEX") / 10 + self.buff_mod("armor"))

    @property
    def crit_chance(self):
        return min(0.35, 0.05 + self.stat("DEX") / 1000 + self.perk("crit", 0))

    @property
    def dodge(self):
        base = min(0.25, 0.03 + self.stat("DEX") / 1500 + self.perk("dodge", 0))
        return min(0.6, base + self.buff_mod("dodge"))

    @property
    def damage_mult(self):
        return self.perk("dmg_mult", 1.0) * (1 + self.buff_mod("damage_pct"))

    def weapon_range(self):
        w = self.equipment.get("weapon")
        lo, hi = ITEMS[w]["dmg"] if w else (1, 3)
        bonus = self.stat(self.cdata["attack_stat"]) * 0.35 + self.level * 0.5
        return int(lo + bonus), int(hi + bonus)

    def roll_weapon(self, mult=1.0):
        lo, hi = self.weapon_range()
        return random.randint(lo, hi) * mult * self.damage_mult

    def power(self, eff):
        """Raw magnitude for a scaling ability effect."""
        return eff["base"] + eff["lvl"] * self.level + eff["scale"] * self.stat(eff["stat"])

    # ------------------------------------------------------------------ xp
    @property
    def xp_needed(self):
        return xp_for_level(self.level)

    def gain_xp(self, amount):
        """Add experience and handle level-ups. Returns a list of message lines."""
        msgs = []
        if self.level >= MAX_LEVEL:
            return msgs
        amount = int(amount * self.perk("xp_mult", 1.0))
        self.xp += amount
        xp_needed = xp_for_level(self.level)
        if xp_needed > 0:
            percent = amount / xp_needed * 100
            msgs.append(("You gain {} experience. ({:.1f}% of your level)".format(amount, percent), "bcyan"))
        else:
            msgs.append(("You gain {} experience.".format(amount), "bcyan"))
        while self.level < MAX_LEVEL and self.xp >= self.xp_needed:
            self.xp -= self.xp_needed
            msgs += self.level_up()
        if self.level >= MAX_LEVEL:
            self.xp = 0
        return msgs

    def level_up(self):
        before = {s: self.stat(s) for s in STATS}
        hp0, mana0 = self.max_hp, self.max_mana
        self.level += 1
        msgs = [("", None),
                ("*** You have reached level {}! ***".format(self.level), "byellow"),
                ]
        gains = ["{} +{}".format(s, self.stat(s) - before[s]) for s in STATS if self.stat(s) > before[s]]
        msgs.append(("Your training as a {} pays off: {}.".format(self.class_name, ", ".join(gains)), "yellow"))
        msgs.append(("Max HP +{}, Max Mana +{}.".format(self.max_hp - hp0, self.max_mana - mana0), "yellow"))
        self.hp, self.mana = self.max_hp, self.max_mana
        for ab in self.abilities_unlocked_at(self.level):
            tag = "spell" if ab["kind"] == "spell" else "ability"
            origin = "" if ab["cls"] == self.cls else " (remembered from a past life as a {})".format(
                CLASSES[ab["cls"]]["name"])
            msgs.append(("You have learned the {} {}!{}".format(tag, ab["name"], origin), "bmagenta"))
        if self.level == MAX_LEVEL:
            msgs.append(("You have reached the pinnacle of mortal power. You may now REBIRTH.", "bmagenta"))
        return msgs

    # ------------------------------------------------------------------ abilities
    def lived_classes(self):
        return {self.cls} | {life["cls"] for life in self.past_lives}

    def known_abilities(self):
        """Every ability from the current and past classes, learned or not yet, sorted by level."""
        classes = self.lived_classes()
        abs_ = [a for a in ABILITIES.values() if a["cls"] in classes]
        return sorted(abs_, key=lambda a: (a["level"], a["cls"] != self.cls, a["name"]))

    def usable_abilities(self):
        return [a for a in self.known_abilities() if a["level"] <= self.level]

    def abilities_unlocked_at(self, level):
        return [a for a in self.known_abilities() if a["level"] == level]

    def mana_cost(self, ab):
        return int(round(ab["cost"] * (1 + 0.1 * (self.level - 1))))

    def tick_cooldowns(self):
        for k in list(self.cooldowns):
            self.cooldowns[k] -= 1
            if self.cooldowns[k] <= 0:
                del self.cooldowns[k]

    # ------------------------------------------------------------------ effects
    def add_effect(self, eff):
        # refresh same-named effects instead of stacking them
        self.effects = [e for e in self.effects if e.get("name") != eff.get("name")]
        self.effects.append(eff)

    def has_effect(self, etype):
        return any(e["type"] == etype for e in self.effects)

    def heal(self, amount):
        amount = max(0, int(amount))
        before = self.hp
        self.hp = min(self.max_hp, self.hp + amount)
        return self.hp - before

    def absorb(self, dmg):
        """Let shields soak damage. Returns remaining damage."""
        for e in self.effects:
            if e["type"] == "shield" and dmg > 0:
                soak = min(e["value"], dmg)
                e["value"] -= soak
                dmg -= soak
        self.effects = [e for e in self.effects if not (e["type"] == "shield" and e["value"] <= 0)]
        return dmg

    # ------------------------------------------------------------------ items
    def armor_tier(self):
        """Index into ARMOR_TIERS of the heaviest armor any of this character's lives could wear."""
        return max(ARMOR_TIERS.index(CLASSES[c]["armor"]) for c in self.lived_classes())

    def trained_for(self, iid):
        """Whether the current class or a past life could use this item (level aside). Returns (ok, why)."""
        it = ITEMS[iid]
        kind, lived = it["kind"], self.lived_classes()
        if kind in FREE_KINDS:
            return True, ""
        if it["type"] == "weapon":
            if any(kind in CLASSES[c]["weapons"] for c in lived):
                return True, ""
            return False, "You have no training with {} weapons.".format(
                "two-handed" if kind == "two-handed" else kind)
        if kind == "shield":
            if any(CLASSES[c]["shield"] for c in lived):
                return True, ""
            return False, "You have no training with shields."
        if ARMOR_TIERS.index(kind) <= self.armor_tier():
            return True, ""
        return False, "You have no training in {} armor.".format(kind)

    def can_equip(self, iid):
        it = ITEMS[iid]
        if it["type"] not in ("weapon", "armor"):
            return False, "You can't equip that."
        ok, why = self.trained_for(iid)
        if not ok:
            return False, why
        if it["level"] > self.level:
            return False, "You must be level {} to use {}.".format(it["level"], it["name"])
        return True, ""

    def drop_untrained(self):
        """Move equipped items this character isn't trained for into the inventory (older saves).
        Returns the item ids moved."""
        moved = [iid for iid in self.equipment.values() if iid and not self.trained_for(iid)[0]]
        for iid in moved:
            self.unequip(ITEMS[iid]["slot"])
        return moved

    def equip(self, iid):
        ok, why = self.can_equip(iid)
        if not ok:
            return False, why
        slot = ITEMS[iid]["slot"]
        self.inventory.remove(iid)
        old = self.equipment.get(slot)
        if old:
            self.inventory.append(old)
        self.equipment[slot] = iid
        self.clamp()
        return True, old

    def unequip(self, slot):
        iid = self.equipment.get(slot)
        if iid:
            self.equipment[slot] = None
            self.inventory.append(iid)
            self.clamp()
        return iid

    def clamp(self):
        self.hp = min(self.hp, self.max_hp)
        self.mana = min(self.mana, self.max_mana)

    # ------------------------------------------------------------------ rebirth
    def rebirth(self, new_cls):
        old = self.cls
        gains = {s: v * (MAX_LEVEL - 1) for s, v in CLASSES[old]["gains"].items()}
        self.past_lives.append({"cls": old, "gains": gains})
        self.cls = new_cls
        self.level = 1
        self.xp = 0
        self.effects = []
        self.cooldowns = {}
        self.pet = None
        removed = []
        for slot, iid in self.equipment.items():
            if iid and ITEMS[iid]["level"] > 1:
                self.equipment[slot] = None
                self.inventory.append(iid)
                removed.append(iid)
        self.hp, self.mana = self.max_hp, self.max_mana
        return removed

    # ------------------------------------------------------------------ persistence
    def to_dict(self):
        d = {k: v for k, v in self.__dict__.items() if k != "pet"}
        d["pet"] = self.pet.to_dict() if self.pet else None
        return d

    @classmethod
    def from_dict(cls, d):
        ch = cls.__new__(cls)
        ch.__dict__.update({k: v for k, v in d.items() if k != "pet"})
        ch.pet = Pet.from_dict(d["pet"]) if d.get("pet") else None
        for s in SLOTS:
            ch.equipment.setdefault(s, None)
        ch.__dict__.setdefault("aliases", {})  # saves from before aliases existed
        ch.__dict__.setdefault("boss_kills", [])
        ch.__dict__.setdefault("automap", False)
        return ch

    def mastered_classes(self):
        """Classes lived all the way to the level cap: every past life, plus this one if it is maxed."""
        done = {life["cls"] for life in self.past_lives}
        if self.level >= MAX_LEVEL:
            done.add(self.cls)
        return done
