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
            if result == OFF_BOARD and result == OVERLAP:
                print("OFF BOARD AND OVERLAP! Please try again...")
            elif result == OFF_BOARD:
                print("OFF BOARD! Please try again...")
            elif result == OVERLAP:
                print("OVERLAP! Please try again...")
            continue
        else:
            return board

def add_ships_player(board):
    for player in SHIPS:
        new_board = check_and_set_ship_player(player, board)
        print_board(new_board)

    return new_board