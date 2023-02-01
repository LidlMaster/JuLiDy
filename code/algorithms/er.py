import random
from typing import Dict
from code.classes.rushhour import Rushhour

class Efficient_Random:
    def random_selection(self, dictionary: Dict) -> str:
            """
            Randomly choose vehicle to move.
            """
            random_vehicle = random.choice(list(dictionary.keys()))
            return random_vehicle

    def random_movement(self, game: Rushhour) -> int:
        """
        Randomly choose direction and distance to move.
        """
        # Create a range of the moves possible and choose randomly
        options = range(-(game.size - 1), game.size -1, 1)
        random_move = random.choice(options)
        
        return random_move

    def make_move(self, vehicle: str, move: int) -> str:
        """"Return the command of the randomly chosen move"""
        return f"{vehicle} {move}"
    
