import random
import main

class Random:
    def __init__(self):
        self.command_list= []
        
    def random_selection(self):
        """
        Randomly choose vehicle to move.
        """
        random_vehicle = random.choice(main.rushhour.cars.carid)
        return random_vehicle

    def random_movement(self):
        """
        Randomly choose distance to move.
        """
        options = [-1,1]
        random_move = random.choice(options)
     
        # options = [range(-(len(main.board.board), len(main.board.board), 1))]
        # random_move = random.choice(options)
        return random_move

    def make_move(self, vehicle, move):
        self.command_list.append(f"{vehicle} {move}")


# if __name__ == "__main__":
#     algorithm = Random()

#     i = 0
#     while i < 3:
#         commands = algorithm.make_move(algorithm.random_selection(), algorithm.random_movement())
#         i += 1

#     print(commands)

    
