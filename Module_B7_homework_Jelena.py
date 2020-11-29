
class Ship:
    def __init__(self, board, orientation, size):
        self.board = board
        self.orientation = orientation
        self.size = size
        self.coordinates = []

    def plot_vertical(self, row, column):
        for i in range(self.size):
            if self.board[(row - 1) + i][column - 1] == "O":
                self.coordinates.append((row + i, column))
            else:
                raise Exception

    def plot_horizontal(self, row, column):
        for i in range(self.size):
            if self.board[row - 1][(column - 1) + i] == "O":
                self.coordinates.append((row, column + i))
            else:
                raise Exception


class Board:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self.fleet = []
        self.neighbours = []
        self.board = [["O" for _ in range(width)] for _ in range(height)]

    def display(self):
        print("    1   2   3   4   5   6 ")
        for count, row in enumerate(self.board, 1):
            print(count, "|", " | ".join(row), "|")

    def place_fleet(self):
        for _ in self.fleet:
            for coordinates in _:
                row, column = coordinates
                self.board[row - 1][column - 1] = u'\u2B1B'

    def place_neighbours(self):
        for i in self.fleet:
            for coordinates in i:
                row, column = coordinates
                self.neighbours.append([(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)])

    def create_ship(self, size):
        size = size
        flag = True
        while flag:
            self.display()
            try:
                print("Create your ship with %d" " deck(s)" % size)
                row = int(input("Pick a row you want to create your ship "))
                while row not in range(1, self.height + 1):
                    print("Wrong input.Try again")
                    row = int(input("Pick a row you want to create your ship "))
                else:
                    column = int(input("Pick a column you want to create your ship "))
                    while column not in range(1, self.width + 1):
                        print("Wrong input.Try again")
                        column = int(input("Pick a column you want to create your ship "))

                orientation = str(input("Choose V or H for vertical or  horizontal orientation accordingly "))
                if orientation == "v" or orientation == "h":
                    orientation = orientation
                else:
                    raise ValueError
                if orientation.lower() == "v":
                    ship = Ship(self.board, orientation, size)
                    ship.plot_vertical(row, column)
                    self.fleet.append(ship.coordinates)
                    self.place_fleet()
                    self.display()
                    print("Ship is created")
                    flag = False
                elif orientation.lower() == "h":
                    ship = Ship(self.board, orientation, size)
                    ship.plot_horizontal(row, column)
                    self.fleet.append(ship.coordinates)
                    self.place_fleet()
                    self.display()
                    print("Ship is created")
                    flag = False
            except ValueError:
                print("No, no, no...Type correct entrees. See rules of the game. Orientation value must be 'v' or 'h'."
                      " Row and column values should be numbers within width and height of the board.Try again")
            except IndexError:
                print("Incorrect input.Make sure your input row/column as height/width plus ship size")

            except Exception as e:
                print("Ops.Overlapping ships.")


player_1 = Board("Player_1", 6, 6)
player_1.create_ship(3)
player_1.create_ship(2)
# player_1.create_ship(2)
player_1.place_neighbours()
print(player_1.fleet)
print(player_1.neighbours)
# board.create_ship(1)
# board.create_ship(1)
# board.create_ship(1)
# board.create_ship(1)
