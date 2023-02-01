# Import libraries
import random
from typing import Dict, TypeVar

# Make typevar hints for self
Self = TypeVar("Self", bound="Random")

class Random:
    def random_selection(self: Self, dictionary: Dict[str, int]) -> str:
            """
            Randomly choose vehicle to move.
            """
            random_vehicle = random.choice(list(dictionary.keys()))
            return random_vehicle

    def random_movement(self) -> int:
        """
        Randomly choose direction to move.
        """
        # Make a list of moves (1 step) and randomly choose
        options = [-1,1]
        random_move = random.choice(options)
        
        return random_move

    def make_move(self, vehicle: str, move: int) -> str:
        """Returns the randomly chosen command"""
        return f"{vehicle} {move}"
    
