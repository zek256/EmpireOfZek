"""Balance simulator: every class fights monsters through the real combat code, with output silenced.

    python tools/balance_sim.py                 # all three reports
    python tools/balance_sim.py fights          # win% / rounds / HP left vs same-level monsters
    python tools/balance_sim.py endurance       # consecutive fights survived without resting
    python tools/balance_sim.py bosses          # boss win% at boss level and boss level +3
    python tools/balance_sim.py endgame         # Planes of the Gods vs level-50 characters with 1/6/11 lives
    options: --n 40 (fights per cell), --levels 1,5,10,20,30,40,50, --seed 3

The simulated player is a human with best-in-slot gear for their level (including boss drops,
so results are optimistic) and a simple AI: heal when low, buff early, otherwise use the
ability with the best expected value. Bosses are fought with 5 healing potions.
Targets the game was tuned to: same-level fights cost ~25-55% HP; endurance 2-6 for most
classes; bosses mostly beatable at level +3. Endgame (monsters above level 50): plane monsters and
plane bosses beatable with 6+ lives; Lord Zek won most of the time (not always) with 11 lives, and
almost never with 6.
"""
import argparse
import os
import random
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

import ui  # noqa: E402

ui.say = ui.out = ui.rule = lambda *a, **k: None  # silence the game

from character import MAX_LEVEL, Character  # noqa: E402
from combat import Combat, potion_drop, resolve_self_effect  # noqa: E402
from data.classes import CLASS_ORDER, CLASSES  # noqa: E402
from data.items import ITEMS, SLOTS  # noqa: E402
from data.monsters import MONSTERS  # noqa: E402
from game import Game  # noqa: E402
from world import MonsterInstance  # noqa: E402

DEFAULT_LEVELS = [1, 3, 5, 8, 12, 16, 20, 25, 30, 35, 40, 45, 50]


def best_gear(p):
    main = {p.cdata["attack_stat"], p.cdata["mana_stat"]}

    def score(it):
        sc = it.get("armor", 0) * 1.5 + sum(v * (2 if s in main else 0.7) for s, v in it["stats"].items())
        if it["type"] == "weapon":
            sc += sum(it["dmg"]) * (1.5 if p.cdata["mana"] < 5 else 0.5)
        return sc

    for slot in SLOTS:
        cands = [i for i in ITEMS.values() if i.get("slot") == slot and i["level"] <= p.level]
        if cands:
            p.equipment[slot] = max(cands, key=score)["id"]


def nearby_monsters(level):
    """The three non-boss monster types closest to `level`."""
    cands = sorted((m for m in MONSTERS.values() if not m["boss"]), key=lambda m: abs(m["level"] - level))
    return [m["id"] for m in cands[:3]]


def setup(cls, level):
    p = Character("Sim", "human", cls)
    p.level = level
    best_gear(p)
    p.hp, p.mana = p.max_hp, p.max_mana
    g = Game(p)
    g.room_id = "cellar"
    g.check_aggro = lambda: None
    return g, p


def fight(g, p, mid, potions=0, max_rounds=60):
    """One fight to the death through the real Combat class. Returns (won, rounds, hp_fraction_left)."""
    room = g.room
    room.monsters = []
    mon = MonsterInstance(mid)
    room.monsters.append(mon)
    for ab in p.usable_abilities():  # summon a pet before the pull, paying its cost
        summon = [e for e in ab["effects"] if e["type"] == "summon"]
        if summon and not p.pet and p.mana >= p.mana_cost(ab):
            p.mana -= p.mana_cost(ab)
            resolve_self_effect(g, ab, summon[0])
    g.combat = Combat(g, [mon])
    pot = next(i for i in iter(lambda: potion_drop(mon.level), None) if i.endswith("healing_potion"))
    weapon_avg = lambda: sum(p.weapon_range()) / 2  # noqa: E731
    rounds = 0
    while g.combat and not g.combat.over and rounds < max_rounds:
        rounds += 1
        if p.has_effect("stun"):
            g.combat.pass_turn()
            continue
        usable = [a for a in p.usable_abilities() if a["id"] not in p.cooldowns
                  and (a["kind"] != "spell" or p.mana_cost(a) <= p.mana)]
        heals = [a for a in usable if a["target"] == "self"
                 and any(e["type"] in ("heal", "heal_pct", "hot") for e in a["effects"])]
        active = {e.get("name") for e in p.effects}
        buffs = [a for a in usable if a["target"] == "self"
                 and any(e["type"] in ("buff", "shield") for e in a["effects"])
                 and not any(e.get("name") in active for e in a["effects"] if e["type"] == "buff")]
        offense = [a for a in usable if a["target"] != "self"]

        def value(a):
            sc = 0
            for e in a["effects"]:
                if e["type"] == "weapon":
                    sc += weapon_avg() * e["mult"]
                elif e["type"] in ("damage", "drain"):
                    sc += p.power(e)
                elif e["type"] == "dot" and not any(x.get("name") == e["name"] for x in mon.effects):
                    sc += p.power(e) * e["turns"] * 0.6
                elif e["type"] == "stun" and not mon.is_stunned():
                    sc += weapon_avg() * 0.8
                elif e["type"] == "weaken" and not any(x.get("name") == e["name"] for x in mon.effects):
                    sc += weapon_avg() * 0.8
            return sc

        if p.hp < p.max_hp * 0.3 and not heals and potions:
            potions -= 1
            p.heal(ITEMS[pot]["heal"])
            g.combat.pass_turn()
        elif p.hp < p.max_hp * 0.4 and heals:
            g.combat.player_ability(max(heals, key=lambda a: a["level"]), None)
        elif buffs and rounds <= 2:
            g.combat.player_ability(max(buffs, key=lambda a: a["level"]), None)
        else:
            best = max(offense, key=value) if offense else None
            if best and value(best) > weapon_avg():
                g.combat.player_ability(best, mon)
            else:
                g.combat.player_attack(mon)
    won = mon.hp <= 0
    return won, rounds, (max(0, p.hp) / p.max_hp if won else 0.0)


