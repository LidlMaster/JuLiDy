from car import Car
from board import Board

class Rushhour:

    def __init__(self, game):
        # Create dictionary of cars and load in cars form input file
        self.cars = {}
        self.load_cars(f"gameboards/Rushhour{game}.csv")

    def load_cars(self, filename):
        """ Read in input file, strip variables per car and stores it in a cars dictionary """
        with open(filename) as f:
            next(f)
            for line in f:
                if not line.strip():
                    break
                data = line.strip().split(",")
                car = Car(data[0], data[1], data[2], data[3], data[4])
                self.cars[data[0]] = car

    def place_cars(self):
        """ Place cars in constructed grid using coördinates and length from the cars dictionary """
        for car in self.cars:
            if self.cars[car].orientation == "H":
                for i in range(self.cars[car].column, self.cars[car].column + self.cars[car].length):
                    board.board[self.cars[car].row][i] = self.cars[car].car_id
            else:
                for i in range(self.cars[car].row, self.cars[car].row + self.cars[car].length):
                    board.board[i][self.cars[car].column] = self.cars[car].car_id

        return board
    
    def move_cars(self, command):
        """ Reads input commands to select car object and move it the input ammount of spaces. 
        Takes oriëntatin of car object into consideration for direction of movement. Cars can only move forward or backwards not sideways."""
        autoID = ''
        for i in range(len(command)):
            if command[i] == ' ':
                break
            else: 
                autoID = autoID + command[i]
        for i in range(len(command)):
                if command[i] == '-':
                    move = int(command[i + 1])
                    move = int(move) * -1   
                    break
                elif command[i].isdigit():
                    move = int(command[i])
        for car in self.cars:
            if self.cars[car].car_id == autoID:
                orientation = self.cars[car].orientation
                if self.is_valid(command, self.cars[car], autoID):
                    if orientation == "H":
                        for i in range(self.cars[car].column, self.cars[car].column + self.cars[car].length):
                            board.board[self.cars[car].row][i] = "_"
                        self.cars[car].column = self.cars[car].column + move
                        for i in range(self.cars[car].column, self.cars[car].column + self.cars[car].length):
                            board.board[self.cars[car].row][i] = self.cars[car].car_id
                            
                    else:
                        for i in range(self.cars[car].row, self.cars[car].row + self.cars[car].length):
                            board.board[i][self.cars[car].column] = "_"
                        self.cars[car].row = self.cars[car].row + move
                        for i in range(self.cars[car].row, self.cars[car].row + self.cars[car].length):
                            board.board[i][self.cars[car].column] = self.cars[car].car_id
                    # MOVE BITCH
                    print(board)

    
    def is_valid(self, command, car, autoID) -> bool:
        """ Checks if input move is valid """
        if autoID not in self.cars:
            return False
        else:
            for i in range(len(command)):
                if command[i] == '-':
                    move = int(command[i+1])
                    move = int(move) * -1   
                    break
                elif command[i].isdigit():
                    move = int(command[i])
                    break
            if car.orientation == 'H':
                if car.column + move > len(board.board) or car.column + move + 1 > len(board.board):
                    return False
                if (board.board[car.row][car.column + move] == '_' or board.board[car.row][car.column + move] == autoID) and (board.board[car.row][car.column + move + 1] == '_' or board.board[car.row][car.column + move + 1] == autoID):
                    return True
            elif car.orientation == 'V':
                if car.row + move > len(board.board) or car.row + move + 1 > len(board.board):
                    return False
                if board.board[car.row + move][car.column] == '_' and (board.board[car.row + move + 1][car.column] == '_' or board.board[car.row + move + 1][car.column] == autoID):
                    return True
            else:
                return False

    def is_solved(self) -> bool:
        """Checks if case is solved (checks if red car is in position) """
        # This is inspired by the is_won function of schuifpuzzel.py
        # Go through all cars
        for i in range (len(rushhour.cars)):
            # Find the red car
            # if self.cars[i].car_id == 'X':
                # Get the row of the red car and save it in a variable
            row_x: int
            row_x = int(self.cars['X'].row)

        # Check if the red car is at the right place and return True if finished, false if not
        if board.board[row_x][-2] == "X" and board.board[row_x][-1] == "X":
            return True
        else:
            return False

if __name__ == "__main__":

    from sys import argv

    # Check command line arguments and respond with usage in case of wrong input
    if len(argv) != 2:
        print("Usage: python rushhour.py <Size>x<Size>_boardnumber")
        exit(1)

    # Load the requested game
    game_name = argv[1]

    # strip input filename for size of board
    size = int(game_name[0])
    if game_name[1].isdigit():
        size = size * 10
        size += int(game_name[1])

    # Create board
    board = Board(size)

    # Create game
    rushhour = Rushhour(game_name)

    print(rushhour.place_cars())

    while True:
        # Prompt
        command = input("Welke auto wil je waarheen bewegen?")

        rushhour.move_cars(command)

        if rushhour.is_solved():
            print("TRUEEEEEE")
            break

    
