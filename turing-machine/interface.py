from blessed import Terminal
import json

with open("tape.json", "r") as f:
    tape = json.load(f)

selected = 0
term = None
started = False


def init():
    global term
    global started
    started = True
    term = Terminal()
    loop()
    return tape


def draw_tape(tape):
    if started:
        for i in range(1, term.width - 1):
            j = str(i - 1)
            try:
                tape[j]
            except KeyError:
                tape[j] = "_"
            if i == selected + 1:
                style = term.white_on_blue_reverse
            else:
                style = term.white_on_blue

            print(
                term.move_xy(i, term.height // 2)
                + style
                + str(tape[j])
                + term.normal
            )
            print(
                term.clear_eol
                + term.move_xy(1, term.height // 2 + 2)
                + " "
                + str(selected)
                + " "
                + term.normal
            )


def loop():
    global selected
    print(term.home + term.clear)
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
                if val == "KEY_BACKSPACE":
                    tape[selected] = "_"

            try:
                tape[str(selected)] = int(val)
            except ValueError:
                pass

        with open("tape.json", "w+") as f:
            s = dict([(i, j) for i, j in tape.items() if j is not "_"])
            json.dump(s, f)

        selected = 0
