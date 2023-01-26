import random
from typing import Dict
# import main
from rushhour import Rushhour

class Random:
    def random_selection(self, dictionary: Dict):
            """
            Randomly choose vehicle to move.
            """
            # print(dictionary)
            random_vehicle = random.choice(list(dictionary.keys()))
            # print(random_vehicle)
            # id = random_vehicle.car_id
            return random_vehicle

    def random_movement(self, game):
        """
        Randomly choose distance to move.
        """
        # options = [-1,1]
        # random_move = random.choice(options)

        # options = [range(-5, 5, 1)]
        # random_move = random.choice(options)


        options = range(-(game.size - 1), game.size -1, 1)
        random_move = random.choice(options)
        
        return random_move

    def make_move(self, vehicle, move):
        return f"{vehicle} {move}"
    
