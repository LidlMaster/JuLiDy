import random
from typing import Dict
from rushhour import Rushhour

class Efficient_Random:
    def random_selection(self, dictionary: Dict):
            """
            Randomly choose vehicle to move.
            """
            random_vehicle = random.choice(list(dictionary.keys()))
            return random_vehicle

    def random_movement(self, game):
        """
        Randomly choose direction and distance to move.
        """
        options = range(-(game.size - 1), game.size -1, 1)
        random_move = random.choice(options)
        
        return random_move

    def make_move(self, vehicle, move):
        return f"{vehicle} {move}"
    
