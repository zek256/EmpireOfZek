"""Draw an SVG map of every room. Run from anywhere: python tools/draw_map.py [out.svg]

Writes map.svg in the game folder by default; open it in any web browser.
Rooms are placed on a grid by following exits from the town square (north is up,
up/down are drawn diagonally). Areas listed in INSETS (dungeons below the surface, realms
above it) would sit on top of surface rooms, so each is laid out on its own grid and drawn
in a framed box to the right of the surface map.
"""
import os
import sys
import textwrap
from collections import deque
from html import escape

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, ROOT)

from data.monsters import MONSTERS  # noqa: E402
from data.rooms import ROOMS, START_ROOM  # noqa: E402

STEP = {"n": (0, -1), "s": (0, 1), "e": (1, 0), "w": (-1, 0), "u": (1, -1), "d": (-1, 1)}
INSETS = [  # (label, areas drawn together, the room that leads in from the surface)
    ("Crypt of Varnoth", {"Crypt of Varnoth"}, "crypt_entry"),
    ("Deepdelve Mine", {"Deepdelve Mine"}, "deepdelve_foot"),
    ("Tomb of the Sand Kings", {"Tomb of the Sand Kings"}, "tomb_antechamber"),
    ("Planes of the Gods", {"Threshold of the Gods", "Plane of Sky", "Plane of Growth", "Plane of Fear",
                            "Plane of Fire", "Plane of Water", "Plane of Earth", "Plane of Air",
                            "Plane of Time"}, "threshold_stair"),
]

COLORS = {  # area: (fill, border)
    "Brightwater": ("#3a3a46", "#c9b67a"), "Greenmeadow": ("#2f4a2a", "#8fc46a"),
    "Whispering Woods": ("#1f3d2c", "#5fae7a"), "The Northlands": ("#3b3f47", "#a7b0bd"),
    "Barrowfield": ("#3d3530", "#a89380"), "Crypt of Varnoth": ("#33293d", "#a98bd0"),
    "The Mirefen": ("#2e3b33", "#7fa58c"), "Ironspine Mountains": ("#363c45", "#8fb3d9"),
    "Ruins of Elandor": ("#2c3445", "#9fb0e8"), "Ashen Peaks": ("#47271f", "#e88a5a"),
    "Westmarch": ("#3d3a26", "#d2b55b"), "Rimefells": ("#3a4048", "#dde6ee"),
    "Hearthdeep": ("#45332a", "#e0a070"), "Deepdelve Mine": ("#243a3a", "#6fc7c0"),
    "Eldergrove": ("#1b3324", "#6fcf86"), "Silverbough": ("#38362a", "#f0e2a0"),
    "Dustway": ("#3f3a33", "#c8b89a"), "Redrock Badlands": ("#4a2a22", "#e07a5a"),
    "Scorchsands": ("#463c22", "#f2c45a"), "Sunspire": ("#40372a", "#ffe08a"),
    "Tomb of the Sand Kings": ("#2a2630", "#c9a0e0"),
    "Threshold of the Gods": ("#3a3a40", "#fff4c8"), "Plane of Sky": ("#2a3a4a", "#a8d8ff"),
    "Plane of Growth": ("#1e3a1e", "#8cf08c"), "Plane of Fear": ("#2a1e2e", "#c080d0"),
    "Plane of Fire": ("#4a1e14", "#ff8050"), "Plane of Water": ("#14304a", "#60b0ff"),
    "Plane of Earth": ("#3a3020", "#c8a060"), "Plane of Air": ("#30384a", "#e0f0ff"),
    "Plane of Time": ("#3a3424", "#ffd870"),
}
BOSS_RED = "#ff5a4a"
CW, CH = 170, 92           # grid cell size
BW, BH = 140, 60           # room box size
PAD, LEGEND_W = 40, 260


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
            sys.exit("Rooms {} and {} land on the same grid square; adjust the layout.".format(taken[p], r))
        taken[p] = r
    return pos


def layout():
    """Returns {room: (x, y)} and a list of (label, rooms, entry, surface room) for the insets."""
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
        sys.exit("Rooms not reached: " + ", ".join(sorted(missing)))
    return pos, insets


