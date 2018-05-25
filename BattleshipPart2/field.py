from ship import Ship
import random


ship_lengths = [4, 3, 3, 2, 2, 2, 1, 1, 1,1 ]


class Field:
    def __init__(self):
        self.ships = []
        self.field_size = [10, 10]
        self.generate_random_field()
        self.misses = set()

    def __str__(self):
        """
        Returns built field with killed ships and missed shots.
        """
        field_list = [[' ' for x in range(10)] for y in range(10)]
        for ship in self.ships:
            if ship.horizontal:
                for i in range(ship.length):
                    field_list[ship.bow[1]][ship.bow[0]+i] = "X" if ship.hit[i] else '*'
            else:
                for i in range(ship.length):
                    field_list[ship.bow[1]+i][ship.bow[0]] = "X" if ship.hit[i] else '*'
        for miss in self.misses:
            field_list[miss[1]][miss[0]] = '.'

        result = ''
        for line in field_list:
            result += ''.join(line) + '\n'
        return result

    def has_ship(self, pos):
        """
        Return True if ship in the specified position and False if not.
        """
        for ship in self.ships:
            if ship.check_at(pos):
                return True;
        return False

    def shoot_at(self, pos):
        """
        Return True if hit the ship and False if not.
        """
        for ship in self.ships:
            if ship.shoot_at(pos):
                return True
        self.misses.add(pos)
        return False

    def has_alive_ships(self):
        """
        Returns True if ship is alive.
        """
        for ship in self.ships:
            if ship.is_alive():
                return True
        return False

    def generate_random_field(self):
        """
        Function for generating random field.
        """
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
                        if self.has_ship((x+i, y)):
                            has_space = False
                            break
                else:
                    x = random.randint(0, self.field_size[0] - 1)
                    y = random.randint(0, self.field_size[1] - length)
                    for i in range(length):
                        if self.has_ship((x, y+i)):
                            has_space = False
                            break
                if has_space:   
                    new_ship = Ship(length)
                    new_ship.bow = (x, y)
                    new_ship.horizontal = horizontal
                    self.ships.append(new_ship)
                    added = True

    def field_with_ships(self):
        """
        Returns field with ships.
        """
        return self.__str__()

    def field_without_ships(self):
        """
        Returns field without ships.
        """
        return self.__str__().replace('*', ' ')


def test():
    """
    Function fot testing battleship
    """
    f = Field()
    f.generate_random_field()
    print(f)
    for i in range(f.field_size[0]):
        for j in range(f.field_size[1]):
            shoot_pos = (i,j)
            print('Shoot at: ', shoot_pos)
            f.shoot_at(shoot_pos)
            print(f)
