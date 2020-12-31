DIRECTIONS = ["N", "S", "E", "W"]
MIN_SHIP_LENGTH = 2
MAX_SHIP_LENGTH = 5

ASCII_A = 65
ASCII_J = 74

CARRIER_LEN = 5
BATTLESHIP_LEN = 4
CRUISER_LEN = 3
SUBMARINE_LEN = 3
DESTROYER_LEN = 2

class Ship:
    def __init__(self, length, direction, position):
        self.set_length(length)
        self.set_direction(direction)
        self.set_position(position)

    def set_length(self, length):
        if length > 0 and length <= MAX_SHIP_LENGTH:
            self.length = length
        else:
            self.length = -1

    def set_direction(self, direction):
        if direction in DIRECTIONS:
            self.direction = direction
        else:
            self.direction = None

    def set_position(self, position):
        """
        Vertical labels are from A, B, ... J
        Horizontal labels are from 1, 2... 10

        :param position:
        :return:
        """
        if (ord(position[0]) >= ASCII_A and ord(position[0]) <= ASCII_J) and (int(position[1:]) > 0 and int(position[1:]) <= 10):
            self.position = position
        else:
            self.position = None

    def to_coordinates(self):
        return (str(ord(self.position[0]) - ASCII_A + 1), self.position[1:])

class Carrier(Ship):
    def __init__(self, direction, position):
        super(Carrier, self).__init__(CARRIER_LEN, direction, position)

class Battleship(Ship):
    def __init__(self, direction, position):
        super(Battleship, self).__init__(BATTLESHIP_LEN, direction, position)

class Cruiser(Ship):
    def __init__(self, direction, position):
        super(Cruiser, self).__init__(CRUISER_LEN, direction, position)

class Submarine(Ship):
    def __init__(self, direction, position):
        super(Submarine, self).__init__(SUBMARINE_LEN, direction, position)

class Destroyer(Ship):
    def __init__(self, direction, position):
        super(Destroyer, self).__init__(DESTROYER_LEN, direction, position)
