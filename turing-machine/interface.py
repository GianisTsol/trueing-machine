from blessed import Terminal
from common import Tape
import json

tape = {}

with open("tape.json", "r") as f:
    tape = Tape(json.load(f))
    print(tape)

selected = 0
term = None
started = False


def init():
    global term
    global started
    global tape
    started = True
    term = Terminal()
    loop()
    return tape


def draw_tape(tape):
    if started:
        for i in range(1, term.width - 1):
            if i == selected + 1:
                style = term.white_on_blue_reverse
            else:
                style = term.white_on_blue

            print(
                term.move_xy(i, term.height // 2)
                + style
                + str(tape[i - 1])
                + term.normal
            )


def loop():
    global selected
    global tape
    print(term.home + term.clear)
    print(term.move_xy(1, term.height // 2 + 2) + "0" + term.normal)

    print(
        term.move_xy(term.width // 2, term.height // 2 - 10)
        + term.red_bold
        + "RUN (q)"
        + term.normal
    )

    with term.cbreak():
        val = ""
        while val.lower() != "q":
            val = term.inkey(timeout=0.1)
            draw_tape(tape)
            if val.is_sequence:
                val = val.name
                if val == "KEY_LEFT":
                    if selected > 0:
                        selected -= 1
                if val == "KEY_RIGHT":
                    if selected < term.width - 3:
                        selected += 1

                if val == "KEY_ENTER":
                    new = "_"
                    if tape[selected] == 0:
                        new = 1
                    if tape[selected] == 1:
                        new = "_"
                    if tape[selected] == "_":
                        new = 0
                    tape[selected] = new
        with open("tape.json", "w") as f:
            json.dump(tape.data, f)

        selected = -1
