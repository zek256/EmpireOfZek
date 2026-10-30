"""Game engine: command parser, exploration, quests, shops, save/load, rebirth."""
import json
import os
import random
import re
import time

import ui
from character import MAX_LEVEL, Character
from combat import AGGRO_GAP, Combat, con_color, resolve_self_effect
from data.abilities import ABILITIES
from data.classes import CLASS_ORDER, CLASSES, STATS
from data.items import ITEMS, SLOTS
from data.monsters import MONSTERS
from data.quests import QUESTS
from data.races import RACE_ORDER, RACES
from data.rooms import NPCS, RESPAWN_ROOM, START_ROOM
from world import DIR_ALIASES, DIRECTIONS, World

SAVE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "saves")
SAVE_VERSION = 1

HELP = [
    ("Movement", [("n, s, e, w, u, d", "move north/south/east/west/up/down (or type the full word)"),
                  ("look / l [thing]", "look at the room, or at a monster, person or item"),
                  ("exits", "list the exits from this room")]),
    ("Combat", [("attack / k <target>", "start a fight (or switch targets); you then auto-attack every round"),
                ("cast <spell> [target]", "cast a spell; in a fight it replaces your next round's attack"),
                ("ability / ab <name> [target]", "use a class ability (e.g. 'ab slam'), also queued for next round"),
                ("consider / con <target>", "judge how dangerous a monster is"),
                ("flee [direction]", "try to escape from combat"),
                ("spells / abilities", "list your spells and abilities")]),
    ("Character", [("stats / score", "full character sheet"),
                   ("level", "level, experience and upcoming abilities"),
                   ("rebirth", "at level 50, be reborn as a new class"),
                   ("sleep / rest", "fall asleep: recover 10% HP and mana every tick (not with enemies near)"),
                   ("wake / stand", "wake up"),
                   ("pet", "check on your summoned companion ('pet dismiss' to release it)")]),
    ("Items", [("inventory / i", "show what you carry"),
               ("equipment / eq", "show what you wear"),
               ("equip / wear / wield <item>", "equip an item"),
               ("remove <item|slot>", "take off an item"),
               ("use / drink <item>", "use a potion"),
               ("examine / x <item>", "inspect an item"),
               ("get / drop <item>", "pick up or drop an item ('get all')")]),
    ("Town", [("talk <person>", "speak with someone (accepts and completes quests)"),
              ("quests / journal", "show your quest log"),
              ("find <quest|#|monster>", "directions to your quest target, e.g. 'find vermin' -> 'wd'"),
              ("list / buy [n] <item> / sell [n|all] <item>", "trade with a merchant ('sell all rat tail', 'sell junk')")]),
    ("System", [("save / load", "save or load your game"),
                ("alias <word> <command>", "make a shortcut, e.g. 'alias mm cast magic missile'"),
                ("alias / unalias <word>", "list your aliases / remove one"),
                ("help", "show this help"),
                ("quit", "leave the game")]),
]


def strip_article(name):
    return re.sub(r"^(a|an|the|some)\s+", "", name, flags=re.I)


def cap(s):
    return s[0].upper() + s[1:] if s else s


TICK_SECONDS = 4.0     # one game tick: a combat round, a step of regeneration or sleep
SLEEP_RECOVERY = 0.10  # share of max HP and mana restored per tick while asleep
AWAKE_HP_REGEN = 0.02
AWAKE_MANA_REGEN = 0.03


def ask(prompt):
    """Blocking prompt for menus and confirmations (the game clock pauses meanwhile)."""
    ui.write(prompt)
    return ui.read_line()


