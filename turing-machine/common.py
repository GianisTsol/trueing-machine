from collections import UserDict


class Tape(UserDict):
    def __setitem__(self, key, item):
        self.data[key] = item

    def __getitem__(self, key):
        if key not in self.data:
            self.data[key] = "_"
        return self.data[key]
