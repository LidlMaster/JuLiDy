from car import Car
from board import Board
import csv
import pandas as pd
from typing import List, TypeVar, Dict, Any
from copy import deepcopy

Self = TypeVar("Self", bound="Rushhour")

class Rushhour:
    def __init__(self: Self, game: str, size: int) -> None:
        """Initialize"""
        # Create dictionary of cars and load-in cars from input file
        self.cars: Dict[Any, Any]
        self.cars = {}
        self.load_cars(f"gameboards/Rushhour{game}.csv")
        self.board: Board
        self.board = Board(size)
        self.size = size
        self.dict = []


    def load_cars(self, filename: str) -> None:
        """ Read in input file, strip variables per car and stores it in a cars dictionary """
        with open(filename) as f:
            next(f)
            for line in f:
                if not line.strip():
                    break
                data = line.strip().split(",")
                car = Car(data[0], data[1], data[2], data[3], data[4])
                self.cars[data[0]] = car
                
    def make_field_names(self) -> List[str]:
        """ Creates a list of fieldnames of the list of dicts.
        post: field_names is a list in which the fieldnames of the dict is stated. 
        """
        # Create a list of the field names
        field_names: List[str]
        field_names = ['car', 'move']
        return field_names

    def give_output(self, file: str, field_names: List[str]) -> None:
        """ Creates a csv file of the output dict, if asked.
        pre: file is a string, field_names is a list and dict is a list of dictionaries.
        post: a csv file of the given name
        """
        # Check if na,me for file is given
        if file != 'n':
            # Code from https://www.geeksforgeeks.org/how-to-save-a-python-dictionary-to-a-csv-file/
            # Write the list of dicts to a csv file
            with open(file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames = field_names)
                writer.writeheader()
                writer.writerows(self.dict)

    def get_moves(self, file: str) -> int:
        """Gets the number of moves from the output file.
        post: number_moves is an int"""
        # Based on https://www.geeksforgeeks.org/how-to-count-the-number-of-lines-in-a-csv-file-in-python/
        # Get the csv file of the results
        output_file: List[str]
        output_file = pd.read_csv(file)

        # Count number of moves
        number_moves: int
        number_moves = len(output_file)
        return number_moves


    def update_dict(self, command: str) -> List[Dict[str, int]]:
        """Updates the dict with the command
        post: dict is a list of dictionaries"""

        # Save the info of the command
        autoID: str
        autoID = ''
        for i in range(len(command)):
            if command[i] == ' ':
                break
            else: 
                autoID = autoID + command[i]
       
        # Isolates and saves input string moving-distance into variable and convert into integer
        for i in range(len(command)):
                # Accounts for double digit numbers
                if command[i] == '-':
                    move: int
                    move = int(command[i + 1])
                    move = int(move) * -1   
                    break
                elif command[i].isdigit():
                    move = int(command[i])

        # Saves info in a dictionary to add to dict
        dictionary: Dict[str, Any]
        dictionary = {'car': autoID, 'move': move}
        self.dict.append(dictionary)

        return self.dict
    
    def place_cars(self) -> Board:
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
    
    def move_cars(self, command: str, mode: str) -> None:
        """ Reads input commands to select car object and move it the input ammount of spaces. 
        Takes oriëntation of car object into consideration for direction of movement. Cars can only move forward or backwards not sideways."""
        # Isolates and saves carID from input string into variable
        autoID: str
        autoID = ''
        for i in range(len(command)):
            if command[i] == ' ':
                break
            else: 
                autoID = autoID + command[i]
       
        # Isolates and saves input string moving-distance into variable and convert into integer
        for i in range(len(command)):
                # Accounts for double digit numbers
                if command[i] == '-':
                    move: int
                    move = int(command[i + 1])
                    move = int(move) * -1   
                    break
                elif command[i].isdigit():
                    move = int(command[i])
        
        # Selects input vehicle from dictionary
        for car in self.cars:
            if self.cars[car].car_id == autoID:
                orientation: str
                orientation = self.cars[car].orientation
                # Checks if input command is valid
                if self.is_valid(command, self.cars[car], autoID):
                    # Moves vehicles with Horizontal orientation
                    if orientation == "H":
                        # Empties current vehicle locations on grid
                        for i in range(self.cars[car].column, self.cars[car].column + self.cars[car].length):
                            self.board.board[self.cars[car].row][i] = "__"
                        # Changes column coördinate of selected vehicle to new location in dictionary
                        self.cars[car].column = self.cars[car].column + move
                        # Updates car location on grid of gameboard
                        for i in range(self.cars[car].column, self.cars[car].column + self.cars[car].length):
                            self.board.board[self.cars[car].row][i] = self.cars[car].car_id
                        # Update list of dicts
                        self.dict = self.update_dict(command)
                            
                    else:
                        # Moves cars with Vertical orientation
                        for i in range(self.cars[car].row, self.cars[car].row + self.cars[car].length):
                            self.board.board[i][self.cars[car].column] = "__"
                        # Changes row coördinate of selected vehicle to new location in dictionary
                        self.cars[car].row = self.cars[car].row + move
                        # Updates car location on grid of gameboard
                        for i in range(self.cars[car].row, self.cars[car].row + self.cars[car].length):
                            self.board.board[i][self.cars[car].column] = self.cars[car].car_id
                        # Update list of dicts
                        self.dict = self.update_dict(command)

                    # Print the board
                    if mode == "H":
                        print(self.board)
                        # print("")
    
    def is_valid(self, command: str, car: Car, autoID: str) -> bool:
        """ Checks if input move is valid """
        # Check if selected vehicle exists in dictionary
        if autoID not in self.cars:
            return False
        else:
            # Isolates and saves input string movingdistance into variable and convert into integer
            for i in range(len(command)):
                # Accounts for double digit numbers
                if command[i] == '-':
                    move = int(command[i+1])
                    move = int(move) * -1 
                    break
                elif command[i].isdigit():
                    move = int(command[i])
                    break
            if move == 0:
                return False
            # Move car for cars with Horizontal orientation
            if car.orientation == 'H':
                # Checks if input move is inside bounds grid
                if car.column + move + car.length -1 >= len(self.board.board) or car.column + move < 0:
                    return False
                if (self.board.board[car.row][car.column + move] == '__' or self.board.board[car.row][car.column + move] == autoID) and (self.board.board[car.row][car.column + move + 1] == '__' or self.board.board[car.row][car.column + move + 1] == autoID):
                    # Checks if there are no cars in between selected car and next location
                    if move > 0:
                        for i in range(move):
                            if self.board.board[car.row][car.column + i + car.length] != '__' and self.board.board[car.row][car.column + i + car.length] != autoID:
                                return False
                    elif move < 0:
                        for i in range(move - car.length, -1):
                            if self.board.board[car.row][car.column + i + car.length] != '__' and self.board.board[car.row][car.column + i + car.length] != autoID:
                                return False

                    return True
            # Move car for cars with Vertical orientation
            elif car.orientation == 'V':
                # Checks if input move is inside bounds grid
                if car.row + move + car.length - 1 >= len(self.board.board) or car.row + move < 0:
                    return False
                # Checks if new location is empty or same carID
                if (self.board.board[car.row + move][car.column] == '__' or self.board.board[car.row + move][car.column] == autoID) and (self.board.board[car.row + move + 1][car.column] == '__' or self.board.board[car.row + move + 1][car.column] == autoID):
                    # Checks if there are no cars in between selected car and next location
                    if move > 0:
                        for i in range(move):
                            if self.board.board[car.row + i + car.length][car.column] != '__' and self.board.board[car.row + i + car.length][car.column] != autoID:
                                return False
                    elif move < 0:
                        for i in range(move - car.length, -1):
                            if self.board.board[car.row + i + car.length][car.column] != '__' and self.board.board[car.row + i + car.length][car.column] != autoID:
                                return False

                    return True
            # Checks if orientation is invalid (not H or V)   
            else:
                return False
        return False

    def is_solved(self) -> bool:
        """Checks if case is solved (checks if red car is in position) """
        # This is inspired by the is_won function of schuifpuzzel.py
        # Go through all cars
        for i in range (len(self.cars)):
            # Get the row of the red car and save it in a variable
            row_x: int
            row_x = int(self.cars['X'].row)

        # Check if the red car is at the right place and return True if finished, false if not
        if self.board.board[row_x][-2] == "X" and self.board.board[row_x][-1] == "X":
            return True
        else:
            return False