import yaml
import sys
import interface
import time

from collections import defaultdict


class TuringInterpreter:
    def __init__(self):
        self.tree = {}
        self.tape = defaultdict(lambda: "_")
        self.goto_flag = "flag go brrr"
        self.exec_start = "main"
        self.position = 0

        self.EXIT_SIG = "exit"

        self.func_table = {
            "read": self.read,
            "write": self.write,
            "move": self.move,
            "goto": self.goto,
        }

    def load_tree(self, data):
        self.tree = data

    #############################

    def goto(self, point):
        self.exec_start = point
        return self.goto_flag

    def move(self, dir):
        if dir == "left":
            self.position -= 1
        elif dir == "right":
            self.position += 1
        else:
            self.position += int(dir)

    def read(self, tree):
        if str(self.position) in self.tape:
            val = self.tape[str(self.position)]
            if val in tree:
                return self.scope(tree[val])

            if val == "_":
                return self.EXIT_SIG

    def write(self, val):
        self.tape[str(self.position)] = val

    ###############################
    def action(self, act, args):
        time.sleep(0.2)
        interface.draw_tape(new.tape)
        interface.selected = self.position
        if act in self.func_table:
            return self.func_table[act](args)

    def scope(self, instructions):
        # print("NEW SCOPE ", instructions)
        for i in instructions.keys():
            # print(i, instructions[i])
            ret = self.action(i, instructions[i])
            if ret == self.EXIT_SIG:
                return self.EXIT_SIG
            if ret == self.goto_flag:
                return self.goto_flag
        return None

    def execute(self):
        if "initial" in self.tree:
            self.position = self.tree["initial"]
        while True:
            func = self.scope(self.tree[self.exec_start])
            if func == self.EXIT_SIG or func is None:
                break


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Provide file as arguments")
        exit(code=1)

    with open(sys.argv[1]) as file:
        list = yaml.safe_load(file)
        tape = interface.init()
        new = TuringInterpreter()
        new.tape = tape
        new.load_tree(list)
        new.execute()
        interface.draw_tape(new.tape)
