import random

ship_lengths = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]


class Field:
    def __init__(self):
        self.field_size = [10, 10]
        self.data = [[' ' for x in range(self.field_size[0])] for y in range(self.field_size[1])]

    def __str__(self):
        result = ''
        for line in self.data:
            result += ''.join(line) + '\n'
        return result

    def read_field(self, file_name):
        with open(file_name, 'r') as file:
            self.data = file.read().splitlines()

    def has_ship(self, pos):
        return self.data[pos[1]][pos[0]] == '*'

    def ship_size(self, pos):
        size = 0
        if self.data[pos[1]][pos[0]] == '*':
            size += 1
            for x in range(pos[1] + 1, len(self.data[0])):
                if self.data[pos[1]][x] == '*':
                    size += 1
                else:
                    break
            for x in range(pos[0] - 1, -1, -1):
                if self.data[pos[1]][x] == '*':
                    size += 1
                else:
                    break
            if size == 1:
                for y in range(pos[1] + 1, len(self.data)):
                    if self.data[y][pos[0]] == '*':
                        size += 1
                    else:
                        break
                for y in range(pos[1] - 1, -1, -1):
                    if self.data[y][pos[0]] == '*':
                        size += 1
                    else:
                        break
        return size

    def generate_field(self):
        self.data = [[' ' for x in range(self.field_size[0])] for y in range(self.field_size[1])]
        for length in ship_lengths:
            added = False
            x = 0
            y = 0
            while not added:
                horizontal = random.choice([True, False])
                x = y = 0
                has_space = True
                if horizontal:
                    x = random.randint(0, self.field_size[0] - length)
                    y = random.randint(0, self.field_size[1] - 1)
                    for i in range(length):
                        if self.has_ship((x + i, y)):
                            has_space = False
                            break
                    if has_space:
                        for i in range(length):
                            self.data[y][x + i] = '*'
                else:
                    x = random.randint(0, self.field_size[0] - 1)
                    y = random.randint(0, self.field_size[1] - length)
                    for i in range(length):
                        if self.has_ship((x, y + i)):
                            has_space = False
                            break
                    if has_space:
                        for i in range(length):
                            self.data[y + i][x] = '*'
                if has_space:
                    added = True


def test():
    f = Field()
    f.read_field('field.txt')
    print(f)
    print(f.ship_size((4, 1)))
    f.generate_field()
    print(f)


test()
