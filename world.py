"""Rooms, monster instances and respawning."""
import random

from data.monsters import MONSTERS
from data.rooms import NPCS, ROOMS

DIRECTIONS = {"n": "north", "s": "south", "e": "east", "w": "west", "u": "up", "d": "down"}
DIR_ALIASES = {"north": "n", "south": "s", "east": "e", "west": "w", "up": "u", "down": "d",
               "n": "n", "s": "s", "e": "e", "w": "w", "u": "u", "d": "d"}
RESPAWN_TICKS = 30
BOSS_RESPAWN_TICKS = 120


class MonsterInstance:
    def __init__(self, mid):
        d = MONSTERS[mid]
        L = d["level"]
        self.id = mid
        self.name = d["name"]
        self.level = L
        self.desc = d["desc"]
        self.boss = d["boss"]
        self.aggro = d["aggro"]
        self.specials = d["specials"]
        self.max_hp = int((20 + 15 * L) * (1 + 0.004 * L) * d["hp"])
        self.hp = self.max_hp
        scale = d["dmg"] * (1 + 0.006 * L)
        self.dmg_min = max(1, int((2 + 1.9 * L) * scale))
        self.dmg_max = max(2, int((4 + 2.8 * L) * scale))
        self.armor = int(2 * L * d["armor"])
        self.effects = []

    @property
    def alive(self):
        return self.hp > 0

    def short(self):
        return self.name[0].upper() + self.name[1:]

    def matches(self, word):
        word = word.lower()
        name = self.name.lower()
        if word in (name, self.id):
            return True
        return any(w.startswith(word) for w in name.replace("'", " ").replace("-", " ").split())

    def weaken_mult(self):
        pct = sum(e["pct"] for e in self.effects if e["type"] == "weaken")
        return max(0.3, 1 - pct)

    def add_effect(self, eff):
        self.effects = [e for e in self.effects if e.get("name") != eff.get("name")]
        self.effects.append(eff)

    def is_stunned(self):
        return any(e["type"] == "stun" for e in self.effects)

    def health_word(self):
        pct = self.hp / self.max_hp
        if pct >= 1:
            return "is in perfect health"
        if pct > 0.75:
            return "has a few scratches"
        if pct > 0.5:
            return "is wounded"
        if pct > 0.25:
            return "is badly wounded"
        if pct > 0.1:
            return "is bleeding heavily"
        return "is near death"


class Room:
    def __init__(self, rid, d):
        self.id = rid
        self.name = d["name"]
        self.area = d["area"]
        self.desc = d["desc"]
        self.exits = d["exits"]
        self.spawns = d["spawns"]
        self.npcs = d["npcs"]
        self.safe = d["safe"]
        self.level = d.get("level")
        self.items = list(d["items"])
        self.monsters = []
        self.respawn_at = {}  # monster id -> list of ticks when a replacement appears

    def count(self, mid):
        return sum(1 for m in self.monsters if m.id == mid and m.alive)

    def living(self):
        return [m for m in self.monsters if m.alive]

    def npc_list(self):
        return [NPCS[n] for n in self.npcs]


class World:
    def __init__(self):
        self.rooms = {rid: Room(rid, d) for rid, d in ROOMS.items()}
        self.tick_count = 0
        for room in self.rooms.values():
            for mid, n in room.spawns:
                for _ in range(n):
                    room.monsters.append(MonsterInstance(mid))

    def room(self, rid):
        return self.rooms[rid]

    def monster_died(self, room, mon):
        if mon in room.monsters:
            room.monsters.remove(mon)
        delay = BOSS_RESPAWN_TICKS if mon.boss else RESPAWN_TICKS
        room.respawn_at.setdefault(mon.id, []).append(self.tick_count + delay + random.randint(0, 10))

    def tick(self, n=1, avoid_room=None):
        """Advance world time. Returns list of (room_id, monster) that respawned."""
        spawned = []
        for _ in range(n):
            self.tick_count += 1
            for room in self.rooms.values():
                for mid, times in room.respawn_at.items():
                    due = [t for t in times if t <= self.tick_count]
                    if not due:
                        continue
                    if room.id == avoid_room and MONSTERS[mid]["boss"]:
                        continue  # bosses never pop in on top of the player
                    for t in due:
                        times.remove(t)
                        m = MonsterInstance(mid)
                        room.monsters.append(m)
                        spawned.append((room.id, m))
        return spawned

    # ------------------------------------------------------------------ persistence
    def to_dict(self):
        return {
            "tick": self.tick_count,
            "rooms": {rid: {"items": r.items,
                            "monsters": [[m.id, m.hp] for m in r.monsters if m.alive],
                            "respawn_at": r.respawn_at}
                      for rid, r in self.rooms.items()},
        }

    @classmethod
    def from_dict(cls, d):
        w = cls()
        w.tick_count = d.get("tick", 0)
        for rid, rd in d.get("rooms", {}).items():
            if rid not in w.rooms:
                continue
            r = w.rooms[rid]
            r.items = rd.get("items", [])
            r.monsters = []
            for mid, hp in rd.get("monsters", []):
                if mid in MONSTERS:
                    m = MonsterInstance(mid)
                    m.hp = min(hp, m.max_hp)
                    r.monsters.append(m)
            r.respawn_at = {k: v for k, v in rd.get("respawn_at", {}).items() if k in MONSTERS}
        return w
