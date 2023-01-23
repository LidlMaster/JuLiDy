# Import libraries
import matplotlib.pyplot as plt # type: ignore
from matplotlib.patches import Rectangle # type: ignore
from matplotlib.animation import FuncAnimation
import pandas as pd # type: ignore
from car import Car
import random
from typing import TypeVar, Dict, Any

# Make typevar hints for self
Self = TypeVar("Self", bound="Animate")

# This class is based on the previous made file animation.py and rushhour.py
class Animate:
    def __init__(self: Self, game_name: str, size: int) -> None:
        """Initialize"""
        self.game_name = game_name
        self.size = size
        self.cars: Dict[Any, Any]
        self.cars = {}
        self.direction_x = []
        self.direction_y = []
        self.car_move = []
        self.dict_cars = {}
        self.rows = {}
        self.columns = {}

    def import_output_file(self) -> Any:
        """Read in the output file to later use it to move.
        Post: output is a Pandas dataframe with the moves each car made during the algorithm
        """
        output = pd.read_csv('output.csv')
        return output

    def import_game_file(self) -> str:
        """Returns the full direction to the gameboard files.
        Post: game is a string which contains the direction to the gameboard file
        """
        game = f"gameboards/Rushhour{self.game_name}.csv"
        return game

    def create_plot(self) -> Any:
        """Creates the board.
        Pre: dict_cars is a dictionary with the strings and Rectangle of the cars
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

    def reset_cars(self):
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

    def save_row(self):
        for car in self.cars:
            self.rows[self.cars[car].car_id] = dict_cars['car{0}'.format(self.cars[car].car_id)].get_y()
        return self.rows

    def save_column(self):  
        for car in self.cars:
            self.columns[self.cars[car].car_id] = dict_cars['car{0}'.format(self.cars[car].car_id)].get_x()

        return self.columns

    def get_column(self, output):
        for line in output.index:
            for car in self.cars:  
                if output['car'][line] == self.cars[car].car_id:
                    if self.cars[car].orientation == 'H':
                        self.columns[car] += output['move'][line]
                        self.direction_x.append(self.columns[car])
                    else:
                        self.direction_x.append(self.columns[car])

        return self.direction_x

    def get_row(self, output):
        for line in output.index:
            for car in self.cars:
                if output['car'][line] == self.cars[car].car_id:
                    if self.cars[car].orientation == 'H':
                        self.direction_y.append(self.rows[car])
                    else:
                        self.rows[car] -= output['move'][line]
                        self.direction_y.append(self.rows[car])

        return self.direction_y

    def get_car(self, output):
        for line in output.index:
            self.car_move.append(f"car{output['car'][line]}")

        return self.car_move

    def animating(self, i):
        for cars in self.dict_cars:
            if self.car_move[i] == cars:
                self.dict_cars[cars].set_xy([self.direction_x[i], self.direction_y[i]])

        return self.dict_cars[cars]

#------------------------------------------------------------
# Set up initial state
animates = Animate('12x12_7', 12)
output = animates.import_output_file()
game = animates.import_game_file()
animates.reset_cars()
animates.get_car_info(game)
animates.reset_cars()
dict_cars = animates.define_cars()
rows = animates.save_row()
columns = animates.save_column()
direction_x = animates.get_column(output)
direction_y = animates.get_row(output)
car_move = animates.get_car(output)

#------------------------------------------------------------
# set up figure and animation
plot = animates.create_plot()
plt = plot[0]
fig = plot[1]
ax = plot[2]

def init():
    # Based on https://note.nkmk.me/en/python-dict-keys-values-items/
    # Adds the cars to the board
    for cars in dict_cars.values():
        ax.add_patch(cars)
    for cars in dict_cars.values():
        return cars

def animation(i):
    for cars in dict_cars:
        if car_move[i] == cars:
            dict_cars[cars].set_xy([direction_x[i], direction_y[i]])
        #print(self.dict_cars[cars])
    return cars

interval = 1 / len(direction_x)

rushHour = FuncAnimation(fig, animation, frames = len(direction_x), interval = interval,
                         init_func = init, repeat = False)

plt.show()