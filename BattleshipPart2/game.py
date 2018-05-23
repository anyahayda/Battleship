from player import Player
from field import Field


class Game:
    def __init__(self):
        self.__players = [Player('Player 1'), Player('Player 2')]
        self.__fields = [Field() for player in self.__players] #enemy field for each player
        self.__current_player = 0

    def shoot_at(self, index, pos):
        self.__fields[index].shoot_at(pos)

    def field_with_ships(self, index):
        return self.__fields[index].field_with_ships()

    def field_without_ships(self, index):
        return self.__fields[index].field_without_ships()

    def play(self):
        while True:
            for i in range(len(self.__players)):
                print("Enemy field:\n" + str(self.__fields[i]))
                self.__fields[i].shoot_at(self.__players[i].read_position())
                if not self.__fields[i].has_alive_ships():
                    print(self.__players[i], 'win!')


def test():
    p = Player('Simple AI')
    f = Field()
    for x in range(f.field_size[0]):
        for y in range(f.field_size[1]):
            print(f)
            shoot_pos = (x,y)
            print('Shoot at pos:', shoot_pos)
            f.shoot_at(shoot_pos)
            if not f.has_alive_ships():
                print(p, "win")
                return
