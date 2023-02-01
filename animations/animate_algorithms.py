# Import libraries
import matplotlib.pyplot as plt # type: ignore
from matplotlib.patches import Rectangle # type: ignore
from matplotlib.animation import FuncAnimation # type: ignore
from matplotlib import animation
import pandas as pd # type: ignore
import random
from typing import TypeVar, Dict, Any, List
import os
import sys
import inspect

# Import from different folder
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from car import Car

# Make typevar hints for self
Self = TypeVar("Self", bound="Animate")

# Set the current directory
script_dir = os.path.dirname(__file__)

# This class is based on the previous made file animation.py and rushhour.py
class Animate:
    def __init__(self: Self, game_name: str, size: int) -> None:
        """Initialize"""
        # Initialize imported variables
        self.game_name = game_name
        self.size = size

        # Initialize lists or dictionaries
        self.cars: Dict[Any, Any]
        self.cars = {}
        self.direction_x: List[int]
        self.direction_x = []
        self.direction_y: List[int]
        self.direction_y = []
        self.car_move: List[str]
        self.car_move = []
        self.dict_cars: Dict[str, str]
        self.dict_cars = {}
        self.rows: Dict[str, int]
        self.rows = {}
        self.columns: Dict[str, int]
        self.columns = {}

    def import_output_file(self) -> Any:
        """Read in the output file to later use it to move.
        Post: output is a Pandas dataframe with the moves each car made during the algorithm
        """
        full_path = os.path.join(script_dir, '../../JuLiDy/output.csv')
        # Get the output file from the directory
        output = pd.read_csv(full_path)
        return output

    def import_game_file(self) -> str:
        """Returns the full direction to the gameboard files.
        Post: game is a string which contains the direction to the gameboard file
        """
        # Save the right directory to the gameboard files
        game = os.path.join(script_dir, f'../../JuLiDy/gameboards/Rushhour{self.game_name}.csv')
        return game

    def create_plot(self) -> Any:
        """Creates the board.
        Post: plt is a module, a figure with all the cars in it
        """
        # Create plot
        fig, ax = plt.subplots()
        ax.set_xlim(1, self.size + 1)
        ax.set_ylim(1, self.size + 1)

        # Check if boardsize is odd or even
        if self.size % 2 == 0:
            # Creates the exit line
            ax.plot([self.size + 1, self.size + 1], [(self.size + 2) / 2, (self.size + 2) / 2 + 1],
                     color = "black")
        else:
            # Creates the exit line
            ax.plot([self.size + 1, self.size + 1], [(self.size + 1) / 2 + 1, (self.size + 1) / 2 + 2],
                     color = "black")

        # # Based on https://note.nkmk.me/en/python-dict-keys-values-items/
        # # Adds the cars to the board
        for cars in self.dict_cars.values():
            ax.add_patch(cars)

        # Returns the full board with the cars added
        return plt, fig, ax

    def get_car_info(self, file: str) -> None:
        """Gets the information on the cars from the gameboard files
        Pre: file is a string with the direction to the right files
        """
        # Open the file
        with open(file) as f:
            next(f)

            # Go through all the lines
            for line in f:
                if not line.strip():
                    break

                data = line.strip().split(",")
                # Get the information of the cars and save to self.cars
                car = Car(data[0], data[1], data[2], data[3], data[4])
                self.cars[data[0]] = car

    def reset_cars(self) -> None:
        """Resets the column and row to their original place."""
        # Go through each car in self.cars
        for car in self.cars:
            # Add one to column and row, this was subtracted in the Car class
            self.cars[car].column += 1
            self.cars[car].row += 1

    def define_cars(self) -> Dict[str, Rectangle]:
        """Defines the colour, size and location of the cars (Rectangles).
        Post: dict_cars is a dictionary with a string (key) and a Rectangle type
        """
        # Iterate over all the cars
        for car in self.cars:
            # Based on https://www.adamsmith.haus/python/answers/how-to-generate-a-random-color-for-a-matplotlib-plot-in-python
            # Get a random colour
            r = random.random()
            g = random.random()
            b = random.random()
            colour = (r, g, b)

            # Check orientation, size and/or car_id
            if self.cars[car].orientation == 'H' and self.cars[car].car_id != 'X':
                # Define the size, name, colour and location of the horizontally placed cars (not X)
                self.dict_cars['car{0}'.format(self.cars[car].car_id)] = Rectangle((self.cars[car].column, 
                                                        self.size + 1 - self.cars[car].row),
                                                        self.cars[car].length, 1, color = colour)
            elif self.cars[car].car_id == 'X':
                # Define the location of car X and set colour to red
                self.dict_cars['carX'] = Rectangle((self.cars[car].column, self.size + 1 - self.cars[car].row),
                                 2, 1, color = 'red')
            elif self.cars[car].length == 3 and self.cars[car].orientation == 'V':
                # Define the location and colour of trucks located vertically
                self.dict_cars['car{0}'.format(self.cars[car].car_id)] = Rectangle((self.cars[car].column, 
                                                        self.size - 1 - self.cars[car].row), 1,
                                                        3, color = colour)
            else:
                # Define the location, colour and name of the vertically located cars
                self.dict_cars['car{0}'.format(self.cars[car].car_id)] = Rectangle((self.cars[car].column, 
                                                        self.size - self.cars[car].row), 1,
                                                        self.cars[car].length, color = colour)

        # Return the dictionary
        return self.dict_cars

    def save_row(self) -> Dict[str, int]:
        """Puts the y coördinate (row number) of each car in a dictionary.
        Post: self.rows is a dictionary which consists of a string with the car name 
        and an integer with the y coördinate
        """
        # Go through each car in self.cars and get the y coördinate of each Rectangle type
        for car in self.cars:
            self.rows[self.cars[car].car_id] = dict_cars['car{0}'.format(self.cars[car].car_id)].get_y()

        return self.rows

    def save_column(self) -> Dict[str, int]: 
        """Puts the x coördinate (column number) of each car in a dictionary.
        Post: self.rows is a dictionary which consists of a string with the car name 
        and an integer with the x coördinate
        """ 
        # Go through each car in self.cars and the x coördinate of each Rectangel type
        for car in self.cars:
            self.columns[self.cars[car].car_id] = dict_cars['car{0}'.format(self.cars[car].car_id)].get_x()

        return self.columns

    def get_column(self, output: Any) -> List[int]:
        """Puts the column the cars are changed to into a list.
        Pre: output is an Any type, because it is a Pandas Dataframe
        Post: self.direction_x is a list with the x coördinates the car is changed to, 
        according to the output file
        """
        # Go through each line of the output file
        for line in output.index:
            # Go through each car in self.cars
            for car in self.cars:
                # Check if the right car is targeted
                if output['car'][line] == self.cars[car].car_id:
                    # Check if the car is oriëntated horizontally
                    if self.cars[car].orientation == 'H':
                        # Change the current column in self.columns
                        self.columns[car] += output['move'][line]
                        # Add the column number to self.direction_x
                        self.direction_x.append(self.columns[car])
                    # Check if car is oriëntated vertically and add the column to self.direction_x
                    else:
                        self.direction_x.append(self.columns[car])

        # Return the completed list
        return self.direction_x

    def get_row(self, output: Any) -> List[int]:
        """Puts the rows the cars are changed to into a list.
        Pre: output is an Any type, because it is a Pandas Dataframe
        Post: self.direction_y is a list with the y coördinates the car is changed to, 
        according to the output file
        """
        # Go through each line of the output file
        for line in output.index:
            # Go through each car in self.cars
            for car in self.cars:
                # Check if the right car is targeted
                if output['car'][line] == self.cars[car].car_id:
                    # Check if car is oriëntated horizontally and add the row to self.direction_y
                    if self.cars[car].orientation == 'H':
                        self.direction_y.append(self.rows[car])
                    # Check if the car is oriëntated vertically
                    else:
                        # Change the current row in self.rows
                        self.rows[car] -= output['move'][line]
                        # Add the row number to self.direction_y
                        self.direction_y.append(self.rows[car])

        # Return the completed list
        return self.direction_y

    def get_car(self, output: Any) -> List[str]:
        """Puts the cars which are changed into a list.
        Pre: output is an Any type, because it is a Pandas Dataframe
        Post: self.car_move is a list in which all the names of the cars, which are moved, 
        are documented
        """
        # Go through each line of the output file
        for line in output.index:
            # Add the car ID to the list
            self.car_move.append(f"car{output['car'][line]}")

        # Return the completed list
        return self.car_move

