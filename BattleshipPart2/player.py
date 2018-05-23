import string

class Player:
    def __init__(self, name):
        self.name = name

    def read_position(self):
        pos = list(input(self.name + ", enter move:" ))
        if len(pos) == 2:
            pos[0] = string.ascii_lowercase.index(pos[0])
            pos[1] = int(pos[1]) - 1
            return tuple(pos)
        return 0,0
    
    def __str__(self):
        return self.name