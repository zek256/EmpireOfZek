"""Check the game data for broken references. Run from anywhere: python tools/validate.py

Exits with status 1 if any problem is found, so it can gate other scripts.
"""
import os
import sys
from collections import Counter, deque

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from data.abilities import ABILITIES  # noqa: E402
from data.classes import CLASSES  # noqa: E402
from data.items import ITEMS, SLOTS  # noqa: E402
from data.monsters import MONSTERS  # noqa: E402
from data.quests import QUESTS  # noqa: E402
from data.races import RACES  # noqa: E402
from data.rooms import NPCS, RESPAWN_ROOM, ROOMS, START_ROOM  # noqa: E402

OPPOSITE = {"n": "s", "s": "n", "e": "w", "w": "e", "u": "d", "d": "u"}


def main():
    errs, warns = [], []

    # rooms: exits, spawns, npcs, ground items
    for rid, r in ROOMS.items():
        for d, dest in r["exits"].items():
            if d not in OPPOSITE:
                errs.append(f"room {rid}: bad exit direction '{d}'")
            elif dest not in ROOMS:
                errs.append(f"room {rid}: exit {d} -> missing room '{dest}'")
            elif ROOMS[dest]["exits"].get(OPPOSITE[d]) != rid:
                errs.append(f"room {rid}: exit {d} -> {dest} is one-way")
        for mid, n in r["spawns"]:
            if mid not in MONSTERS:
                errs.append(f"room {rid}: spawns missing monster '{mid}'")
        for nid in r["npcs"]:
            if nid not in NPCS:
                errs.append(f"room {rid}: missing npc '{nid}'")
        for iid in r["items"]:
            if iid not in ITEMS:
                errs.append(f"room {rid}: ground item '{iid}' missing")
        gate = r.get("gate") or {}
        for mid in gate.get("kills", []):
            if not MONSTERS.get(mid, {}).get("boss"):
                errs.append(f"room {rid}: gate needs '{mid}', which is not a boss (only bosses are recorded)")
        if gate and "msg" not in gate:
            errs.append(f"room {rid}: gate has no refusal message")
        if r["safe"] and any(MONSTERS.get(mid, {}).get("aggro") for mid, _ in r["spawns"]):
            warns.append(f"room {rid}: safe room spawns aggressive monsters")
    for special in (START_ROOM, RESPAWN_ROOM):
        if special not in ROOMS:
            errs.append(f"START/RESPAWN room '{special}' missing")

    # every room reachable from the start
    seen, queue = {START_ROOM}, deque([START_ROOM])
    while queue:
        for dest in ROOMS[queue.popleft()]["exits"].values():
            if dest in ROOMS and dest not in seen:
                seen.add(dest)
                queue.append(dest)
    for rid in sorted(set(ROOMS) - seen):
        errs.append(f"room {rid}: unreachable from {START_ROOM}")

    # monsters, items, npcs, quests, classes
    for mid, m in MONSTERS.items():
        for iid, chance in m["loot"]:
            if iid not in ITEMS:
                errs.append(f"monster {mid}: loot '{iid}' missing")
            if not 0 < chance <= 1:
                errs.append(f"monster {mid}: loot chance {chance} for '{iid}'")
    for iid, it in ITEMS.items():
        if it["type"] in ("weapon", "armor") and it.get("slot") not in SLOTS:
            errs.append(f"item {iid}: bad slot '{it.get('slot')}'")
    for nid, n in NPCS.items():
        for iid in n.get("shop", []):
            if iid not in ITEMS:
                errs.append(f"npc {nid}: sells missing item '{iid}'")
        for qid in n.get("quests", []):
            if qid not in QUESTS:
                errs.append(f"npc {nid}: missing quest '{qid}'")
            elif QUESTS[qid]["giver"] != nid:
                errs.append(f"quest {qid}: listed by {nid} but giver is {QUESTS[qid]['giver']}")
    for qid, q in QUESTS.items():
        pool = MONSTERS if q["type"] == "kill" else ITEMS
        if q["target"] not in pool:
            errs.append(f"quest {qid}: target '{q['target']}' missing")
        if q["prereq"] and q["prereq"] not in QUESTS:
            errs.append(f"quest {qid}: prereq '{q['prereq']}' missing")
        if q["giver"] not in NPCS:
            errs.append(f"quest {qid}: giver '{q['giver']}' missing")
        for iid in q["reward"].get("items", []):
            if iid not in ITEMS:
                errs.append(f"quest {qid}: reward item '{iid}' missing")
        if q["type"] == "collect" and not any(i == q["target"] for m in MONSTERS.values() for i, _ in m["loot"]):
            errs.append(f"quest {qid}: no monster drops '{q['target']}'")
    for cid, c in CLASSES.items():
        for iid in c["gear"]:
            if iid not in ITEMS:
                errs.append(f"class {cid}: starting gear '{iid}' missing")
    for aid, a in ABILITIES.items():
        if a["cls"] not in CLASSES:
            errs.append(f"ability {aid}: unknown class '{a['cls']}'")

    spawned = {mid for r in ROOMS.values() for mid, _ in r["spawns"]}
    for mid in sorted(set(MONSTERS) - spawned):
        warns.append(f"monster {mid}: never spawns anywhere")

    per_class = Counter(a["cls"] for a in ABILITIES.values())
    print(f"{len(ROOMS)} rooms, {len(MONSTERS)} monsters ({sum(m['boss'] for m in MONSTERS.values())} bosses), "
          f"{len(ITEMS)} items, {len(QUESTS)} quests, {len(RACES)} races, {len(CLASSES)} classes, "
          f"{len(ABILITIES)} abilities ({min(per_class.values())}-{max(per_class.values())} per class)")
    for w in warns:
        print("warning:", w)
    for e in errs:
        print("ERROR:", e)
    print("OK" if not errs else f"{len(errs)} error(s)")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
