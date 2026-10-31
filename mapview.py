"""Room grid layout (shared with tools/draw_map.py) and the text maps behind 'map' and 'automap'.

Rooms are placed on a grid by following exits from the town square: north is up, and up/down
steps diagonally, so the world stays flat and stairs are shown as ^ and v markers. Areas in
INSETS (dungeons below the surface, realms above it) would overlap surface rooms, so each is
laid out on its own grid. A text map only ever shows one layer: the surface or one inset.
"""
import shutil
from collections import deque

import ui
from data.rooms import NPCS, ROOMS, START_ROOM

STEP = {"n": (0, -1), "s": (0, 1), "e": (1, 0), "w": (-1, 0), "u": (1, -1), "d": (-1, 1)}
INSETS = [  # (label, areas drawn together, the room that leads in from the surface)
    ("Crypt of Varnoth", {"Crypt of Varnoth"}, "crypt_entry"),
    ("Deepdelve Mine", {"Deepdelve Mine"}, "deepdelve_foot"),
    ("Tomb of the Sand Kings", {"Tomb of the Sand Kings"}, "tomb_antechamber"),
    ("Planes of the Gods", {"Threshold of the Gods", "Plane of Sky", "Plane of Growth", "Plane of Fear",
                            "Plane of Justice", "Plane of Fire", "Plane of Water", "Plane of Earth",
                            "Plane of Air"}, "threshold_stair"),
    ("Plane of Time", {"Plane of Time"}, "time_gate"),  # above the Threshold, so drawn on its own
]

LEGEND = [("#", "you", "bmagenta"), ("$", "shop", "yellow"), ("!", "quest", "byellow"),
          ("?", "hand in", "byellow"), ("*", "boss", "bred"), ("^ v", "stairs", "bcyan")]


def walk(start, areas):
    """Grid positions of every room reachable from `start` without leaving `areas`."""
    pos = {start: (0, 0)}
    q = deque([start])
    while q:
        r = q.popleft()
        x, y = pos[r]
        for d, t in ROOMS[r]["exits"].items():
            if t not in pos and ROOMS[t]["area"] in areas:
                dx, dy = STEP[d]
                pos[t] = (x + dx, y + dy)
                q.append(t)
    taken = {}
    for r, p in pos.items():
        if p in taken:
            raise ValueError("Rooms {} and {} land on the same grid square; adjust the layout.".format(taken[p], r))
        taken[p] = r
    return pos


def layout():
    """Returns {room: (x, y)} and a list of (label, rooms, entry, surface room) for the insets.
    Insets are shifted to the right of the surface so the positions never collide."""
    inset_areas = set().union(*(areas for _, areas, _ in INSETS))
    pos = walk(START_ROOM, {r["area"] for r in ROOMS.values()} - inset_areas)
    next_x = max(x for x, _ in pos.values()) + 2
    insets = []
    for label, areas, entry in INSETS:
        local = walk(entry, areas)
        outside = next(t for t in ROOMS[entry]["exits"].values() if ROOMS[t]["area"] not in areas)
        # line the entry up with the surface room it hangs from, to the right of everything so far
        dx = next_x - min(x for x, _ in local.values())
        dy = pos[outside][1] - local[entry][1]
        for r, (x, y) in local.items():
            pos[r] = (x + dx, y + dy)
        next_x += max(x for x, _ in local.values()) - min(x for x, _ in local.values()) + 2
        insets.append((label, set(local), entry, outside))
    missing = set(ROOMS) - set(pos)
    if missing:
        raise ValueError("Rooms not reached: " + ", ".join(sorted(missing)))
    return pos, insets


_grid = None  # (pos, {room: layer}, {(x, y): room}), built on first use


def grid():
    global _grid
    if _grid is None:
        pos, insets = layout()
        layer = {r: None for r in pos}
        for label, rooms, _, _ in insets:
            for r in rooms:
                layer[r] = label
        _grid = pos, layer, {p: r for r, p in pos.items()}
    return _grid


def marker(game, rid):
    """The one-character note shown inside a room's brackets, with its colour."""
    if rid == game.room_id:
        return "#", "bmagenta"
    room = game.world.room(rid)
    if any(m.boss for m in room.living()):
        return "*", "bred"
    states = [game.quest_state(q) for n in room.npcs for q in NPCS[n].get("quests", [])]
    if "ready" in states:
        return "?", "byellow"
    if "available" in states:
        return "!", "byellow"
    if any(NPCS[n].get("shop") for n in room.npcs):
        return "$", "yellow"
    if "u" in room.exits:
        return "^", "bcyan"
    if "d" in room.exits:
        return "v", "bcyan"
    return " ", None


def render(game, cols, rows):
    """Lines of a map centred on the player, at most `cols` x `rows` rooms. Rooms of the current
    area are drawn in green, other areas on the same layer in grey."""
    pos, layer, at = grid()
    here = game.room_id
    px, py = pos[here]
    # frame the current area, cropped around the player if it doesn't fit
    area = [pos[r] for r in pos if ROOMS[r]["area"] == ROOMS[here]["area"] and layer[r] == layer[here]]
    x0, x1 = min(x for x, _ in area) - 1, max(x for x, _ in area) + 1
    y0, y1 = min(y for _, y in area) - 1, max(y for _, y in area) + 1
    if x1 - x0 + 1 > cols:
        x0 = min(max(x0, px - cols // 2), x1 - cols + 1)
        x1 = x0 + cols - 1
    if y1 - y0 + 1 > rows:
        y0 = min(max(y0, py - rows // 2), y1 - rows + 1)
        y1 = y0 + rows - 1

    def room_at(x, y):
        r = at.get((x, y))
        return r if r and layer[r] == layer[here] else None

    # trim empty edges (the margin around the area is often bare)
    shown = [(x, y) for x in range(x0, x1 + 1) for y in range(y0, y1 + 1) if room_at(x, y)]
    x0, x1 = min(x for x, _ in shown), max(x for x, _ in shown)
    y0, y1 = min(y for _, y in shown), max(y for _, y in shown)

    lines = []
    for y in range(y0, y1 + 1):
        top, below = [], []
        for x in range(x0, x1 + 1):
            r = room_at(x, y)
            if not r:
                top.append("    ")
                below.append("    ")
                continue
            ex = ROOMS[r]["exits"]
            wall = "green" if ROOMS[r]["area"] == ROOMS[here]["area"] else "grey"
            ch, color = marker(game, r)
            east = "-" if x < x1 and ex.get("e") == room_at(x + 1, y) and "e" in ex else " "
            south = "|" if y < y1 and ex.get("s") == room_at(x, y + 1) and "s" in ex else " "
            top.append(ui.c("[", wall) + (ui.c(ch, color, "bold") if color else ch) + ui.c("]", wall) + east)
            below.append(" " + south + "  ")
        lines.append("".join(top).rstrip())
        if y < y1:
            lines.append("".join(below).rstrip())
    while lines and not lines[-1].strip():
        lines.pop()
    return lines


def legend():
    return "  ".join(ui.c(ch, color, "bold") + " " + word for ch, word, color in LEGEND)


def full_map(game):
    """The 'map' command: as much of the current area as fits in the terminal."""
    cols = max(5, ui.width() // 4)
    rows = max(3, (shutil.get_terminal_size((88, 24)).lines - 6) // 2 + 1)
    return render(game, cols, rows)


def mini_map(game):
    """The automap under a room description: two rooms in every direction."""
    return render(game, 5, 5)
