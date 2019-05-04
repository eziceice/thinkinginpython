def check_index(key):
    if not isinstance(key, int):
        raise TypeError
    if key < 0:
        raise IndexError


class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        check_index(key)

        try:
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    def __setitem__(self, key, value):
        check_index(key)
        self.changed[key] = value