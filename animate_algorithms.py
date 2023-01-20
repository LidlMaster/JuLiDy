# Import libraries
import matplotlib.pyplot as plt # type: ignore
from matplotlib.patches import Rectangle # type: ignore
from matplotlib import animation 
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

    def create_plot(self, dict_cars: Dict[str, Rectangle]) -> Any:
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

        # Based on https://note.nkmk.me/en/python-dict-keys-values-items/
        # Adds the cars to the board
        for cars in dict_cars.values():
            ax.add_patch(cars)

        # Returns the full board with the cars added
        return plt

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

    def define_cars(self) -> Dict[str, Rectangle]:
        """Defines the colour, size and location of the cars (Rectangles).
        Post: dict_cars is a dictionary with a string (key) and a Rectangle type
        """
        # Create empty dict
        dict_cars = {}

        # Iterate over all the cars
        for car in self.cars:
            # Add one to column and row, this was subtracted in the Car class
            self.cars[car].column += 1
            self.cars[car].row += 1

            # Based on https://www.adamsmith.haus/python/answers/how-to-generate-a-random-color-for-a-matplotlib-plot-in-python
            # Get a random colour
            r = random.random()
            g = random.random()
            b = random.random()
            colour = (r, g, b)

            # Check orientation, size and/or car_id
            if self.cars[car].orientation == 'H' and self.cars[car].car_id != 'X':
                # Define the size, name, colour and location of the horizontally placed cars (not X)
                dict_cars["car{0}".format(self.cars[car].car_id)] = Rectangle((self.cars[car].column, 
                                                        self.size + 1 - self.cars[car].row),
                                                        self.cars[car].length, 1, color = colour)
            elif self.cars[car].car_id == 'X':
                # Define the location of car X and set colour to red
                dict_cars["carX"] = Rectangle((self.cars[car].column, self.size + 1 - self.cars[car].row),
                                 2, 1, color = 'red')
            elif self.cars[car].length == 3 and self.cars[car].orientation == 'V':
                # Define the location and colour of trucks located vertically
                dict_cars["car{0}".format(self.cars[car].car_id)] = Rectangle((self.cars[car].column, 
                                                        self.size - 1 - self.cars[car].row), 1,
                                                        3, color = colour)
            else:
                # Define the location, colour and name of the vertically located cars
                dict_cars["car{0}".format(self.cars[car].car_id)] = Rectangle((self.cars[car].column, 
                                                        self.size - self.cars[car].row), 1,
                                                        self.cars[car].length, color = colour)

        # Return the dictionary
        return dict_cars
    
if __name__ == "__main__":
    animate = Animate('6x6_1', 6)
    output = animate.import_output_file()
    game = animate.import_game_file()
    animate.get_car_info(game)
    dict_cars = animate.define_cars()
    plt = animate.create_plot(dict_cars)
    plt.show()