import random
from typing import Dict
# import main

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

    def random_movement(self):
        """
        Randomly choose distance to move.
        """
        options = [-1,1]
        random_move = random.choice(options)

        # options = [range(-5, 5), 1))]
        # random_move = random.choice(options)

        # options = [range(-(len(main.board.board), len(main.board.board), 1))]
        # random_move = random.choice(options)
        return random_move

    def make_move(self, vehicle, move):
        return f"{vehicle} {move}"
# ============================================================================================


# if __name__ == "__main__":
#     algorithm = Random()

#     i = 0
#     while i < 3:
#         commands = algorithm.make_move(algorithm.random_selection(), algorithm.random_movement())
#         i += 1

#     print(commands)

    
