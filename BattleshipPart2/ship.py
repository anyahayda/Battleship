class Ship:
    def __init__(self, length):
        self.bow = (0,0)
        self.horizontal = False
        self.length = length
        self.hit = []
        for i in range(self.length):
            self.hit.append(False)

    def check_at(self, pos):
        if self.horizontal:
            if self.bow[0] <= pos[0] < self.bow[0] + self.length and pos[1] == self.bow[1]:
                return True
        else:
            if self.bow[1] <= pos[1] < self.bow[1] + self.length and pos[0] == self.bow[0]:
                return True
        return False
    
    def shoot_at(self, pos):
        if self.horizontal:
            if self.bow[0] <= pos[0] < self.bow[0] + self.length and pos[1] == self.bow[1]:
                self.hit[pos[0] - self.bow[0]] = True
                return True
        else:
            if self.bow[1] <= pos[1] < self.bow[1] + self.length and pos[0] == self.bow[0]:
                self.hit[pos[1] - self.bow[1]] = True
                return True
        return False

    def is_alive(self):
        return False in self.hit

    def __str__(self):
        return str([self.bow, self.length, self.horizontal])


def test():
    ship = Ship((2))
    ship.bow = (2,2)
    print("Ship ", ship,)
    shootPos = (2,2)
    print("Shoot at ", shootPos, " ", ship.shoot_at(shootPos))
    print("Is alive", ship.is_alive())
    shootPos = (3,2)
    print("Shoot at ", shootPos, " ", ship.shoot_at(shootPos))
    print("Is alive", ship.is_alive())
    shootPos = (2,3)
    print("Shoot at ", shootPos, " ", ship.shoot_at(shootPos))
    print("Is alive", ship.is_alive())

