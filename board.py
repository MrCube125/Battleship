OFF_BOARD = "OFF BOARD!"
OVERLAP = "OVERLAP!"

def create_board(length = 10, width = 10):
    board = []
    row = []
    col = 65
    row.append(" ")
    for j in range(1, 11):
        row.append(str(j) + " ")
    board.append(row)
    for i in range(length):
        row = []
        row.append(chr(col) + " ")
        for j in range(width):
            row.append("~ ")
        col += 1
        board.append(row)
    return board

def print_board(board):
    if str(type(board)) == "<class 'str'>":
        print(board.strip())
    else:
        for i in board:
            for j in i:
                print(j, end = "")
            print()

def add_ship(ship, board):
    if ship.position == None:
        return "SHIP POSITION NONE!"

    game_board = board.copy()
    row = int(ship.to_coordinates()[0])
    col = int(ship.to_coordinates()[1])
    # print(row, col, ship.direction)

    if (ship.direction == "N" and row - ship.length < 0) or \
        (ship.direction == "S" and row + ship.length > 11) or \
        (ship.direction == "W" and col - ship.length < 0) or \
        (ship.direction == "E" and col + ship.length > 11):
        # print_board(board)
        return OFF_BOARD

    for i in range(ship.length):
        # check if the cell is occupied
        if game_board[row][col] == "X ":
            # print_board(board)
            return OVERLAP

        if ship.direction == "N":
            row -= 1
        elif ship.direction == "S":
            row += 1
        elif ship.direction == "E":
            col += 1
        elif ship.direction == "W":
            col -= 1

    row = int(ship.to_coordinates()[0])
    col = int(ship.to_coordinates()[1])

    for i in range(ship.length):
        game_board[row][col] = "X "
        if ship.direction == "N":
            row -= 1
        elif ship.direction == "S":
            row += 1
        elif ship.direction == "E":
            col += 1
        elif ship.direction == "W":
            col -= 1

    return game_board