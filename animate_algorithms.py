# Import libraries
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
from matplotlib import animation
import pandas as pd
from car import Car
import random

class Animate:
    
    def __init__(self, game_name, size) -> None:
        self.game_name = game_name
        self.size = size
        self.cars = {}

    def import_output_file(self):
        output = pd.read_csv('output.csv')
        return output

    def import_game_file(self):
        game = f"gameboards/Rushhour{self.game_name}.csv"
        return game

    def create_plot(self, dict_cars):
        fig, ax = plt.subplots()
        ax.set_xlim(1, self.size + 1)
        ax.set_ylim(1, self.size + 1)

        if self.size % 2 == 0:
            ax.plot([self.size + 1, self.size + 1], [(self.size + 2) / 2, (self.size + 2) / 2 + 1],
                     color = "black")
        else:
            ax.plot([self.size + 1, self.size + 1], [(self.size + 1) / 2 + 1, (self.size + 1) / 2 + 2],
                     color = "black")

        for cars in dict_cars.values():
            ax.add_patch(cars)

        return plt

    def get_car_info(self, file):
        with open(file) as f:
            next(f)
            for line in f:
                if not line.strip():
                    break
                data = line.strip().split(",")
                car = Car(data[0], data[1], data[2], data[3], data[4])
                self.cars[data[0]] = car

    def define_cars(self):
        dict_cars = {}
        for car in self.cars:
            r = random.random()
            g = random.random()
            b = random.random()
            colour = (r, g, b)
            if self.cars[car].orientation == 'H' and self.cars[car].car_id != 'X':
                dict_cars["car{0}".format(self.cars[car].car_id)] = Rectangle((self.cars[car].column, 
                                                        self.size + 1 - self.cars[car].row),
                                                        self.cars[car].length, 1, color = colour)
            elif self.cars[car].car_id == 'X':
                dict_cars["carX"] = Rectangle((self.cars[car].column, self.size + 1 - self.cars[car].row),
                                 2, 1, color = 'red')
            else:
                dict_cars["car{0}".format(self.cars[car].car_id)] = Rectangle((self.cars[car].column, 
                                                        self.size + 1 - self.cars[car].row), 1,
                                                        self.cars[car].length, color = colour)
        return dict_cars

    
    # def add_cars(self, dict_cars, ax):
    #     for key in dict_cars:
    #         ax.add_patch(key)

    
if __name__ == "__main__":
    animate = Animate('6x6_1', 6)
    output = animate.import_output_file()
    game = animate.import_game_file()
    animate.get_car_info(game)
    dict_cars = animate.define_cars()
    plt = animate.create_plot(dict_cars)
    plt.show()