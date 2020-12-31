from battleships.game import generate_ships, has_won, fire, fire_board
from battleships.board import create_board, print_board
from battleships.player_info import add_ships_player
from battleships.ships import ASCII_A, ASCII_J

import random

def set_fire_position():
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

    return (row, col)

# if __name__ == "__main__":
#     computer_board = create_board()
#     computer_board = generate_ships(computer_board)
#     print_board(computer_board)
#
#     player_board = create_board()
#     player_board = add_ships_player(player_board)
#     print_board(player_board)
#
#     while not has_won(computer_board) and not has_won(player_board):
#         print("Chose a position to fire at!")
#         position = set_fire_position()
#         computer_board = fire(position[0] + str(position[1]), computer_board)
#         print_board(fire_board(computer_board))
#
#         player_board = fire(chr(random.randint(ASCII_A, ASCII_J)) + str(random.randint(1, 10)), player_board)
#         print("Player board:")
#         print_board(player_board)
#     print("Game Over!")
#     if has_won(computer_board):
#         print("Good job player! You won by sinking all of your opponent's ships.")B
#         #has_won(board) checks if there are remaining ships
#         #since the computer_board has no remaining ships, the player won
#     else:
#         print("Oh no! You lose, your opponent sunk all of your ships.")


if __name__ == "__main__":
    computer_board = create_board()
    computer_board = generate_ships(computer_board)

    player_board = create_board()
    player_board = add_ships_player(player_board)

    while not has_won(computer_board) and not has_won(player_board):
        print("\nChose a position to fire at!")

        position = set_fire_position()
        fired_on_computer_board, message = fire(position[0] + str(position[1]), computer_board)
        print("You fired at (" + position[0] + "," + str(position[1]) + ") => " + message )
        print_board(fire_board(fired_on_computer_board))

        computer_position = chr(random.randint(ASCII_A, ASCII_J)) + str(random.randint(1, 10))
        fired_on_player_board, message = fire(computer_position, player_board)
        print("Your Opponent fired at (" + computer_position[0] + "," + computer_position[1] + ") => " + message )

    print("Game Over!")
    if has_won(computer_board):
        print("Good job player! You won by sinking all of your opponent's ships.")
        #has_won(board) checks if there are remaining ships
        #since the computer_board has no remaining ships, the player won
    else:
        print("Oh no! You lose, your opponent sunk all of your ships.")