class Game:
    def __init__(self, player, world=None, room_id=START_ROOM, dev=False):
        self.player = player
        self.world = world or World()
        self.room_id = room_id
        self.combat = None
        self.running = True
        self.dev = dev
        self.sleeping = False
        self.next_tick = 0.0

    @property
    def room(self):
        return self.world.room(self.room_id)

    # ================================================================ lookup helpers
    def find_monster(self, word, prefer=None):
        word = word.strip().lower()
        idx = 1
        m = re.match(r"^(\d+)\.(.+)$", word)
        if m:
            idx, word = int(m.group(1)), m.group(2)
        pools = []
        if prefer:
            pools.append(prefer)
        pools.append(self.room.living())
        for pool in pools:
            matches = [mon for mon in pool if mon.matches(word)]
            if len(matches) >= idx:
                return matches[idx - 1]
        return None

    @staticmethod
    def find_item(ids, word):
        word = word.strip().lower()
        if not word:
            return None
        idx = 1
        m = re.match(r"^(\d+)\.(.+)$", word)
        if m:
            idx, word = int(m.group(1)), m.group(2)
        exact, partial = [], []
        for iid in ids:
            name = strip_article(ITEMS[iid]["name"]).lower()
            if word in (name, iid, ITEMS[iid]["name"].lower()):
                exact.append(iid)
            elif word in name or all(any(w.startswith(p) for w in name.split()) for p in word.split()):
                partial.append(iid)
        found = exact or partial
        return found[idx - 1] if len(found) >= idx else None

    def find_npc(self, word):
        word = word.strip().lower()
        for nid in self.room.npcs:
            npc = NPCS[nid]
            if not word or any(k.startswith(word) for k in npc["keywords"]) or word in npc["name"].lower():
                return nid, npc
        return None, None

    @staticmethod
    def find_ability(args, pool):
        """Match the longest leading run of words to an ability name. Returns (ability, remaining text)."""
        words = args.lower().split()
        for k in range(len(words), 0, -1):
            cand = " ".join(words[:k])
            exact = [a for a in pool if a["name"].lower() == cand or a["id"] == cand.replace(" ", "_")]
            starts = [a for a in pool if a["name"].lower().startswith(cand)]
            hit = exact or (starts if len(starts) == 1 else [])
            if not hit and starts:
                # several abilities share the prefix: prefer the one usable now
                hit = starts[:1]
            if hit:
                return hit[0], " ".join(words[k:])
        return None, args

    # ================================================================ main loop
    def prompt(self):
        p = self.player
        hpc = "bgreen" if p.hp > p.max_hp * 0.5 else ("byellow" if p.hp > p.max_hp * 0.25 else "bred")
        tag = ui.c(" [COMBAT]", "bred") if self.combat else (ui.c(" [ASLEEP]", "bblue") if self.sleeping else "")
        if p.level >= MAX_LEVEL:
            xp = "L{} MAX".format(p.level)
        else:
            xp = "L{} {}%".format(p.level, int(100 * p.xp / p.xp_needed))
        # plain (dark) yellow reads as gold and stays distinct from the bright yellow of a wounded HP readout
        return "\n" + ui.c("<", "grey") + ui.c("{}/{}hp".format(p.hp, p.max_hp), hpc) + " " + \
            ui.c("{}/{}mp".format(p.mana, p.max_mana), "bblue") + " " + ui.c(xp, "yellow") + \
            ui.c(">", "grey") + tag + " "

    def reset_clock(self):
        self.next_tick = time.monotonic() + TICK_SECONDS

    def run(self):
        self.look()
        self.check_aggro()
        self.reset_clock()
        ui.write(self.prompt())
        while self.running:
            line = ui.read_line(max(0.0, self.next_tick - time.monotonic()))
            if line is None:  # the clock struck: one game tick
                self.reset_clock()
                before = ui.lines_printed
                self.guarded(self.game_tick)
                if self.running and ui.lines_printed != before:
                    ui.write(self.prompt())
                continue
            line = line.strip()
            if line:
                self.guarded(lambda: self.handle(line))
            if self.running:
                ui.write(self.prompt())

    @staticmethod
    def guarded(fn):
        try:
            fn()
        except (KeyboardInterrupt, SystemExit):
            raise
        except Exception as exc:  # keep the game alive if something unexpected breaks
            ui.say("Something strange happened ({}: {}). The world shimmers and steadies.".format(
                type(exc).__name__, exc), "red")

    def game_tick(self):
        if self.combat:
            self.combat.round()
        else:
            self.world_tick()

    SLEEP_OK = {"wake", "sleep", "stats", "level", "inventory", "equipment", "spells", "quests",
                "help", "save", "load", "quit", "pet", "examine", "find", "alias", "unalias"}

    def handle(self, line):
        parts = line.split(None, 1)
        verb = parts[0].lower()
        args = parts[1].strip() if len(parts) > 1 else ""
        if verb in self.player.aliases:
            # expand once (an alias can't start with another alias); extra words are appended,
            # so with 'alias mm cast magic missile', 'mm rat' casts at the rat
            line = self.player.aliases[verb] + (" " + args if args else "")
            parts = line.split(None, 1)
            verb = parts[0].lower()
            args = parts[1].strip() if len(parts) > 1 else ""
        if verb in DIR_ALIASES and not args:
            verb, args = "move", DIR_ALIASES[verb]
        elif verb == "go" and args.lower() in DIR_ALIASES:
            verb, args = "move", DIR_ALIASES[args.lower()]
        cmd = self.ALIASES.get(verb, verb)
        fn = getattr(self, "cmd_" + cmd, None)
        if fn is None or (cmd in self.DEV_CMDS and not self.dev):
            ui.say("Huh? Type 'help' for a list of commands.", "grey")
            return
        if self.sleeping and cmd not in self.SLEEP_OK:
            ui.say("You are asleep. Type 'wake' to get up.", "grey")
            return
        if self.combat and cmd in self.NO_COMBAT:
            ui.say("You can't do that in the middle of a fight!", "red")
            return
        fn(args)

    ALIASES = {
        "l": "look", "k": "attack", "kill": "attack", "hit": "attack", "fight": "attack",
        "c": "cast", "ab": "ability", "abil": "ability", "skill": "ability",
        "i": "inventory", "inv": "inventory", "eq": "equipment", "equip": "wear", "wield": "wear",
        "unequip": "remove", "drink": "use", "quaff": "use",
        "score": "stats", "sc": "stats", "sheet": "stats", "lvl": "level", "xp": "level",
        "x": "examine", "inspect": "examine", "take": "get", "pick": "get",
        "speak": "talk", "greet": "talk", "ask": "talk",
        "journal": "quests", "j": "quests", "quest": "quests", "shop": "list",
        "track": "find", "where": "find", "route": "find", "path": "find",
        "rest": "sleep", "stand": "wake", "con": "consider", "h": "help", "?": "help", "q": "quit", "exit": "quit",
        "abilities": "spells", "skills": "spells", "spellbook": "spells", "run": "flee",
    }
    NO_COMBAT = {"sleep", "save", "load", "talk", "buy", "sell", "list", "get", "drop",
                 "wear", "remove", "rebirth"}
    DEV_CMDS = {"setlevel", "goto", "addgold", "give"}

    # ================================================================ exploration
    def look(self):
        r = self.room
        p = self.player
        ui.out("")
        ui.out(ui.c(r.name, "byellow", "bold") + ui.c("  [{}]".format(r.area), "grey"))
        ui.say(r.desc)
        ui.out(ui.c("Exits:", "bcyan"))
        for d, rid in r.exits.items():
            ui.out(ui.c("{} - {}".format(DIRECTIONS[d], self.world.room(rid).name), "bcyan"))
        for npc in r.npc_list():
            marker = ""
            for qid in npc.get("quests", []):
                st = self.quest_state(qid)
                if st == "available":
                    marker = ui.c(" (!)", "byellow")
                    break
                if st == "ready":
                    marker = ui.c(" (?)", "byellow")
                    break
            ui.out(ui.c("{} is here.".format(cap(npc["name"])), "bgreen") + marker)
        for m in r.living():
            color, _ = con_color(m.level, p.level)
            boss = ui.c(" [BOSS]", "bred", "bold") if m.boss else ""
            ui.out(ui.c("{} (level {}) is here.".format(m.short(), m.level), color) + boss)
        if r.items:
            ui.out(ui.c("On the ground: " + ", ".join(ITEMS[i]["name"] for i in r.items), "bwhite"))
        if p.pet:
            ui.out(ui.c("{} waits loyally at your side.".format(cap(p.pet.name)), "cyan"))

    def cmd_look(self, args):
        if not args:
            self.look()
            return
        mon = self.find_monster(args)
        if mon:
            color, word = con_color(mon.level, self.player.level)
            ui.say(mon.desc)
            ui.say("{} {}. (Level {}: {}.)".format(mon.short(), mon.health_word(), mon.level, word), color)
            return
        nid, npc = self.find_npc(args)
        if npc:
            ui.say(npc["desc"])
            return
        if args.lower() in ("me", "self", "myself"):
            self.cmd_stats("")
            return
        self.cmd_examine(args)

    def cmd_exits(self, args):
        for d, rid in self.room.exits.items():
            ui.out("  {:<6} - {}".format(DIRECTIONS[d], self.world.room(rid).name))

    def cmd_move(self, args):
        d = DIR_ALIASES.get(args.lower())
        if not d:
            ui.say("Which way? (n, s, e, w, u, d)")
            return
        if self.combat:
            self.queue_flee(d)
            return
        if d not in self.room.exits:
            ui.say("You can't go that way.", "grey")
            return
        self.go(self.room.exits[d])

    def go(self, rid, verbose=True):
        self.leave_room()
        self.room_id = rid
        if verbose:
            self.look()
        self.check_aggro()

    def leave_room(self):
        """Monsters don't regenerate; instead, everything in a room you leave recovers fully."""
        for m in self.room.living():
            m.hp = m.max_hp
            m.effects = []

    def check_aggro(self):
        if self.combat or self.room.safe:
            return
        p = self.player
        hostile = [m for m in self.room.living() if m.aggro and m.level >= p.level - AGGRO_GAP]
        if hostile:
            if self.sleeping:
                self.sleeping = False
                ui.say("You are jolted awake!", "byellow")
            for m in hostile:
                ui.say("{} spots you and attacks!".format(m.short()), "bred")
            self.combat = Combat(self, hostile)
            self.combat.status_line()

    def world_tick(self):
        """One tick of time outside combat: regeneration or sleep, effect timers, cooldowns, respawns."""
        p = self.player
        rm = p.perk("regen_mult", 1.0)
        if self.sleeping:
            hp_pct = mana_pct = SLEEP_RECOVERY * rm
        else:
            hp_pct, mana_pct = AWAKE_HP_REGEN * rm, AWAKE_MANA_REGEN * rm
        hp_gain = p.heal(max(1, p.max_hp * hp_pct))
        mana_before = p.mana
        p.mana = min(p.max_mana, p.mana + max(1, int(p.max_mana * mana_pct)))
        if p.pet:
            p.pet.hp = min(p.pet.max_hp, p.pet.hp + max(1, int(p.pet.max_hp * hp_pct)))
        keep = []
        for e in p.effects:
            if e.get("fresh"):
                e["fresh"] = False
            if e["type"] == "dot":
                p.hp = max(1, p.hp - e["value"])
            elif e["type"] == "hot":
                p.heal(e["value"])
            e["turns"] -= 1
            if e["turns"] > 0:
                keep.append(e)
        p.effects = keep
        p.tick_cooldowns()
        if self.sleeping:
            ui.say("You sleep... (+{} HP, +{} mana)".format(hp_gain, p.mana - mana_before), "blue")
            if p.hp >= p.max_hp and p.mana >= p.max_mana:
                self.sleeping = False
                ui.say("You wake feeling fully refreshed, and climb to your feet.", "bgreen")
        arrived = False
        for rid, m in self.world.tick(1, avoid_room=self.room_id):
            if rid == self.room_id:
                ui.say("{} arrives.".format(m.short()), "red")
                arrived = True
        if arrived:
            self.check_aggro()

    # ================================================================ combat commands
    def start_combat(self, mon):
        """The player opens a fight: their first action resolves now, the next one a full tick later."""
        # aggressive monsters in the room pile in; passive ones stay out of it
        others = [m for m in self.room.living() if m is not mon and m.aggro and m.level >= self.player.level - AGGRO_GAP]
        self.combat = Combat(self, [mon] + others)
        self.combat.target = mon
        self.reset_clock()
        for m in others:
            ui.say("{} leaps to its ally's defence!".format(m.short()), "red")

    def end_combat(self):
        self.combat = None
        self.check_aggro()

    def cmd_attack(self, args):
        if self.combat:
            if not args:
                ui.say("You are already fighting! Your attacks land every round.", "grey")
                return
            mon = self.combat.find_target(args)
            if not mon:
                ui.say("You don't see that here.", "grey")
                return
            self.combat.target = mon
            ui.say("You turn to fight {}.".format(mon.name), "bred")
            return
        if self.room.safe:
            ui.say("The peace of this place stays your hand.", "grey")
            return
        if not args:
            alive = self.room.living()
            if not alive:
                ui.say("Attack whom?", "grey")
                return
            mon = alive[0]
        else:
            mon = self.find_monster(args)
        if not mon:
            ui.say("You don't see that here.", "grey")
            return
        ui.say("You attack {}!".format(mon.name), "bred")
        self.start_combat(mon)
        self.combat.player_attack(mon)

    def cmd_cast(self, args):
        self.use_ability(args, "spell")

    def cmd_ability(self, args):
        self.use_ability(args, "ability")

    def use_ability(self, args, kind):
        p = self.player
        if not args:
            self.cmd_spells("")
            return
        known = p.known_abilities()
        pool = [a for a in known if a["kind"] == kind] + [a for a in known if a["kind"] != kind]
        ab, rest = self.find_ability(args, pool)
        if not ab:
            ui.say("You know no {} by that name. Type 'spells' to see what you know.".format(kind), "grey")
            return
        err = self.ability_error(ab)
        if err:
            ui.say(err, "grey")
            return
        if self.combat:
            if ab["target"] == "enemy" and rest and not self.combat.find_target(rest):
                ui.say("You don't see that here.", "grey")
                return
            self.combat.queue("You prepare {}.".format(ab["name"]), lambda: self.ability_round(ab, rest))
            return
        if ab["target"] == "self":
            p.mana -= p.mana_cost(ab) if ab["kind"] == "spell" else 0
            if ab["cooldown"]:
                p.cooldowns[ab["id"]] = ab["cooldown"]
            ui.say(ab["msg"].format(t="yourself"), "bmagenta")
            for eff in ab["effects"]:
                resolve_self_effect(self, ab, eff)
            return
        if self.room.safe:
            ui.say("The peace of this place stays your hand.", "grey")
            return
        target = self.find_monster(rest) if rest else (self.room.living() or [None])[0]
        if not target:
            ui.say("There is nothing here to use that on." if not rest else "You don't see that here.", "grey")
            return
        self.start_combat(target)
        self.combat.player_ability(ab, target)

    def ability_error(self, ab):
        p = self.player
        if ab["level"] > p.level:
            return "{} will return to you at level {}.".format(ab["name"], ab["level"])
        if ab["id"] in p.cooldowns:
            return "{} is not ready yet ({} rounds).".format(ab["name"], p.cooldowns[ab["id"]])
        cost = p.mana_cost(ab) if ab["kind"] == "spell" else 0
        if cost > p.mana:
            return "You don't have enough mana for {} ({} needed).".format(ab["name"], cost)
        return None

    def ability_round(self, ab, target_word):
        """Resolve a queued spell or ability as this round's action."""
        c = self.combat
        err = self.ability_error(ab)
        if err:
            ui.say(err + " You attack instead.", "grey")
            c.auto_attack()
            return
        if ab["target"] == "self":
            c.player_ability(ab, None)
            return
        target = c.find_target(target_word) if target_word else None
        target = target if target and target.alive else c.current_target()
        if target:
            c.player_ability(ab, target)
        else:
            c.end_round()

    def cmd_flee(self, args):
        if not self.combat:
            ui.say("You aren't fighting anything.", "grey")
            return
        self.queue_flee(DIR_ALIASES.get(args.lower()) if args else None)

    def queue_flee(self, d):
        if d and d not in self.room.exits:
            ui.say("You can't flee that way!", "grey")
            return
        self.combat.queue("You look for a chance to escape...", lambda: self.attempt_flee(d))

    def attempt_flee(self, d):
        exits = self.room.exits
        d = d or random.choice(list(exits))
        boss = any(m.boss for m in self.combat.living())
        chance = (0.45 if boss else 0.7) + min(0.15, self.player.stat("DEX") / 1000)
        if random.random() < chance:
            ui.say("You break away and flee {}!".format(DIRECTIONS[d]), "byellow")
            self.combat = None
            self.go(exits[d])
        else:
            ui.say("You try to flee, but your foes cut off your escape!", "bred")
            self.combat.pass_turn()

    def cmd_consider(self, args):
        mon = self.find_monster(args) if args else None
        if not mon:
            ui.say("Consider whom?", "grey")
            return
        color, word = con_color(mon.level, self.player.level)
        boss = " It is a mighty foe of legend." if mon.boss else ""
        ui.say("{} (level {}) looks {}.{}".format(mon.short(), mon.level, word, boss), color)
        ui.say("  HP ~{}, hits for {}-{}, armor {}.".format(mon.max_hp, mon.dmg_min, mon.dmg_max, mon.armor), "grey")
        if mon.aggro:
            ui.say("  It watches you with hostile intent, and will attack on sight.", "red")
        else:
            ui.say("  It seems content to leave you alone, unless you start something.", "grey")

    def player_died(self):
        p = self.player
        self.combat = None
        self.sleeping = False
        ui.out("")
        ui.rule("YOU HAVE DIED")
        ui.say("Darkness takes you. For a long moment there is nothing... and then a distant warmth, "
               "like sunrise through closed eyelids. You awaken upon the cold marble before the "
               "Dawnfather's altar, weak, but alive.", "bwhite")
        #lost_xp = min(p.xp, int(p.xp_needed * 0.1)) if p.level < MAX_LEVEL else 0
        lost_xp = 0
        #lost_gold = p.gold // 10
        lost_gold = 0
        p.xp -= lost_xp
        p.gold -= lost_gold
        p.deaths += 1
        p.effects = []
        p.cooldowns = {}
        p.hp = max(1, p.max_hp // 2)
        p.mana = p.max_mana // 2
        if lost_xp or lost_gold:
            ui.say("You lost {} experience and {} gold.".format(lost_xp, lost_gold), "red")
        self.leave_room()
        self.room_id = RESPAWN_ROOM
        self.look()

    # ================================================================ character info
    def cmd_stats(self, args):
        p = self.player
        ui.rule(p.name)
        lives = ""
        if p.past_lives:
            lives = "  Past lives: " + ", ".join(CLASSES[l["cls"]]["name"] for l in p.past_lives)
        ui.out("{} {}, level {}{}".format(ui.c(p.race_name, "bcyan"), ui.c(p.class_name, "bcyan"),
                                          ui.c(p.level, "byellow"), lives))
        ui.out("HP   {} {}/{}".format(ui.bar(p.hp, p.max_hp, 24, "green"), p.hp, p.max_hp))
        ui.out("Mana {} {}/{}".format(ui.bar(p.mana, p.max_mana, 24, "blue"), p.mana, p.max_mana))
        if p.level < MAX_LEVEL:
            ui.out("XP   {} {}/{}".format(ui.bar(p.xp, p.xp_needed, 24, "cyan"), p.xp, p.xp_needed))
        else:
            ui.out("XP   " + ui.c("MAXIMUM LEVEL - you may REBIRTH", "bmagenta"))
        ui.out("")
        for s in STATS:
            base, gear, reb = p.base_stat(s), p.gear_stat(s), p.rebirth_bonus(s)
            extra = []
            if gear:
                extra.append("+{} gear".format(gear))
            if reb:
                extra.append("incl. +{} from past lives".format(reb))
            ui.out("  {} {:>4}   {}".format(ui.c(s, "byellow"), base + gear, ui.c(", ".join(extra), "grey")))
        lo, hi = p.weapon_range()
        ui.out("")
        ui.out("  Weapon damage {}-{}   Armor {}   Crit {:.0f}%   Dodge {:.0f}%".format(
            int(lo * p.damage_mult), int(hi * p.damage_mult), p.armor, p.crit_chance * 100, p.dodge * 100))
        ui.out("  Gold {}   Kills {}   Deaths {}".format(ui.c(p.gold, "yellow"), p.kills, p.deaths))
        ui.out(ui.c("  Racial perk: " + p.rdata["perk_text"], "grey"))
        active = [e for e in p.effects]
        if active:
            ui.out("  Active effects: " + ", ".join("{} ({})".format(e["name"], e["turns"]) for e in active))

    def cmd_level(self, args):
        p = self.player
        ui.out("Level {} {} ({} past lives).".format(p.level, p.class_name, len(p.past_lives)))
        if p.level >= MAX_LEVEL:
            ui.say("You stand at the pinnacle of mortal power. Type REBIRTH to begin anew as another class.", "bmagenta")
        else:
            ui.out("Experience: {}/{} ({} to next level)".format(p.xp, p.xp_needed, p.xp_needed - p.xp))
        upcoming = [a for a in p.known_abilities() if a["level"] > p.level][:5]
        if upcoming:
            ui.out("Coming abilities:")
            for a in upcoming:
                ui.out("  level {:>2}: {} ({})".format(a["level"], a["name"], CLASSES[a["cls"]]["name"]))

    def cmd_spells(self, args):
        p = self.player
        ui.rule("Spells & Abilities")
        for a in p.known_abilities():
            usable = a["level"] <= p.level
            origin = "" if a["cls"] == p.cls else " [{}]".format(CLASSES[a["cls"]]["name"])
            if a["kind"] == "spell":
                cost = "{} mana".format(p.mana_cost(a))
            else:
                cost = "ability"
            if a["cooldown"]:
                cost += ", {}r cd".format(a["cooldown"])
            if a["id"] in p.cooldowns:
                cost += ui.c(" (ready in {})".format(p.cooldowns[a["id"]]), "red")
            line = "  L{:>2} {:<27} {:<20} {}".format(a["level"], a["name"] + origin, cost, a["desc"])
            ui.out(ui.c(line, "bwhite") if usable else ui.c(line + " (locked)", "grey"))
        ui.out(ui.c("Use spells with 'cast <name> [target]' and abilities with 'ability <name> [target]'.", "grey"))

    def cmd_pet(self, args):
        p = self.player
        if not p.pet:
            ui.say("You have no companion.", "grey")
            return
        if args.lower().startswith("dis"):
            ui.say("You release {}. It fades away.".format(p.pet.name), "grey")
            p.pet = None
            return
        ui.say("{}: {} ({}/{} HP, {}-{} damage)".format(cap(p.pet.name), p.pet.desc, p.pet.hp, p.pet.max_hp,
                                                       p.pet.dmg_min, p.pet.dmg_max), "cyan")

    # ================================================================ items
    def item_line(self, iid):
        it = ITEMS[iid]
        bits = []
        if it["type"] == "weapon":
            bits.append("{}-{} dmg".format(*it["dmg"]))
        if it.get("armor"):
            bits.append("{} armor".format(it["armor"]))
        bits += ["{}+{}".format(s, v) for s, v in it.get("stats", {}).items()]
        if it.get("heal"):
            bits.append("heals {}".format(it["heal"]))
        if it.get("mana"):
            bits.append("restores {} mana".format(it["mana"]))
        lvl = it.get("level")
        req = ""
        if lvl and it["type"] in ("weapon", "armor"):
            req = " L{}".format(lvl)
            if lvl > self.player.level:
                req = ui.c(req, "red")
        return "{}{}{}".format(it["name"], req, " " + ui.c("(" + ", ".join(bits) + ")", "grey") if bits else "")

    def cmd_inventory(self, args):
        p = self.player
        ui.out(ui.c("You are carrying:", "byellow"))
        if not p.inventory:
            ui.out("  nothing at all.")
        counts = {}
        for iid in p.inventory:
            counts[iid] = counts.get(iid, 0) + 1
        for iid, n in sorted(counts.items(), key=lambda kv: (ITEMS[kv[0]]["type"], ITEMS[kv[0]]["name"])):
            ui.out("  {}{}".format("({}x) ".format(n) if n > 1 else "", self.item_line(iid)))
        ui.out(ui.c("Gold: {}".format(p.gold), "yellow"))

    def cmd_equipment(self, args):
        ui.out(ui.c("You are wearing:", "byellow"))
        for slot in SLOTS:
            iid = self.player.equipment.get(slot)
            ui.out("  {:<7} {}".format(slot + ":", self.item_line(iid) if iid else ui.c("-", "grey")))
        ui.out("  Armor rating: {}".format(self.player.armor))

    def cmd_wear(self, args):
        p = self.player
        iid = self.find_item(p.inventory, args)
        if not iid:
            ui.say("You aren't carrying that.", "grey")
            return
        ok, res = p.equip(iid)
        if not ok:
            ui.say(res, "grey")
            return
        if res:
            ui.say("You remove {}.".format(ITEMS[res]["name"]))
        ui.say("You equip {}.".format(ITEMS[iid]["name"]), "bgreen")

    def cmd_remove(self, args):
        p = self.player
        slot = args.lower() if args.lower() in SLOTS else None
        if not slot:
            iid = self.find_item([i for i in p.equipment.values() if i], args)
            slot = ITEMS[iid]["slot"] if iid else None
        if not slot or not p.equipment.get(slot):
            ui.say("You aren't wearing that.", "grey")
            return
        iid = p.unequip(slot)
        ui.say("You remove {}.".format(ITEMS[iid]["name"]))

    def cmd_use(self, args):
        p = self.player
        iid = self.find_item([i for i in p.inventory if ITEMS[i]["type"] == "consumable"], args)
        if not iid:
            ui.say("You have no such potion.", "grey")
            return
        if self.combat:
            self.combat.queue("You reach for {}.".format(ITEMS[iid]["name"]), lambda: self.drink_round(iid))
            return
        self.drink(iid)

    def drink_round(self, iid):
        if iid in self.player.inventory:
            self.drink(iid)
        self.combat.pass_turn()

    def drink(self, iid):
        p = self.player
        it = ITEMS[iid]
        p.inventory.remove(iid)
        ui.say("You drink {}.".format(it["name"]), "bgreen")
        if it.get("heal"):
            ui.say("You are healed for {} HP.".format(p.heal(it["heal"])), "bgreen")
        if it.get("mana"):
            before = p.mana
            p.mana = min(p.max_mana, p.mana + it["mana"])
            ui.say("You regain {} mana.".format(p.mana - before), "bblue")

    def cmd_examine(self, args):
        p = self.player
        pool = p.inventory + [i for i in p.equipment.values() if i] + self.room.items
        iid = self.find_item(pool, args)
        if not iid:
            ui.say("You see nothing like that here.", "grey")
            return
        it = ITEMS[iid]
        ui.out(ui.c(cap(it["name"]), "byellow"))
        ui.say(it["desc"])
        ui.out("  " + self.item_line(iid))
        if it["type"] in ("weapon", "armor"):
            cur = p.equipment.get(it["slot"])
            if cur and cur != iid:
                ui.out(ui.c("  Currently equipped: ", "grey") + self.item_line(cur))
        ui.out(ui.c("  Value: {} gold".format(it["value"]), "grey"))

    def cmd_get(self, args):
        r, p = self.room, self.player
        if not r.items:
            ui.say("There is nothing here to pick up.", "grey")
            return
        if args.lower() == "all":
            for iid in list(r.items):
                r.items.remove(iid)
                p.inventory.append(iid)
                ui.say("You pick up {}.".format(ITEMS[iid]["name"]))
            return
        iid = self.find_item(r.items, args)
        if not iid:
            ui.say("You don't see that here.", "grey")
            return
        r.items.remove(iid)
        p.inventory.append(iid)
        ui.say("You pick up {}.".format(ITEMS[iid]["name"]))

    def cmd_drop(self, args):
        p = self.player
        iid = self.find_item(p.inventory, args)
        if not iid:
            ui.say("You aren't carrying that.", "grey")
            return
        p.inventory.remove(iid)
        self.room.items.append(iid)
        ui.say("You drop {}.".format(ITEMS[iid]["name"]))

    # ================================================================ shops
    def shopkeeper(self):
        for nid in self.room.npcs:
            if NPCS[nid].get("shop"):
                return NPCS[nid]
        return None

    @staticmethod
    def price(iid):
        return max(1, ITEMS[iid]["value"])

    def cmd_list(self, args):
        shop = self.shopkeeper()
        if not shop:
            ui.say("There is no merchant here.", "grey")
            return
        ui.out(ui.c("{} offers:".format(cap(shop["name"])), "byellow"))
        for iid in shop["shop"]:
            ui.out("  {:>6} gold  {}".format(self.price(iid), self.item_line(iid)))
        ui.out(ui.c("Type 'buy <item>' or 'sell <item>' (merchants pay a third of an item's value).", "grey"))

    def cmd_buy(self, args):
        shop = self.shopkeeper()
        if not shop:
            ui.say("There is no merchant here.", "grey")
            return
        qty = 1
        m = re.match(r"^(\d+)\s+(.+)$", args)
        if m:
            qty, args = min(50, int(m.group(1))), m.group(2)
        iid = self.find_item(shop["shop"], args)
        if not iid:
            ui.say("'I don't sell anything like that.'", "grey")
            return
        cost = self.price(iid) * qty
        if cost > self.player.gold:
            ui.say("You can't afford that ({} gold needed).".format(cost), "red")
            return
        self.player.gold -= cost
        self.player.inventory += [iid] * qty
        ui.say("You buy {}{} for {} gold.".format("{} x ".format(qty) if qty > 1 else "", ITEMS[iid]["name"], cost), "bgreen")

    def cmd_sell(self, args):
        shop = self.shopkeeper()
        p = self.player
        if not shop:
            ui.say("There is no merchant here.", "grey")
            return
        if args.lower() in ("junk", "trophies"):
            junk = [i for i in p.inventory if ITEMS[i]["type"] == "junk"]
            total = sum(max(1, ITEMS[i]["value"] // 3) for i in junk)
            for i in junk:
                p.inventory.remove(i)
            p.gold += total
            ui.say("You sell {} trophies for {} gold.".format(len(junk), total), "yellow")
            return
        qty = 1
        m = re.match(r"^(all|\d+)\s+(.+)$", args, re.I)
        if m:
            qty, args = m.group(1).lower(), m.group(2)
        iid = self.find_item(p.inventory, args)
        if not iid:
            ui.say("You aren't carrying that.", "grey")
            return
        have = p.inventory.count(iid)
        qty = have if qty == "all" else min(int(qty), have)
        if qty < 1:
            ui.say("Sell how many?", "grey")
            return
        each = max(1, ITEMS[iid]["value"] // 3)
        for _ in range(qty):
            p.inventory.remove(iid)
        p.gold += each * qty
        ui.say("You sell {}{} for {} gold.".format("{} x ".format(qty) if qty > 1 else "", ITEMS[iid]["name"],
                                                    each * qty), "yellow")

    # ================================================================ quests & NPCs
    def quest_state(self, qid):
        q, p = QUESTS[qid], self.player
        st = p.quests.get(qid)
        if st and st["status"] == "done":
            return "done"
        if st:
            return "ready" if self.quest_progress(qid) >= q["count"] else "active"
        if q["prereq"] and p.quests.get(q["prereq"], {}).get("status") != "done":
            return "locked"
        if p.level < q["min_level"]:
            return "locked"
        return "available"

    def quest_progress(self, qid):
        q, p = QUESTS[qid], self.player
        if q["type"] == "collect":
            return p.inventory.count(q["target"])
        return p.quests.get(qid, {}).get("count", 0)

    def on_kill(self, mid):
        for qid, st in self.player.quests.items():
            q = QUESTS[qid]
            if st["status"] == "active" and q["type"] == "kill" and q["target"] == mid:
                if st["count"] < q["count"]:
                    st["count"] += 1
                    ui.say("Quest '{}': {}/{}".format(q["name"], st["count"], q["count"]), "byellow")
                    if st["count"] >= q["count"]:
                        ui.say("Quest objective complete! Return to {}.".format(NPCS[q["giver"]]["name"]), "byellow")

    def cmd_talk(self, args):
        nid, npc = self.find_npc(args)
        if not npc:
            ui.say("There is no one like that here.", "grey")
            return
        p = self.player
        ui.out(ui.c(cap(npc["name"]), "bgreen") + " says:")
        for qid in npc.get("quests", []):
            q = QUESTS[qid]
            st = self.quest_state(qid)
            if st == "ready":
                ui.say(q["complete"], "white")
                if q["type"] == "collect":
                    for _ in range(q["count"]):
                        p.inventory.remove(q["target"])
                p.quests[qid]["status"] = "done"
                rw = q["reward"]
                ui.say("Quest complete: {}!".format(q["name"]), "byellow")
                p.gold += rw.get("gold", 0)
                ui.say("You receive {} gold.".format(rw.get("gold", 0)), "yellow")
                for iid in rw.get("items", []):
                    p.inventory.append(iid)
                    ui.say("You receive {}.".format(ITEMS[iid]["name"]), "bwhite")
                for line, color in p.gain_xp(rw.get("xp", 0)):
                    ui.say(line, color) if color else ui.out(line)
                return
            if st == "active":
                ui.say(q["progress"].format(n=self.quest_progress(qid), count=q["count"]), "white")
                return
            if st == "available":
                ui.say(q["offer"], "white")
                p.quests[qid] = {"status": "active", "count": 0}
                ui.say("New quest accepted: {}".format(q["name"]), "byellow")
                return
        ui.say(npc["greeting"], "white")

    def cmd_quests(self, args):
        p = self.player
        ui.rule("Quest Journal")
        if not p.quests:
            ui.say("Your journal is empty. Speak with the townsfolk of Brightwater to find work.", "grey")
        for qid, st in p.quests.items():
            if st["status"] == "done":
                ui.out(ui.c("  [done] {}".format(QUESTS[qid]["name"]), "grey"))
        for i, qid in enumerate(self.active_quests(), 1):
            q = QUESTS[qid]
            n = self.quest_progress(qid)
            what = "slay" if q["type"] == "kill" else "collect"
            ui.out(ui.c("  {}. {} - {} {} ({}/{}), then return to {}.".format(
                i, q["name"], what, self.quest_target_name(qid), min(n, q["count"]), q["count"],
                NPCS[q["giver"]]["name"]), "byellow"))
        if self.active_quests():
            ui.out(ui.c("  Type 'find <quest name or number>' for directions.", "grey"))

    def active_quests(self):
        return [qid for qid, st in self.player.quests.items() if st["status"] != "done"]

    @staticmethod
    def quest_target_name(qid):
        q = QUESTS[qid]
        if q["type"] == "collect":
            return strip_article(ITEMS[q["target"]]["name"])
        return strip_article(MONSTERS[q["target"]]["name"])

    # ================================================================ find / directions
    def route_to(self, goals):
        """Shortest list of directions from here to any room in `goals`, or None if unreachable."""
        prev = {self.room_id: None}
        frontier = [self.room_id]
        while frontier:
            nxt = []
            for rid in frontier:
                if rid in goals:
                    goal, path = rid, []
                    while prev[rid]:
                        rid, d = prev[rid]
                        path.append(d)
                    return path[::-1], self.world.room(goal)
                for d, dest in self.world.room(rid).exits.items():
                    if dest not in prev:
                        prev[dest] = (rid, d)
                        nxt.append(dest)
            frontier = nxt
        return None, None

    def quest_goal(self, qid):
        """(set of room ids, description of what is there) for a quest's next step."""
        q = QUESTS[qid]
        if self.quest_state(qid) == "ready":
            rooms = {rid for rid, r in self.world.rooms.items() if q["giver"] in r.npcs}
            return rooms, "turn in to " + NPCS[q["giver"]]["name"]
        if q["type"] == "kill":
            mids = {q["target"]}
        else:
            mids = {mid for mid, m in MONSTERS.items() if any(i == q["target"] for i, _ in m["loot"])}
        rooms = {rid for rid, r in self.world.rooms.items() if any(mid in mids for mid, _ in r.spawns)}
        return rooms, self.quest_target_name(qid)

    def cmd_find(self, args):
        active = self.active_quests()
        word = args.strip().lower()
        qid = None
        if not word:
            if len(active) == 1:
                qid = active[0]
            else:
                ui.say("Find what? Give a quest name or number from your journal, or a monster's name.", "grey")
                for i, a in enumerate(active, 1):
                    ui.out("  {}. {}".format(i, QUESTS[a]["name"]))
                return
        elif word.isdigit() and 1 <= int(word) <= len(active):
            qid = active[int(word) - 1]
        else:
            qid = next((a for a in active if word in QUESTS[a]["name"].lower()), None)
        if qid:
            rooms, what = self.quest_goal(qid)
            title = QUESTS[qid]["name"]
        else:
            # not a quest: treat it as a monster name
            mids = {mid for mid, m in MONSTERS.items()
                    if word in strip_article(m["name"]).lower() or mid == word.replace(" ", "_")}
            if not mids:
                ui.say("You have no active quest called that, and no one has heard of such a creature.", "grey")
                return
            rooms = {rid for rid, r in self.world.rooms.items() if any(mid in mids for mid, _ in r.spawns)}
            title, what = args.strip(), None
        path, dest = self.route_to(rooms)
        if what is None and dest:
            what = strip_article(MONSTERS[next(mid for mid, _ in dest.spawns if mid in mids)]["name"])
        if path is None:
            ui.say("You can't find a way to {} from here.".format(what), "grey")
        elif not path:
            ui.say("{}: {} - right here!".format(title, what), "byellow")
        else:
            ui.say("{}: {} ({}).".format(title, what, dest.name), "byellow")
            ui.out("  Route: " + ui.c("".join(path), "bwhite", "bold") + ui.c("  ({} steps)".format(len(path)), "grey"))

    # ================================================================ player aliases
    MAX_ALIASES = 50

    def reserved_words(self):
        """Every word the game already understands; aliases may not shadow them."""
        words = {name[4:] for name in dir(self) if name.startswith("cmd_")}
        return words | set(self.ALIASES) | set(DIR_ALIASES) | {"go"}

    def cmd_alias(self, args):
        aliases = self.player.aliases
        parts = args.split(None, 1)
        if not parts:
            if not aliases:
                ui.say("You have no aliases. Create one with 'alias <word> <command>', "
                       "e.g. 'alias mm cast magic missile'.", "grey")
                return
            ui.out(ui.c("Your aliases:", "byellow"))
            for word, expansion in sorted(aliases.items()):
                ui.out("  {:<12} {}".format(ui.c(word, "bwhite"), expansion))
            return
        word = parts[0].lower()
        if len(parts) == 1:
            if word in aliases:
                ui.out("  {:<12} {}".format(ui.c(word, "bwhite"), aliases[word]))
            else:
                ui.say("'{}' is not an alias.".format(word), "grey")
            return
        expansion = parts[1].strip()
        if not re.fullmatch(r"[a-z0-9]{1,15}", word):
            ui.say("An alias must be a single word of letters or digits (up to 15).", "grey")
            return
        if word in self.reserved_words():
            ui.say("'{}' is already a game command and can't be used as an alias.".format(word), "red")
            return
        first = expansion.split()[0].lower()
        if first in aliases:
            ui.say("An alias can't start with another alias ('{}').".format(first), "red")
            return
        if word not in aliases and len(aliases) >= self.MAX_ALIASES:
            ui.say("You can have at most {} aliases. Remove one with 'unalias <word>'.".format(self.MAX_ALIASES), "grey")
            return
        replaced = word in aliases
        aliases[word] = expansion[:100]
        ui.say("Alias {}: '{}' now means '{}'.".format("updated" if replaced else "created", word, aliases[word]), "bgreen")

    def cmd_unalias(self, args):
        word = args.strip().lower()
        if word in self.player.aliases:
            del self.player.aliases[word]
            ui.say("Alias '{}' removed.".format(word), "bgreen")
        else:
            ui.say("'{}' is not an alias. Type 'alias' to list yours.".format(word) if word else "Unalias what?", "grey")

    # ================================================================ resting
    def cmd_sleep(self, args):
        p = self.player
        if self.sleeping:
            ui.say("You are already asleep.", "grey")
            return
        hostile = [m for m in self.room.living() if m.aggro]
        if hostile:
            ui.say("You can't sleep with {} nearby!".format(hostile[0].name), "red")
            return
        if p.hp >= p.max_hp and p.mana >= p.max_mana:
            ui.say("You are already fully rested.", "grey")
            return
        if self.room_id == "inn":
            ui.say("You take a room upstairs and sink into a soft feather bed.", "bblue")
        elif self.room.safe:
            ui.say("You find a quiet corner, lie down, and drift off to sleep.", "bblue")
        else:
            ui.say("You find a sheltered spot, keep your weapon close, and fall into an uneasy sleep.", "bblue")
        ui.say("(You recover {}% of your health and mana every {:g} seconds. Type 'wake' to get up.)".format(
            int(SLEEP_RECOVERY * 100), TICK_SECONDS), "grey")
        self.sleeping = True

    def cmd_wake(self, args):
        if not self.sleeping:
            ui.say("You are already awake.", "grey")
            return
        self.sleeping = False
        ui.say("You wake, stretch, and climb to your feet.", "bgreen")

    # ================================================================ rebirth
    def cmd_rebirth(self, args):
        p = self.player
        if p.level < MAX_LEVEL:
            ui.say("Only those who have reached level {} may seek rebirth. You are level {}.".format(MAX_LEVEL, p.level), "grey")
            return
        ui.rule("Rebirth")
        ui.say("You kneel and close your eyes. The world falls away, and you stand in a place of endless "
               "pale light. A voice older than the stars speaks: 'You have walked the path of the {} to "
               "its end. Choose a new path, and begin again - carrying all that you were.'".format(p.class_name), "bmagenta")
        ui.out("")
        ui.say("You will return to level 1 with XP reset. You keep every ability you have learned (each "
               "becomes usable again when you reach the level you first learned it), and the full stat "
               "gains of your {} life become a permanent bonus that grows as you level. Gear above "
               "level 1 will be unequipped until you can wield it again.".format(p.class_name), "white")
        choices = [c for c in CLASS_ORDER if c != p.cls]
        for i, cid in enumerate(choices, 1):
            past = " (lived before)" if cid in p.lived_classes() else ""
            ui.out("  {:>2}. {:<14} {}{}".format(i, CLASSES[cid]["name"], ui.c(CLASSES[cid]["desc"], "grey"), past))
        sel = ask("Choose your new class (number or name, blank to cancel): ").strip().lower()
        if not sel:
            ui.say("You open your eyes. Perhaps another day.", "grey")
            return
        cid = None
        if sel.isdigit() and 1 <= int(sel) <= len(choices):
            cid = choices[int(sel) - 1]
        else:
            cid = next((c for c in choices if c.startswith(sel)), None)
        if not cid:
            ui.say("That is not a path you can walk.", "grey")
            return
        if ask("Be reborn as a {}? This cannot be undone. (yes/no): ".format(CLASSES[cid]["name"])).strip().lower() not in ("y", "yes"):
            ui.say("You open your eyes. Perhaps another day.", "grey")
            return
        old = p.class_name
        removed = p.rebirth(cid)
        ui.out("")
        ui.say("Light pours through you. Your old life burns away like morning mist, and you are born "
               "anew as a {} - yet the {} you were remains within you.".format(p.class_name, old), "byellow")
        totals = {}
        for life in p.past_lives:
            for s, v in life["gains"].items():
                totals[s] = totals.get(s, 0) + v
        ui.say("Permanent bonus at level 50: " + ", ".join("{} +{}".format(s, v) for s, v in totals.items()), "bcyan")
        if removed:
            ui.say("Too heavy for your new body for now, you unequip: " + ", ".join(ITEMS[i]["name"] for i in removed), "grey")
        ready = [a["name"] for a in p.usable_abilities()]
        ui.say("Abilities usable now: " + ", ".join(ready), "bmagenta")

    # ================================================================ save / load
    def save_path(self, name):
        safe = re.sub(r"[^a-z0-9_-]", "_", name.lower())
        return os.path.join(SAVE_DIR, safe + ".json")

    def cmd_save(self, args):
        os.makedirs(SAVE_DIR, exist_ok=True)
        data = {"version": SAVE_VERSION, "player": self.player.to_dict(), "room": self.room_id,
                "world": self.world.to_dict()}
        path = self.save_path(self.player.name)
        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=1)
        os.replace(tmp, path)
        ui.say("Game saved ({}).".format(os.path.relpath(path)), "bgreen")

    def cmd_load(self, args):
        g = load_game_interactive(args, dev=self.dev)
        if g:
            self.player, self.world, self.room_id, self.combat = g.player, g.world, g.room_id, None
            self.sleeping = False
            ui.say("Game loaded. Welcome back, {}.".format(self.player.name), "bgreen")
            self.look()

    def cmd_quit(self, args):
        ans = ask("Save before quitting? (y/n/cancel): ").strip().lower()
        if ans.startswith("c"):
            return
        if ans.startswith("y"):
            if self.combat:
                ui.say("(Saving mid-combat: you will return just after the fight.)", "grey")
            self.cmd_save("")
        ui.say("Farewell, {}. May the Dawnfather light your road.".format(self.player.name), "byellow")
        self.running = False

    def cmd_help(self, args):
        ui.rule("Commands")
        for section, cmds in HELP:
            ui.out(ui.c(section, "byellow"))
            for k, v in cmds:
                ui.out("  {:<32} {}".format(ui.c(k, "bwhite"), v))
        ui.out(ui.c("Combat and sleep run on a {:g}-second game tick: one round of combat per tick.".format(TICK_SECONDS), "grey"))
        if self.dev:
            ui.out(ui.c("Dev: setlevel <n>, goto <room_id>, addgold <n>, give <item_id>", "grey"))

    # ================================================================ dev tools (python main.py --dev)
    def cmd_setlevel(self, args):
        p = self.player
        target = max(1, min(MAX_LEVEL, int(args or 1)))
        while p.level < target:
            for line, color in p.level_up():
                ui.say(line, color) if color else ui.out(line)
        p.level = target
        p.xp = 0
        p.hp, p.mana = p.max_hp, p.max_mana

    def cmd_goto(self, args):
        if args in self.world.rooms:
            self.combat = None
            self.go(args)
        else:
            ui.say("Rooms: " + ", ".join(self.world.rooms), "grey")

    def cmd_addgold(self, args):
        self.player.gold += int(args or 1000)

    def cmd_give(self, args):
        if args in ITEMS:
            self.player.inventory.append(args)
            ui.say("Given {}.".format(ITEMS[args]["name"]))


# ==================================================================== setup / loading
def list_saves():
    if not os.path.isdir(SAVE_DIR):
        return []
    return sorted(f[:-5] for f in os.listdir(SAVE_DIR) if f.endswith(".json"))


def load_game(path, dev=False):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    player = Character.from_dict(data["player"])
    world = World.from_dict(data.get("world", {}))
    room = data.get("room", START_ROOM)
    if room not in world.rooms:
        room = START_ROOM
    return Game(player, world, room, dev=dev)


def load_game_interactive(name="", dev=False):
    saves = list_saves()
    if not saves:
        ui.say("There are no saved games.", "grey")
        return None
    if not name:
        ui.out(ui.c("Saved games:", "byellow"))
        for i, s in enumerate(saves, 1):
            ui.out("  {}. {}".format(i, s))
        name = ask("Load which? (number or name, blank to cancel): ").strip()
        if not name:
            return None
    if name.isdigit() and 1 <= int(name) <= len(saves):
        name = saves[int(name) - 1]
    match = next((s for s in saves if s.lower() == name.lower()), None) or \
        next((s for s in saves if s.lower().startswith(name.lower())), None)
    if not match:
        ui.say("No save named '{}'.".format(name), "red")
        return None
    try:
        return load_game(os.path.join(SAVE_DIR, match + ".json"), dev=dev)
    except (OSError, ValueError, KeyError) as exc:
        ui.say("That save could not be read: {}".format(exc), "red")
        return None


def choose(prompt, options, label):
    for i, key in enumerate(options, 1):
        ui.out("  {:>2}. {}".format(i, label(key)))
    while True:
        sel = ask(prompt).strip().lower()
        if sel.isdigit() and 1 <= int(sel) <= len(options):
            return options[int(sel) - 1]
        match = [o for o in options if o.startswith(sel)] if sel else []
        if len(match) == 1 or (match and match[0] == sel):
            return match[0]
        ui.say("Please choose a number from the list.", "grey")


def create_character(dev=False):
    ui.rule("Create Your Hero")
    while True:
        name = ask("By what name shall the bards know you? ").strip()
        if re.fullmatch(r"[A-Za-z][A-Za-z' -]{1,19}", name):
            name = name[0].upper() + name[1:]
            break
        ui.say("Names must be 2-20 letters.", "grey")
    ui.out("")
    ui.out(ui.c("Choose your race:", "byellow"))
    race = choose("Race: ", RACE_ORDER, lambda r: "{:<10} {}".format(
        RACES[r]["name"], ui.c(RACES[r]["perk_text"], "grey")))
    ui.say(RACES[race]["desc"], "grey")
    ui.out("")
    ui.out(ui.c("Choose your class:", "byellow"))
    cls = choose("Class: ", CLASS_ORDER, lambda c: "{:<14} {}".format(CLASSES[c]["name"], ui.c(CLASSES[c]["desc"], "grey")))
    player = Character(name, race, cls)
    ui.out("")
    ui.rule()
    ui.say("You are {}, a {} {}.".format(name, RACES[race]["name"], CLASSES[cls]["name"]), "byellow")
    ui.say("The morning sun is warm on your face as you step into the town square of Brightwater, a "
           "pack on your shoulder and adventure in your heart. Rumours swirl through the market of rats "
           "in the inn cellar, wolves in the Whispering Woods, and darker things stirring beneath "
           "Barrowfield. Somewhere out there, your legend begins.")
    ui.say("Tip: type 'help' for commands. Visit Bram in the inn to the west for your first job.", "grey")
    return Game(player, dev=dev)
