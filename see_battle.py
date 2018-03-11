import random


def build_table(table):
    """
    This function build table for Player
    """
    print("             Player")
    print("   0  1  2  3  4  5  6  7  8  9")
    for i in range(0, len(table)):
        s = str(i) + ' '
        for j in range(0, len(table)):
            s = s + ' ' + str(table[i][j])
        print(s)


def build_tables(table, table2):
    """
    This function build table for Player and Computer
    """
    print("                Player                              Computer")
    print("   0  1  2  3  4  5  6  7  8  9           0  1  2  3  4  5  6  7  8  9")
    for i in range(0, len(table)):
        s = str(i) + ' '
        s2 = str(i) + ' '
        for j in range(0, len(table)):
            s = s + ' ' + str(table[i][j])
            s2 = s2 + ' ' + str(table2[i][j])
        both = s + "       " + s2
        print(both)


def table1(table):
    table[0][0] = "4"
    table[0][1] = "4"
    table[0][2] = "4"
    table[0][3] = "4"
    table[0][4] = "4"
    table[0][5] = "4"

    table[8][8] = "0"
    table[8][9] = "0"

    table[3][5] = "2"
    table[4][5] = "2"
    table[5][5] = "2"
    table[6][5] = "2"

    table[2][2] = "1"
    table[3][2] = "1"
    table[4][2] = "1"

    table[0][7] = "3"
    table[1][7] = "3"
    table[2][7] = "3"
    table[3][7] = "3"
    table[4][7] = "3"


def table2(table):
    table[0][0] = "4"
    table[1][0] = "4"
    table[2][0] = "4"
    table[3][0] = "4"
    table[4][0] = "4"
    table[5][0] = "4"

    table[9][8] = "0"
    table[9][9] = "0"

    table[5][3] = "2"
    table[5][4] = "2"
    table[5][5] = "2"
    table[5][6] = "2"

    table[2][2] = "1"
    table[2][3] = "1"
    table[2][4] = "1"

    table[7][0] = "3"
    table[7][1] = "3"
    table[7][2] = "3"
    table[7][3] = "3"
    table[7][4] = "3"


def table3(table):
    table[9][0] = "4"
    table[9][1] = "4"
    table[9][2] = "4"
    table[9][3] = "4"
    table[9][4] = "4"
    table[9][5] = "4"

    table[0][8] = "0"
    table[0][9] = "0"

    table[2][2] = "2"
    table[3][2] = "2"
    table[4][2] = "2"
    table[5][2] = "2"

    table[2][8] = "1"
    table[3][8] = "1"
    table[4][8] = "1"

    table[0][3] = "3"
    table[1][3] = "3"
    table[2][3] = "3"
    table[3][3] = "3"
    table[4][3] = "3"


first_table = []
first_table_1 = []
second_table = []
second_table_1 = []

for i in range(0, 10):
    first_table.append(["  "])
    first_table_1.append(["  "])
    second_table.append(["  "])
    second_table_1.append(["  "])
    for j in range(0, 9):
        first_table[i].append("  ")
        first_table_1[i].append("  ")
        second_table[i].append("  ")
        second_table_1[i].append("  ")

print("")
build_table(first_table_1)
print("")

r = random.randint(1, 3)
print(r)

if r == 1:
    table1(second_table)
elif r == 2:
    table2(second_table)
else:
    table3(second_table)

# loop for building ships
for i in range(0, 5):
    first_coord = input("Enter the initial coordinate of the ship size " + str(i + 2))
    last_coord = input("Enter the final coordinate of the ship size " + str(i + 2))
    p1X = int(first_coord[0])
    p1Y = int(first_coord[1])
    p2X = int(last_coord[0])
    p2Y = int(last_coord[1])
    while not ((p1X == p2X) or (p1Y == p2Y)):
        print("You must enter right coordinates")
        first_coord = input("Enter the initial coordinate of the ship size " + str(i + 2))
        last_coord = input("Enter the final coordinate of the ship size " + str(i + 2))
        p1X = int(first_coord[0])
        p1Y = int(first_coord[1])
        p2X = int(last_coord[0])
        p2Y = int(last_coord[1])
    # building a ships

    if (p1X == p2X) or (p1Y == p2Y):
        if p1X == p2X:
            for j in range(p1Y, (p1Y + i + 2)):
                first_table[p1X][j] = str(i)
                first_table_1[p1X][j] = "[]"
        else:
            for j in range(p1X, (p1X + i + 2)):
                first_table[j][p1Y] = str(i)
                first_table_1[j][p1Y] = "[]"
        build_table(first_table_1)

defeat_player = 0
defeat_computer = 0
turn = "Player"
end = False
# loop for entering coordinate to which player or computer want to shoot
while (end == False):
    # if player will shoot
    if turn == "Player":
        px = int(input("Enter the coordinate x to which you want to shoot: "))
        py = int(input("Enter the coordinate y to which you want to shoot: "))
        second_table_1[px][py] = "O "  # if not the bullet hit the ship
        shoot = False
        for i in range(0, 5):
            if second_table[px][py] == str(i):
                defeat_computer += 1  # adding points
                second_table_1[px][py] = "X "  # if the bullet hit the ship
                second_table[px][py] = " "
                shoot = True
        # if the bullet flew past
        if shoot == False:
            turn = "Computer"
    # if computer will shoot
    elif turn == "Computer":
        px = random.randint(0, 9)
        py = random.randint(0, 9)
        print("The computer shoot to the position " + str(px) + ", " + str(py))
        first_table_1[px][py] = "O "  # if not the bullet hit the ship
        shoot = False
        for i in range(0, 5):
            if first_table[px][py] == str(i):
                defeat_player += 1  # adding points
                first_table_1[px][py] = "X "  # if the bullet hit the ship
                first_table[px][py] = " "
                shoot = True
        # if the bullet flew past
        if shoot == False:
            turn = "Player"
    print("")
    build_tables(first_table_1, second_table_1)
    print("")
    # count who is won
    if defeat_player == 20:
        print("COMPUTER WIN")
        end = True
    elif defeat_computer == 20:
        print("PLAYER WIN")
        end = True
