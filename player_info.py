from battleships.game import SHIPS, DIRECTIONS
from battleships.ships import ASCII_A, ASCII_J, Carrier, Battleship, Cruiser, Submarine, Destroyer, CARRIER_LEN, BATTLESHIP_LEN, CRUISER_LEN, SUBMARINE_LEN, DESTROYER_LEN
from battleships.board import add_ship, OFF_BOARD, OVERLAP, create_board, print_board

def set_ship_player(ship, direction, position):
    if (ship == "Carrier"):
        return Carrier(direction, position)
    elif (ship == "Battleship"):
        return Battleship(direction, position)
    elif (ship == "Cruiser"):
        return Cruiser(direction, position)
    elif (ship == "Submarine"):
        return Submarine(direction, position)
    elif (ship == "Destroyer"):
        return Destroyer(direction, position)
    else:
        return None

def get_length(ship_name):
    if ship_name == "Carrier":
        return CARRIER_LEN
    elif ship_name == "Battleship":
        return BATTLESHIP_LEN
    elif ship_name == "Cruiser":
        return CRUISER_LEN
    elif ship_name == "Submarine":
        return SUBMARINE_LEN
    elif ship_name == "Destroyer":
        return DESTROYER_LEN
    else:
        return None

# def add_ships_player(board):
#     for i in SHIPS:
#         print("This ship is a " + i + ". It is", str(get_length(i)), "cells long.")
#         row = input("Enter a row (A-J): ")
#         col = int(input("Enter a col (1-10): "))
#         direction = input("Enter a direction (N, S, W, E): ")
#         is_not_valid = ord(row) < ASCII_A or ord(row) > ASCII_J or col < 1 or col > 10 or not (direction in DIRECTIONS)
#         while is_not_valid:
#             print("You entered an invalid value!")
#             row = input("Enter a row (A-J): ")
#             col = int(input("Enter a col (1-10): "))
#             direction = input("Enter a direction (N, S, W, E): ")
#         ship = set_ship_player(i, direction, (row + str(col)))
#         invalid_ship = add_ship(ship, board) == OFF_BOARD or add_ship(ship, board) == OVERLAP
#         if invalid_ship:
#             while is_not_valid and invalid_ship:
#                 print("The value you entered was not compatible with the current board!")
#                 row = input("Enter a row (A-J): ")
#                 col = int(input("Enter a col (1-10): "))
#                 direction = input("Enter a direction (N, S, W, E): ")
#             else:
#                 print("Everything is fine...")
#         board = add_ship(ship, board)
#         print_board(board)

def check_and_set_ship_player(ship_name, board):
    while True:
        print("\nThis ship is a " + ship_name + ". It is", str(get_length(ship_name)), "cells long.")
        while True:
            try:
                row = input("Enter a row (A-J): ")
                row = row.upper()
                if ord(row) < ASCII_A or ord(row) > ASCII_J:
                    continue
                else:
                    break
            except:
                print("Invalid input!")
        while True:
            try:
                col = int(input("Enter a col (1-10): "))
                if col < 1 or col > 10:
                    continue
                else:
                    break
            except:
                print("Invalid input!")
        while True:
            direction = input("Enter a direction (N, S, W, E): ")
            direction = direction.upper()
            if direction not in DIRECTIONS:
                continue
            else:
                break

        ship = set_ship_player(ship_name, direction, (row + str(col)))
        result = add_ship(ship, board)
        if (result == OFF_BOARD or result == OVERLAP):
            print("OOPS => OFF_BOARD or OVERLAP, Please try again...")
            continue
        else:
            return board

def add_ships_player(board):
    for player in SHIPS:
        new_board = check_and_set_ship_player(player, board)
        print_board(new_board)

    return new_board

# board = create_board()
# add_ships_player(board)