def report_fights(levels, n):
    print("win% / avg rounds / avg HP% left, vs same-level monsters")
    print("lvl  " + " ".join("{:>13}".format(c[:13]) for c in CLASS_ORDER))
    for L in levels:
        mids = nearby_monsters(L)
        row = []
        for cls in CLASS_ORDER:
            res = []
            for _ in range(n):
                g, p = setup(cls, L)
                res.append(fight(g, p, random.choice(mids)))
            wins = [r for r in res if r[0]]
            row.append("{:>3.0f}%{:>4.1f}r{:>3.0f}%".format(
                100 * len(wins) / n, sum(r[1] for r in res) / n,
                100 * sum(r[2] for r in wins) / max(1, len(wins))))
        print("{:>3}  ".format(L) + " ".join("{:>13}".format(x) for x in row))


def report_endurance(levels, n, cap=8):
    print("consecutive same-level fights survived (3 ticks of regen between, cap {})".format(cap))
    print("lvl  " + " ".join("{:>7}".format(c[:7]) for c in CLASS_ORDER))
    for L in levels:
        mids = nearby_monsters(L)
        row = []
        for cls in CLASS_ORDER:
            total = 0
            for _ in range(n):
                g, p = setup(cls, L)
                survived = 0
                while survived < cap:
                    won, _, _ = fight(g, p, random.choice(mids))
                    if not won or p.hp <= 0:
                        break
                    survived += 1
                    for _ in range(3):
                        g.world_tick()
                total += survived
            row.append("{:>7.1f}".format(total / n))
        print("{:>3}  ".format(L) + " ".join(row))


def report_bosses(n):
    print("boss win% with 5 healing potions: at boss level / at boss level +3")
    print("{:<30}".format("") + " ".join("{:>9}".format(c[:9]) for c in CLASS_ORDER))
    for b in (m for m in MONSTERS.values() if m["boss"] and m["level"] <= MAX_LEVEL + 2):
        row = []
        for cls in CLASS_ORDER:
            rates = []
            for offset in (0, 3):
                L = min(50, b["level"] + offset)
                wins = 0
                for _ in range(n):
                    g, p = setup(cls, L)
                    wins += fight(g, p, b["id"], potions=5)[0]
                rates.append(100 * wins / n)
            row.append("{:>3.0f}/{:<3.0f}".format(*rates))
        print("{:<30}".format(b["name"][:29]) + " ".join("{:>9}".format(x) for x in row))


ENDGAME_LIVES = (1, 6, 11)


def setup_lives(cls, lives):
    """A level-50 character in `cls` who has lived `lives` classes in all (this one included)."""
    g, p = setup(cls, MAX_LEVEL)
    for other in [c for c in CLASS_ORDER if c != cls][:lives - 1]:
        p.past_lives.append({"cls": other, "gains": {s: v * (MAX_LEVEL - 1)
                                                     for s, v in CLASSES[other]["gains"].items()}})
    best_gear(p)
    p.hp, p.mana = p.max_hp, p.max_mana
    return g, p


def report_endgame(n):
    """Planes of the Gods (monsters above level 50): win% for characters with 1, 6 and 11 lives."""
    print("level-50 win% vs the planes, averaged over classes (bosses with 5 potions): "
          + " / ".join("{} li{}".format(x, "fe" if x == 1 else "ves") for x in ENDGAME_LIVES)
          + "   [worst class at 11 lives]")
    mids = sorted((m for m in MONSTERS.values() if m["level"] > MAX_LEVEL), key=lambda m: (m["boss"], m["level"]))
    for m in mids:
        rates, worst = [], 100
        for lives in ENDGAME_LIVES:
            total = 0
            for cls in CLASS_ORDER:
                wins = sum(fight(*setup_lives(cls, lives), m["id"], potions=5 if m["boss"] else 0)[0]
                           for _ in range(n))
                total += wins
                if lives == ENDGAME_LIVES[-1]:
                    worst = min(worst, 100 * wins / n)
            rates.append(100 * total / (n * len(CLASS_ORDER)))
        print("{:<34} L{}  ".format(m["name"][:33], m["level"])
              + " / ".join("{:>3.0f}%".format(r) for r in rates) + "   [{:.0f}%]".format(worst))


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("report", nargs="?", default="all", choices=["all", "fights", "endurance", "bosses", "endgame"])
    ap.add_argument("--n", type=int, default=30, help="simulated fights per table cell")
    ap.add_argument("--levels", default=",".join(map(str, DEFAULT_LEVELS)), help="comma-separated levels")
    ap.add_argument("--seed", type=int, default=3)
    opts = ap.parse_args()
    random.seed(opts.seed)
    levels = [int(x) for x in opts.levels.split(",")]
    if opts.report in ("all", "fights"):
        report_fights(levels, opts.n)
        print()
    if opts.report in ("all", "endurance"):
        report_endurance(levels, opts.n)
        print()
    if opts.report in ("all", "bosses"):
        report_bosses(opts.n)
        print()
    if opts.report in ("all", "endgame"):
        report_endgame(opts.n)


if __name__ == "__main__":
    main()
