from rushhour import Rushhour
from board import Board
from car import Car
from baseline import Random
import random
# from animate_algorithms import Animate

# Baseline algorithm: Random
# ============================================================================================
# def random_selection():
#         """
#         Randomly choose vehicle to move.
#         """
#         print(rushhour.cars)
#         random_vehicle = random.choice(list(rushhour.cars.items()))
#         print(random_vehicle)
#         # id = random_vehicle.car_id
#         return id

# def random_movement():
#     """
#     Randomly choose distance to move.
#     """
#     options = [-1,1]
#     random_move = random.choice(options)

#     # options = [range(-5, 5), 1))]
#     # random_move = random.choice(options)

#     # options = [range(-(len(main.board.board), len(main.board.board), 1))]
#     # random_move = random.choice(options)
#     return random_move

# def make_move(vehicle, move):
#     return f"{vehicle} {move}"
# ============================================================================================


if __name__ == "__main__":

    from sys import argv

    # Check command line arguments and respond with usage in case of wrong input
    if len(argv) not in [2, 3]:
        print("Usage: python rushhour.py <Size>x<Size>_boardnumber")
        exit(1)

    # Load the requested game
    game_name = argv[1]

    # Checks if additional arguments are provided for how code should be ran
    if len(argv) == 2:
        # Default is player based input
        mode = "H"
    else: 
        # Else mode is based on additional argument (Currently H for "Hand" or R for "Random")
        mode = argv[2]

    # Strip input filename for size of board
    size = int(game_name[0])
    if game_name[1].isdigit():
        size = size * 10
        size += int(game_name[1])

    # Create board
    # board = Board(size)

    # Create game
    rushhour = Rushhour(game_name, size)
    algorithm = Random()

    # Create list of moves
    dict = rushhour.make_dict()
    field_names = rushhour.make_field_names()
    file = 'output.csv'

    print(rushhour.place_cars())
    comm = 0
    
    # Start game
    while True:
        if mode == "R" or mode == "r":
            # Prompt input from user or algorithm 
            vehicle = algorithm.random_selection(rushhour.cars)
            # print("v:",vehicle)
            afstand = algorithm.random_movement()
            # print("a:",afstand)
            command = algorithm.make_move(vehicle, afstand)
            comm += 1

            # Uses input command to move selected vehicle
            rushhour.move_cars(command, dict, mode)

            # Checks if game is solved and ends game
            if rushhour.is_solved():
                rushhour.give_output(file, field_names, dict)
                print("Won in", rushhour.get_moves(file), "moves")
                print("And with", comm, "commands")
                # from animate_algorithms import Animate
                break
                   
        elif mode == "H" or mode == 'h':
            command = input("Welke auto wil je waarheen bewegen?").upper()
            # Uses input command to move selected vehicle
            rushhour.move_cars(command, dict, mode)

            # Checks if game is solved and ends game
            if rushhour.is_solved():
                rushhour.give_output(file, field_names, dict)
                print("Won in", rushhour.get_moves(file), "moves")
                print("And with", comm, "commands")
                #from animate_algorithms import Animate
                break
