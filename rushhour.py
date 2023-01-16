from car import Car
from board import Board
import csv
from typing import List

class Rushhour:
    def __init__(self, game, size):
        # Create dictionary of cars and load in cars form input file
        self.cars = {}
        self.load_cars(f"gameboards/Rushhour{game}.csv")
        self.board = Board(size)


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
                
    def make_field_names(self) -> List:
        """ Creates a list of fieldnames of the list of dicts.
        post: field_names is a list in which the fieldnames of the dict is stated. 
        """
        # Create field_names
        field_names: List
        field_names = ['car', 'move']
        return field_names

    def give_output(self, file: str, field_names: List, dict: List) -> None:
        """ Creates a csv file of the output dict, if asked.
        pre: file is a string, field_names is a list and dict is a list of dictionaries.
        post: a csv file of the given name
        """
        # Check if file is given
        if file != 'n':
            # Write the list of dicts to a csv file
            with open(file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames = field_names)
                writer.writeheader()
                writer.writerows(dict)

    def want_output(self) -> str:
        """Asks the filename.
        post: file is a string of the filename.
        """
        file = 'n'
        while not file.endswith('.csv'):
            # Asks for the filename
            file = input("To what csv file do you want it written? ")
        # Returns
        return file

    def make_dict(self) -> List:
        """Makes an empty list
        post: dict is an empty list.
        """
        dict = []
        return dict

    def update_dict(self, dict: List, command: str) -> List[dict]:
        """Updates the dict with the command
        post: dict is a list of dictionaries"""

        for i in range(len(command)):
                # Accounts for dubble digit numbers
                if command[i] == '-':
                    move = int(command[i+1])
                    move = int(move) * -1 
                    break
                elif command[i].isdigit():
                    move = int(command[i])
                    break

        dictionary = {'car': command[0], 'move': move}

        dict.append(dictionary)

        return dict
    
    def place_cars(self):
        """ Place cars in constructed grid using coördinates and length from the cars dictionary """
        for car in self.cars:
            # Place cars with Horizontal orientation
            if self.cars[car].orientation == "H":
                for i in range(self.cars[car].column, self.cars[car].column + self.cars[car].length):
                    self.board.board[self.cars[car].row][i] = self.cars[car].car_id
            #  Place cars with Vertical orientation   
            else:
                for i in range(self.cars[car].row, self.cars[car].row + self.cars[car].length):
                    self.board.board[i][self.cars[car].column] = self.cars[car].car_id

        return self.board
    
    def move_cars(self, command, dict):
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
                            self.board.board[self.cars[car].row][i] = "_"
                        # Changes collumn coördinate of selected vehicle to new location in dictionary
                        self.cars[car].column = self.cars[car].column + move
                        # Updates car location on grid of gameboard
                        for i in range(self.cars[car].column, self.cars[car].column + self.cars[car].length):
                            self.board.board[self.cars[car].row][i] = self.cars[car].car_id
                        # Update list of dicts
                        dict = self.update_dict(dict, command)
                            
                    else:
                        # Moves cars with Vertical orientation
                        for i in range(self.cars[car].row, self.cars[car].row + self.cars[car].length):
                            self.board.board[i][self.cars[car].column] = "_"
                        # Changes row coördinate of selected vehicle to new location in dictionary
                        self.cars[car].row = self.cars[car].row + move
                        # Updates car location on grid of gameboard
                        for i in range(self.cars[car].row, self.cars[car].row + self.cars[car].length):
                            self.board.board[i][self.cars[car].column] = self.cars[car].car_id
                        # Update list of dicts
                        dict = self.update_dict(dict, command)
                    # MOVE BITCH
                    print(self.board)
    
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
                if car.column + move + car.length -1 >= len(self.board.board) or car.column < 0:
                    return False
                if (self.board.board[car.row][car.column + move] == '_' or self.board.board[car.row][car.column + move] == autoID) and (self.board.board[car.row][car.column + move + 1] == '_' or self.board.board[car.row][car.column + move + 1] == autoID):
                    # Checks if there are no cars in between selected car and next location
                    for i in range(move):
                        if self.board.board[car.row][car.column + i + car.length] != '_' and self.board.board[car.row][car.column + i + car.length] != autoID:
                            return False
                    return True
            # Move car for cars with Vertical orientation
            elif car.orientation == 'V':
                # Checks if input move is inside bounds grid
                if car.row + move + car.length - 1 >= len(self.board.board) or car.row + move < 0:
                    return False
                # Checks if new loaction is empty or same carID
                if (self.board.board[car.row + move][car.column] == '_' or self.board.board[car.row + move][car.column] == autoID) and (self.board.board[car.row + move + 1][car.column] == '_' or self.board.board[car.row + move + 1][car.column] == autoID):
                    # Checks if there are no cars in between selected car and next location
                    for i in range(move):
                        if self.board.board[car.row + i + car.length][car.column] != '_' and self.board.board[car.row + i + car.length][car.column] != autoID:
                            return False
                    return True
            # Checks if orientation is invalid (not H or V)   
            else:
                return False

    def is_solved(self) -> bool:
        """Checks if case is solved (checks if red car is in position) """
        # This is inspired by the is_won function of schuifpuzzel.py
        # Go through all cars
        for i in range (len(self.cars)):
            # Find the red car
            # if self.cars[i].car_id == 'X':
                # Get the row of the red car and save it in a variable
            row_x: int
            row_x = int(self.cars['X'].row)

        # Check if the red car is at the right place and return True if finished, false if not
        if self.board.board[row_x][-2] == "X" and self.board.board[row_x][-1] == "X":
            return True
        else:
            return False