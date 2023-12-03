


class Number:
    def __init__(self):
        self.numbers = []
        self.value = None
        self.textual_value = ''
        self.gears = set()

    def add(self, value, x, y):
        digit = Digit(value, x, y)
        self.numbers.append(digit)
        self.textual_value += value

    def finalize(self):
        self.value = int(self.textual_value)

    def __repr__(self):
        return self.textual_value
    def get_neighbor_symbols(self, data):
        neighbor_symbols = []
        neighbors = set()
        for digit in self.numbers:
            digit_neighbors = self.get_neighbors(digit, data)
            for dn in digit_neighbors:
                if data[dn[1]][dn[0]] == '*':
                    self.gears.add((dn[1],dn[0]))
                if not data[dn[1]][dn[0]].isnumeric() and data[dn[1]][dn[0]] != '.':
                    neighbors.add(data[dn[1]][dn[0]])
        return neighbors

    def get_neighbors(self, digit, data):
        pos = digit.pos
        neighbors = []
        for x in range(-1,2):
            for y in range(-1,2):
                neighbor_pos = (pos[0] + y, pos[1] + x)
                if neighbor_pos[0] > -1 and neighbor_pos[0] < len(data[0]):
                    if neighbor_pos[1] > -1 and neighbor_pos[1] < len(data):
                        neighbors.append(neighbor_pos)
        return neighbors


class Digit:
    def __init__(self, value, x, y):
        self.value = int(value)
        self.pos = (x, y)