import random
import time


class Battleship:
    def __init__(self):
        self.private_board = [
            [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
            ['A', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['B', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['C', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['D', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['E', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['F', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['G', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['H', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['I', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['J', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']]
        self.public_board = [
            [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
            ['A', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['B', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['C', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['D', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['E', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['F', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['G', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['H', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['I', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['J', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']]
        self.ships = [
            [[], []],
            [[], [], []],
            [[], [], [], []],
            [[], [], [], [], []],
            [[], [], [], [], [], []]]

    def get_remaining_ships(self):
        remaining_ships = []
        for i in self.ships:
            if not i[0]:
                remaining_ships.append(len(i))
        return remaining_ships

    def check_if_ship_is_valid(self, ship):
        try:
            ship = int(ship)
        except ValueError:
            return 0
        if ship < 2 or ship > 6:
            return 1
        elif self.ships[ship - 2][0]:
            return 2
        else:
            return 3

    @staticmethod
    def check_if_direction_is_valid(direction):
        if direction == 'u' or direction == 'd' or direction == 'l' or direction == 'r':
            return True

    @staticmethod
    def check_if_placement_valid(ship, start_position, direction):
        x_start_pos = start_position[0]
        y_start_pos = start_position[1]
        ship = int(ship) - 1  # has to include starting position
        if 'u' in direction:
            if y_start_pos - ship < 1:
                return False
        if 'd' in direction:
            if y_start_pos + ship > 10:
                return False
        if 'l' in direction:
            if x_start_pos - ship < 1:
                return False
        if 'r' in direction:
            if x_start_pos + ship > 10:
                return False
        return True

    def check_if_crosses_existing_ship(self, ship, start_position, direction):
        x_start_pos = start_position[0]
        y_start_pos = start_position[1]
        if direction == 'u':
            for i in range(ship):
                if self.private_board[y_start_pos - i][x_start_pos] == 's':
                    return True
        elif direction == 'd':
            for i in range(ship):
                if self.private_board[y_start_pos + i][x_start_pos] == 's':
                    return True
        elif direction == 'l':
            for i in range(ship):
                if self.private_board[y_start_pos][x_start_pos - i] == 's':
                    return True
        elif direction == 'r':
            for i in range(ship):
                if self.private_board[y_start_pos][x_start_pos + i] == 's':
                    return True
        return False

    def place_ship(self, ship, start_position, direction):
        x_start_pos = start_position[0]
        y_start_pos = start_position[1]
        if direction == 'u':
            for i in range(ship):
                self.private_board[y_start_pos - i][x_start_pos] = 's'
                self.ships[ship - 2][i].append(x_start_pos)
                self.ships[ship - 2][i].append(y_start_pos - i)
        elif direction == 'd':
            for i in range(ship):
                self.private_board[y_start_pos + i][x_start_pos] = 's'
                self.ships[ship - 2][i].append(x_start_pos)
                self.ships[ship - 2][i].append(y_start_pos + i)
        elif direction == 'l':
            for i in range(ship):
                self.private_board[y_start_pos][x_start_pos - i] = 's'
                self.ships[ship - 2][i].append(x_start_pos - i)
                self.ships[ship - 2][i].append(y_start_pos)
        elif direction == 'r':
            for i in range(ship):
                self.private_board[y_start_pos][x_start_pos + i] = 's'
                self.ships[ship - 2][i].append(x_start_pos + i)
                self.ships[ship - 2][i].append(y_start_pos)

    def get_private_board(self):
        return self.private_board

    def get_public_board(self):
        return self.public_board

    def print_public_board(self):
        for i in self.public_board:
            for j in i:
                print(j, end="   ")
            print("\n")

    def print_private_board(self):
        for i in self.private_board:
            for j in i:
                print(j, end="   ")
            print("\n")

    def check_adjacent_spots(self, coords):
        adjacent_spots = []
        x_coord = coords[0]
        y_coord = coords[1]
        try:
            adjacent_spots.append(self.public_board[y_coord - 1][x_coord])
        except IndexError:
            pass
        try:
            adjacent_spots.append(self.public_board[y_coord + 1][x_coord])
        except IndexError:
            pass
        try:
            adjacent_spots.append(self.public_board[y_coord][x_coord - 1])
        except IndexError:
            pass
        try:
            adjacent_spots.append(self.public_board[y_coord][x_coord + 1])
        except IndexError:
            pass
        return adjacent_spots

    def shoot(self, x_pos, y_pos):
        if self.private_board[y_pos][x_pos] == 's':
            self.public_board[y_pos][x_pos] = 'x'
            self.private_board[y_pos][x_pos] = 'x'
            return 0
        elif self.private_board[y_pos][x_pos] == 'x':
            return 1
        elif self.private_board[y_pos][x_pos] == '_':
            self.public_board[y_pos][x_pos] = 'o'
            self.private_board[y_pos][x_pos] = 'o'
            return 2
        elif self.private_board[y_pos][x_pos] == 'o':
            return 3

    def check_if_ship_sunk(self, x_pos, y_pos):
        for i in self.ships:
            if [x_pos, y_pos] in i:
                # Found which ship has this coordinate
                for j in i:
                    if self.private_board[j[1]][j[0]] != "x":
                        return False
                # All the ship's coordinates are "x"s
                return True
        raise ValueError("coordinate wasn't part of any ship")

    def check_all_ships_sunk(self):
        for i in self.ships:
            for j in i:
                if self.private_board[j[1]][j[0]] != 'x':
                    return False
        return True


def convert_game_pos_to_coords(pos):
    pos = pos.lower()
    try:
        x_coord = int(pos[1:])
    except ValueError:
        return []
    if x_coord < 1 or x_coord > 10:
        return []
    if pos[0] == 'a':
        y_coord = 1
    elif pos[0] == 'b':
        y_coord = 2
    elif pos[0] == 'c':
        y_coord = 3
    elif pos[0] == 'd':
        y_coord = 4
    elif pos[0] == 'e':
        y_coord = 5
    elif pos[0] == 'f':
        y_coord = 6
    elif pos[0] == 'g':
        y_coord = 7
    elif pos[0] == 'h':
        y_coord = 8
    elif pos[0] == 'i':
        y_coord = 9
    elif pos[0] == 'j':
        y_coord = 10
    else:
        return []
    return [x_coord, y_coord]


def convert_coords_to_game_pos(coords):
    game_pos = ""
    if coords[1] == 1:
        game_pos += "A"
    elif coords[1] == 2:
        game_pos += "B"
    elif coords[1] == 3:
        game_pos += "C"
    elif coords[1] == 4:
        game_pos += "D"
    elif coords[1] == 5:
        game_pos += "E"
    elif coords[1] == 6:
        game_pos += "F"
    elif coords[1] == 7:
        game_pos += "G"
    elif coords[1] == 8:
        game_pos += "H"
    elif coords[1] == 9:
        game_pos += "I"
    elif coords[1] == 10:
        game_pos += "J"
    game_pos += str(coords[0])
    return game_pos


def set_up_player_board(my_board):
    print("This is your board. You will place five ships  of differing lengths on it:\n")
    while len(my_board.get_remaining_ships()) > 0:
        my_board.print_private_board()

        remaining_ships = my_board.get_remaining_ships()
        print("Ship lengths remaining:", end=" ")
        for i in remaining_ships:
            print(i, end=" ")
        print()

        while True:
            ship = input("Pick a ship to place: ")
            if my_board.check_if_ship_is_valid(ship) == 0:
                print("That's not a number")
            elif my_board.check_if_ship_is_valid(ship) == 1:
                print("You don't have a ship of that length")
            elif my_board.check_if_ship_is_valid(ship) == 2:
                print("You already placed that ship")
            elif my_board.check_if_ship_is_valid(ship) == 3:
                break

        start_pos = []
        while not start_pos:
            start_pos = convert_game_pos_to_coords(input("Pick the point the ship will start at: "))
            if not start_pos:
                print("That's not a valid position")

        while True:
            direction = input("Pick a direction for the ship to go:  (u,d,l,r) ").lower()
            if my_board.check_if_direction_is_valid(direction):
                break
            print("That is not a valid direction, try again")

        if not my_board.check_if_placement_valid(ship, start_pos, direction):
            print("That placement would put the ship off the board, try again")
            continue

        if my_board.check_if_crosses_existing_ship(int(ship), start_pos, direction):
            print("That would put the ship through an existing ship try again")
            continue

        my_board.place_ship(int(ship), start_pos, direction)
    my_board.print_private_board()


def set_up_ai_board(ai_board):
    while len(ai_board.get_remaining_ships()) > 0:
        while True:
            ship = random.randint(2, 6)
            if ai_board.check_if_ship_is_valid(ship) == 3:
                break

        start_pos = []
        while not start_pos:
            start_pos = [random.randint(1, 10), random.randint(1, 10)]

        while True:
            direction = random.randint(1, 4)
            if direction == 1:
                direction = 'u'
            elif direction == 2:
                direction = 'd'
            elif direction == 3:
                direction = 'l'
            elif direction == 4:
                direction = 'r'
            if ai_board.check_if_direction_is_valid(direction):
                break

        if not ai_board.check_if_placement_valid(ship, start_pos, direction):
            continue

        if ai_board.check_if_crosses_existing_ship(ship, start_pos, direction):
            continue

        ai_board.place_ship(ship, start_pos, direction)


def ai_shot(my_board):
    board = my_board.get_public_board()
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if board[j][i] == "x":
                possible_shots = []
                try:
                    if board[j - 1][i] == "_":
                        possible_shots.append([i, j - 1])
                except IndexError:
                    pass
                try:
                    if board[j + 1][i] == "_":
                        possible_shots.append([i, j + 1])
                except IndexError:
                    pass
                try:
                    if board[j][i - 1] == "_":
                        possible_shots.append([i - 1, j])
                except IndexError:
                    pass
                try:
                    if board[j][i + 1] == "_":
                        possible_shots.append([i + 1, j])
                except IndexError:
                    pass
                if len(possible_shots) > 0:
                    return possible_shots[random.randint(0, len(possible_shots) - 1)]

    for i in range(15):
        coords = [random.randint(1, 10), random.randint(1, 10)]
        if board[coords[1]][coords[0]] != "o":
            if "o" not in my_board.check_adjacent_spots(coords):
                return coords

    coords = [random.randint(1, 10), random.randint(1, 10)]
    while board[coords[1]][coords[0]] != "_":
        coords = [random.randint(1, 10), random.randint(1, 10)]
    return coords


def player_turn(ai_board):
    shot = []
    while not shot:
        print("Computer's board")
        ai_board.print_public_board()
        shot = convert_game_pos_to_coords(input("Choose a spot to shoot: "))
        if not shot:
            print("That's not a valid spot")
    shot_result = ai_board.shoot(shot[0], shot[1])
    if shot_result == 0:
        print("You got a hit!")
        if ai_board.check_if_ship_sunk(shot[0], shot[1]):
            print("That ship is sunk")
    elif shot_result == 1:
        print("You already shot the ship there")
        if ai_board.check_if_ship_sunk(shot[0], shot[1]):
            print("That ship is sunk")
    elif shot_result == 2:
        print("You missed")
    elif shot_result == 3:
        print("You already shot that spot, it's a miss")


def ai_turn(my_board):
    shot = ai_shot(my_board)
    shot_result = my_board.shoot(shot[0], shot[1])
    print("The computer shot " + convert_coords_to_game_pos(shot))
    if shot_result == 0:
        print("The computer shot your ship!")
        if my_board.check_if_ship_sunk(shot[0], shot[1]):
            print("Your ship sunk")
    elif shot_result == 2:
        print("The computer missed")
    my_board.print_private_board()


def main():
    print("Welcome to Battleship.")
    time.sleep(1)
    print("This is a slightly modified version of the game where you will have slightly different ships than normal.")
    time.sleep(3)
    print("Enjoy the game!\n")
    time.sleep(2)

    my_board = Battleship()
    set_up_player_board(my_board)

    print("The computer is setting up it's board\n")
    time.sleep(2)

    ai_board = Battleship()
    set_up_ai_board(ai_board)

    ai_board.print_private_board()

    while True:
        player_turn(ai_board)
        time.sleep(1)
        if ai_board.check_all_ships_sunk():
            print("Game over. You won the game!")
            break

        ai_turn(my_board)
        time.sleep(2)
        if my_board.check_all_ships_sunk():
            print("Game over. You lost the game.")
            break


main()
