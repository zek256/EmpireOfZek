"""The room constructor shared by every region file."""


def R(name, area, desc, exits, spawns=None, npcs=None, safe=False, items=None, level=None, max_aggro=None):
    """max_aggro: how many monsters here may attack on sight (default 1); the rest wait until you
    attack them. Rooms with a boss ignore it: everything in a boss room attacks."""
    return {"name": name, "area": area, "desc": desc, "exits": exits, "spawns": spawns or [],
            "npcs": npcs or [], "safe": safe, "items": items or [], "level": level, "max_aggro": max_aggro}
