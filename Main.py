"""Empire of Zek - an offline, single-player fantasy MUD.

Run:  python main.py            (add --no-color to disable colour, --dev for test commands)
"""
import argparse
import random
import sys

import game as engine
import ui
from game import ask, create_character, list_saves, load_game_interactive

TITLE = r"""
  +==================================================+
  |                                                  |
  |      E  M  P  I  R  E     o f     Z  E  K        |
  |                                                  |
  |      ~ swords, sorcery, and lives beyond ~       |
  |                                                  |
  +==================================================+
"""


def main():
    ap = argparse.ArgumentParser(description="Empire of Zek, a text fantasy RPG.")
    ap.add_argument("--no-color", action="store_true", help="disable ANSI colours")
    ap.add_argument("--dev", action="store_true", help="enable developer/test commands")
    ap.add_argument("--seed", type=int, help="random seed (for reproducible testing)")
    ap.add_argument("--tick", type=float, default=engine.TICK_SECONDS, help="seconds per game tick (default 4)")
    opts = ap.parse_args()
    engine.TICK_SECONDS = max(0.05, opts.tick)
    if opts.seed is not None:
        random.seed(opts.seed)
    ui.init(color=not opts.no_color)
    ui.start_input()

    ui.out(ui.c(TITLE, "byellow"))
    ui.say("A tale of swords and sorcery, of crypts and dragons, of heroes who live, and live again.", "grey")
    ui.out("")
    game = None
    while game is None:
        ui.out("  1. New game")
        ui.out("  2. Load game" + ("" if list_saves() else ui.c("  (no saves yet)", "grey")))
        ui.out("  3. Quit")
        sel = ask("> ").strip().lower()
        if sel in ("1", "n", "new"):
            game = create_character(dev=opts.dev)
        elif sel in ("2", "l", "load"):
            game = load_game_interactive(dev=opts.dev)
            if game:
                ui.say("Welcome back, {}.".format(game.player.name), "bgreen")
        elif sel in ("3", "q", "quit"):
            return
    game.run()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print()
        sys.exit(0)