#------------------------------------------------------------
# Set up initial state and get variables

# Set up the initial state of Animate
animates = Animate('6x6_2', 6)

# Get the needed variables to set the board
output = animates.import_output_file()
game = animates.import_game_file()

# Prepare to set the board
animates.get_car_info(game)
animates.reset_cars()

# Get the needed variable to set the board
dict_cars = animates.define_cars()

# Get the needed variables to make the animation
rows = animates.save_row()
columns = animates.save_column()
direction_x = animates.get_column(output)
direction_y = animates.get_row(output)
car_move = animates.get_car(output)

#------------------------------------------------------------
# Set up animation and refer back to figure

# Set the board
plt, fig, ax = animates.create_plot()

def init() -> Rectangle:
    """Initialize animation"""
    # Based on https://note.nkmk.me/en/python-dict-keys-values-items/
    # Adds the cars to the board
    for cars in dict_cars.values():
        ax.add_patch(cars)

    # Return each car seperately
    for cars in dict_cars.values():
        return cars

def animate(i: int) -> str:
    """Prepare the steps for the animation.
    Pre: i is the indez for the animation
    Post: cars is a string which represents the car that has been moved"""
    # Go through each car in dict_cars
    for cars in dict_cars:
        # Make sure that the right car is targeted
        if car_move[i] == cars:
            # Move the car to the direction of the next int of direction_x and direction_y
            dict_cars[cars].set_xy([direction_x[i], direction_y[i]])

    # Return the moved car
    return cars

# Calculate the validity of the animation
interval = 1 / len(direction_x)

# Make the animation
rushHour = FuncAnimation(fig, animate, frames = len(direction_x), interval = interval,
                         init_func = init, repeat = False)

# Based on https://holypython.com/how-to-save-matplotlib-animations-the-ultimate-guide/
# Save animation as an gif-file
f = f"{script_dir}/animation.gif"
writergif = animation.PillowWriter(fps = 2) 
rushHour.save(f, writer = writergif)

# Show the animation
plt.show()