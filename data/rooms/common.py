"""The room constructor shared by every region file."""


def R(name, area, desc, exits, spawns=None, npcs=None, safe=False, items=None, level=None, max_aggro=None,
      gate=None):
    """max_aggro: how many monsters here may attack on sight (default 1); the rest wait until you
    attack them. Rooms with a boss ignore it: everything in a boss room attacks.

    gate: a condition for entering the room, checked by Game.gate_block, with a "msg" shown on refusal:
      {"kills": [boss ids], "msg": ...}       - the character must have killed every listed boss
      {"all_classes": True, "msg": ...}       - every class lived to level 50 (past lives + current)
    """
    return {"name": name, "area": area, "desc": desc, "exits": exits, "spawns": spawns or [],
            "npcs": npcs or [], "safe": safe, "items": items or [], "level": level, "max_aggro": max_aggro,
            "gate": gate}