def draw(pos, insets):
    xs = [p[0] for p in pos.values()]
    ys = [p[1] for p in pos.values()]
    minx, miny = min(xs), min(ys)
    W = (max(xs) - minx + 1) * CW + 2 * PAD + LEGEND_W
    H = (max(ys) - miny + 1) * CH + 2 * PAD + 40

    def ctr(r):
        x, y = pos[r]
        return PAD + (x - minx) * CW + CW / 2, PAD + 40 + (y - miny) * CH + CH / 2

    out = ['<svg xmlns="http://www.w3.org/2000/svg" width="{0}" height="{1}" viewBox="0 0 {0} {1}" '
           'font-family="Georgia, serif">'.format(W, H),
           '<rect width="100%" height="100%" fill="#16161c"/>',
           '<text x="{}" y="34" fill="#e8d9a8" font-size="24">Empire of Zek</text>'.format(PAD)]

    # exits, each drawn once
    done = set()
    for r, v in ROOMS.items():
        for d, t in v["exits"].items():
            if frozenset((r, t)) in done:
                continue
            done.add(frozenset((r, t)))
            (x1, y1), (x2, y2) = ctr(r), ctr(t)
            dash = ' stroke-dasharray="6 5"' if d in "ud" else ""
            if abs(pos[r][0] - pos[t][0]) <= 1 and abs(pos[r][1] - pos[t][1]) <= 1:
                out.append('<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#77736a" stroke-width="2"{}/>'
                           .format(x1, y1, x2, y2, dash))
                if d in "ud":
                    out.append('<text x="{}" y="{}" fill="#b8b3a6" font-size="11" text-anchor="middle">stairs</text>'
                               .format((x1 + x2) / 2 + 22, (y1 + y2) / 2 - 4))
            # the way into an inset is not drawn as a line; the surface room gets a note instead
    portal = {}  # surface room -> (text, colour) naming the inset below or above it
    for label, rooms, entry, outside in insets:
        way = next(d for d, t in ROOMS[outside]["exits"].items() if t == entry)
        arrow = {"d": "↓ ", "u": "↑ "}.get(way, "")
        portal[outside] = (arrow + label, COLORS.get(ROOMS[entry]["area"], ("", "#999999"))[1])

    # inset frames
    for label, rooms, entry, outside in insets:
        ix = [ctr(r)[0] for r in rooms]
        iy = [ctr(r)[1] for r in rooms]
        color = COLORS.get(ROOMS[entry]["area"], ("", "#999999"))[1]
        way = next(d for d, t in ROOMS[entry]["exits"].items() if t == outside)
        where = {"u": "below", "d": "above"}.get(way, "beside")
        out.append('<rect x="{}" y="{}" width="{}" height="{}" rx="12" fill="none" stroke="{}" stroke-dasharray="4 4"/>'
                   .format(min(ix) - BW / 2 - 14, min(iy) - BH / 2 - 30, max(ix) - min(ix) + BW + 28,
                           max(iy) - min(iy) + BH + 44, color))
        out.append('<text x="{}" y="{}" fill="{}" font-size="13">{} ({} {})</text>'
                   .format(min(ix) - BW / 2 - 4, min(iy) - BH / 2 - 12, color, escape(label), where,
                           escape(ROOMS[outside]["name"].replace("The ", ""))))

    # rooms
    for r, v in ROOMS.items():
        cx, cy = ctr(r)
        fill, border = COLORS.get(v["area"], ("#333333", "#999999"))
        bosses = [MONSTERS[m] for m, _ in v["spawns"] if MONSTERS[m]["boss"]]
        out.append('<rect x="{}" y="{}" width="{}" height="{}" rx="6" fill="{}" stroke="{}" stroke-width="{}"/>'
                   .format(cx - BW / 2, cy - BH / 2, BW, BH, fill,
                           BOSS_RED if bosses else border, 3 if bosses else 1.2))
        lines = textwrap.wrap(v["name"], 20)[:2]
        if bosses:
            sub = "Boss Lv {}".format(bosses[0]["level"])
        elif v["level"]:
            lo, hi = v["level"]
            sub = "Lv {}-{}".format(lo, hi) if lo != hi else "Lv {}".format(lo)
        else:
            sub = "safe" if v["safe"] else ""
        notes = [(sub, "#ff8a7a" if bosses else border)] if sub else []
        if r in portal:
            notes.append(portal[r])
        top = cy - (len(lines) + len(notes)) * 14 / 2 + 11
        for i, ln in enumerate(lines):
            out.append('<text x="{}" y="{}" fill="#f1ead6" font-size="12.5" text-anchor="middle">{}</text>'
                       .format(cx, top + i * 14, escape(ln)))
        for i, (text, color) in enumerate(notes):
            out.append('<text x="{}" y="{}" fill="{}" font-size="11" text-anchor="middle">{}</text>'
                       .format(cx, top + (len(lines) + i) * 14 + 1, color, escape(text)))

    # legend
    lx, ly = W - LEGEND_W + 40, PAD + 50
    out.append('<text x="{}" y="{}" fill="#e8d9a8" font-size="15">Areas</text>'.format(lx, ly))
    y = ly + 16
    for area, (fill, border) in COLORS.items():
        out.append('<rect x="{}" y="{}" width="22" height="16" rx="3" fill="{}" stroke="{}"/>'.format(lx, y, fill, border))
        out.append('<text x="{}" y="{}" fill="#ddd6c4" font-size="12">{}</text>'.format(lx + 30, y + 12, area))
        y += 24
    y += 10
    out.append('<rect x="{}" y="{}" width="22" height="16" rx="3" fill="none" stroke="{}" stroke-width="3"/>'
               .format(lx, y, BOSS_RED))
    out.append('<text x="{}" y="{}" fill="#ddd6c4" font-size="12">Boss room</text>'.format(lx + 30, y + 12))
    y += 26
    out.append('<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#77736a" stroke-width="2" stroke-dasharray="6 5"/>'
               .format(lx, y + 8, lx + 22, y + 8))
    out.append('<text x="{}" y="{}" fill="#ddd6c4" font-size="12">Up / down</text>'.format(lx + 30, y + 12))
    out.append('<text x="{}" y="{}" fill="#9a958a" font-size="11">North is up. Lv = monster levels.</text>'
               .format(lx, y + 36))
    out.append("</svg>")
    return "\n".join(out)


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "map.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(draw(*layout()))
    print("Wrote " + os.path.abspath(path))
