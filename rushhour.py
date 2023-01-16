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
            # Place cars with Horizontal orientation
            if self.cars[car].orientation == "H":
                for i in range(self.cars[car].column, self.cars[car].column + self.cars[car].length):
                    board.board[self.cars[car].row][i] = self.cars[car].car_id
            #  Place cars with Vertical orientation   
            else:
                for i in range(self.cars[car].row, self.cars[car].row + self.cars[car].length):
                    board.board[i][self.cars[car].column] = self.cars[car].car_id

        return board
    
    def move_cars(self, command):
        """ Reads input commands to select car object and move it the input ammount of spaces. 
        Takes oriëntatin of car object into consideration for direction of movement. Cars can only move forward or backwards not sideways."""
        # Isolate and save carID from input string into variable
        autoID = ''
        for i in range(len(command)):
            if command[i] == ' ':
                break
            else: 
                autoID = autoID + command[i]
       
        # Isolate and save input string movingdistance into variable and convert into integer
        for i in range(len(command)):
                # Accounts for dubble digit numbers
                if command[i] == '-':
                    move = int(command[i + 1])
                    move = int(move) * -1   
                    break
                elif command[i].isdigit():
                    move = int(command[i])
        
        # Selects input vehicle from dictionary
        for car in self.cars:
            if self.cars[car].car_id == autoID:
                orientation = self.cars[car].orientation
                # Checks if input command is valid
                if self.is_valid(command, self.cars[car], autoID):
                    # Moves vehicles with Horizontal orientation
                    if orientation == "H":
                        # Empties current vehicle locations on grid
                        for i in range(self.cars[car].column, self.cars[car].column + self.cars[car].length):
                            board.board[self.cars[car].row][i] = "_"
                        # Changes collumn coördinate of selected vehicle to new location in dictionary
                        self.cars[car].column = self.cars[car].column + move
                        # Updates car location on grid of gameboard
                        for i in range(self.cars[car].column, self.cars[car].column + self.cars[car].length):
                            board.board[self.cars[car].row][i] = self.cars[car].car_id
                            
                    else:
                        # Moves cars with Vertical orientation
                        for i in range(self.cars[car].row, self.cars[car].row + self.cars[car].length):
                            board.board[i][self.cars[car].column] = "_"
                        # Changes row coördinate of selected vehicle to new location in dictionary
                        self.cars[car].row = self.cars[car].row + move
                        # Updates car location on grid of gameboard
                        for i in range(self.cars[car].row, self.cars[car].row + self.cars[car].length):
                            board.board[i][self.cars[car].column] = self.cars[car].car_id
                    # MOVE BITCH
                    print(board)

    
    def is_valid(self, command, car, autoID) -> bool:
        """ Checks if input move is valid """
        # Check if slected vehicle exists in dictionary
        if autoID not in self.cars:
            return False
        else:
            # Isolate and save input string movingdistance into variable and convert into integer
            for i in range(len(command)):
                # Accounts for dubble digit numbers
                if command[i] == '-':
                    move = int(command[i+1])
                    move = int(move) * -1 
                    break
                elif command[i].isdigit():
                    move = int(command[i])
                    break
            # Move car for cars with Horizontal orientation
            if car.orientation == 'H':
                # Checks if input move is inside bounds grid
                if car.column + move + car.length - 1 >= len(board.board) or car.column < 0:
                    return False
                if (board.board[car.row][car.column + move] == '_' or board.board[car.row][car.column + move] == autoID) and (board.board[car.row][car.column + move + 1] == '_' or board.board[car.row][car.column + move + 1] == autoID):
                    # Checks if there are no cars in between selected car and next location
                    for i in range(move):
                        if board.board[car.row][car.column + i + car.length] != '_' and board.board[car.row][car.column + i + car.length] != autoID:
                            return False
                    return True
            # Move car for cars with Vertical orientation
            elif car.orientation == 'V':
                # Checks if input move is inside bounds grid
                print(car.row)
                print(car.row + move + car.length - 1)
                if car.row + move + car.length - 1 >= len(board.board) or car.row + move < 0:
                    return False
                # Checks if new loaction is empty or same carID
                if (board.board[car.row + move][car.column] == '_' or board.board[car.row + move][car.column] == autoID) and (board.board[car.row + move + 1][car.column] == '_' or board.board[car.row + move + 1][car.column] == autoID):
                    # Checks if there are no cars in between selected car and next location
                    for i in range(move):
                        if board.board[car.row + i + car.length][car.column] != '_' and board.board[car.row + i + car.length][car.column] != autoID:
                            return False
                    return True
            # Checks if orientation is invalid (not H or V)   
            else:
                print("CCC")
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
    # Start game
    while True:
        # Prompt input from user or algorithm 
        command = input("Welke auto wil je waarheen bewegen?").upper()

        # Uses input command to move selceted vehicle
        rushhour.move_cars(command)

        # Checks if game is solved and ends game
        if rushhour.is_solved():
            print("TRUEEEEEE")
            break

    
