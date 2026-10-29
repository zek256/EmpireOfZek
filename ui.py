"""Terminal output helpers: ANSI colour (auto-disabled when unsupported) and word wrapping."""
import os
import queue
import shutil
import sys
import textwrap
import threading
import time

_CODES = {
    "reset": "0", "bold": "1", "dim": "2",
    "red": "31", "green": "32", "yellow": "33", "blue": "34", "magenta": "35", "cyan": "36", "white": "37",
    "grey": "90", "bred": "91", "bgreen": "92", "byellow": "93", "bblue": "94", "bmagenta": "95",
    "bcyan": "96", "bwhite": "97",
}

_color = True
_input = queue.Queue()
lines_printed = 0  # bumped by every printed line, so the game knows when to redraw the prompt
_prompt_open = False  # a prompt is on screen without a newline after it


def start_input():
    """Read stdin on a background thread so the game clock keeps ticking while the player types."""
    def reader():
        while True:
            line = sys.stdin.readline()
            if not line:
                _input.put(None)
                return
            _input.put(line.rstrip("\r\n"))
    threading.Thread(target=reader, daemon=True).start()


def read_line(timeout=None):
    """Next line typed by the player, or None if `timeout` seconds pass first. EOF ends the game."""
    deadline = None if timeout is None else time.monotonic() + timeout
    while True:
        # short waits keep Ctrl-C responsive on every platform
        wait = 0.25 if deadline is None else max(0.0, min(0.25, deadline - time.monotonic()))
        try:
            line = _input.get(timeout=wait)
        except queue.Empty:
            if deadline is not None and time.monotonic() >= deadline:
                return None
            continue
        if line is None:
            raise SystemExit
        global _prompt_open
        _prompt_open = False  # the player's Enter already moved to a new line
        return line


def write(text):
    """Print without a newline (prompts)."""
    global _prompt_open
    sys.stdout.write(text)
    sys.stdout.flush()
    _prompt_open = True


def _emit(text):
    global lines_printed, _prompt_open
    if _prompt_open:
        # output arriving on its own (a combat round, sleep) starts below the prompt, not beside it
        print()
        _prompt_open = False
    lines_printed += 1
    print(text)


def init(color=True):
    global _color
    if os.environ.get("NO_COLOR") or not sys.stdout.isatty():
        color = False
    if color and os.name == "nt":
        os.system("")  # enables ANSI escape processing in Windows consoles
    _color = color
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass


def c(text, *styles):
    if not _color or not styles:
        return str(text)
    seq = ";".join(_CODES[s] for s in styles)
    return f"\033[{seq}m{text}\033[0m"


def width():
    return max(40, min(100, shutil.get_terminal_size((88, 24)).columns - 2))


def wrap(text):
    return "\n".join(textwrap.fill(p, width()) if p else "" for p in str(text).split("\n"))


def say(text="", *styles):
    _emit(c(wrap(text), *styles) if styles else wrap(text))


def out(text=""):
    """Print without wrapping (for pre-formatted or coloured lines)."""
    _emit(text)


def rule(title=""):
    w = width()
    if title:
        side = max(2, (w - len(title) - 2) // 2)
        _emit(c("=" * side + f" {title} " + "=" * side, "yellow"))
    else:
        _emit(c("=" * w, "yellow"))


def bar(cur, mx, length=20, color="green"):
    mx = max(1, mx)
    filled = max(0, min(length, round(length * cur / mx)))
    return c("#" * filled, color) + c("-" * (length - filled), "grey")
