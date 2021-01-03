import random
from board import add_ship, OFF_BOARD, OVERLAP
from ships import DIRECTIONS, Carrier, Battleship, Cruiser, Submarine, Destroyer, ASCII_A, ASCII_J
from copy import deepcopy

SHIPS = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]

def fire(position, board):
    row = ord(position[0]) - 64
    col = int(position[1:])
    game_board = board.copy()

    if game_board[row][col].strip() == "X" or game_board[row][col].strip() == "O":
        game_board[row][col] = "O "
        return (game_board, "HIT!");
    else:
        game_board[row][col] = "v "
        # this is what a cannonball hitting the water is supposed to look like
        # ~ ~ ~ ~ ~ v ~ ~ ~ ~
        return (game_board, "MISS!");

def fire_board(board):
    input = deepcopy(board)
    output = deepcopy(board)
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j].strip() == "X":
                output[i][j] = "~ "
            else:
                output[i][j] = input[i][j]
    return output

def set_ship_position(ship):
    row = chr(random.randint(ASCII_A, ASCII_J))
    col = random.randint(1, 10)
    pos = row + str(col)
    dir = DIRECTIONS[random.randint(0, 3)]

    if (ship == "Carrier"):
        return Carrier(dir, pos)
    elif (ship == "Battleship"):
        return Battleship(dir, pos)
    elif (ship == "Cruiser"):
        return Cruiser(dir, pos)
    elif (ship == "Submarine"):
        return Submarine(dir, pos)
    elif (ship == "Destroyer"):
        return Destroyer(dir, pos)
    else:
        return None

def generate_ships(board):
    for ship in SHIPS:
        while True:
            current_ship = set_ship_position(ship)
            result = add_ship(current_ship, board)
            if (result == OFF_BOARD or result == OVERLAP):
                continue
            else:
                board = result
                break
    return board

def has_won(board):
    for i in board:
        if "X " in i:
            return False
    return True