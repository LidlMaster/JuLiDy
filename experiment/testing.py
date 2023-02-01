# Import libraries
from sys import argv
import statistics
import os
import sys
import inspect
from typing import List

# Import from different folder
currentdir: str
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from code.algorithms.dfs import depth_first_search
from code.algorithms.bfs import breadth_first_search
from code.algorithms.baseline import Random
from code.classes.rushhour import Rushhour

if __name__ == "__main__":
    # Check command line arguments and respond with usage in case of wrong input
    if len(argv) not in [2, 3]:
        print("Usage: python rushhour.py <Size>x<Size>_boardnumber")
        exit(1)

    # Load the requested game
    game_name = argv[1]

    # Checks if additional arguments are provided for how code should be ran
    if len(argv) == 2:
        # Default is player based input
        mode: str
        mode = "H"
    else: 
        # Else mode is based on additional argument (Currently H for "Hand" or R for "Random")
        mode = argv[2].upper()

    # Strip input filename for size of board
    size = int(game_name[0])

    if game_name[1].isdigit():
        size = size * 10
        size += int(game_name[1])

    # Create game
    rushhour = Rushhour(game_name, size)
    algorithm = Random()

    # Create list of moves
    dict = rushhour.dict
    field_names = rushhour.make_field_names()
    file: str
    file = 'output.csv'
    command_list: List[int]
    command_list = []
    move_list: List[int]
    move_list = []
    times: int
    times = 0
    comm: int
    comm = 0

    # Start game
    while True:
        # Checks if random needs to run
        if mode == "R":
            # Repeats 1000 times
            while times <= 1000:
                # Prompt input from user or algorithm 
                vehicle = algorithm.random_selection(rushhour.cars)
                afstand = algorithm.random_movement()
                command = algorithm.make_move(vehicle, afstand)
                comm += 1
                # Uses input command to move selected vehicle
                rushhour.move_cars(command, mode)

                # Checks if game is solved
                if rushhour.is_solved():
                    rushhour.give_output(file, field_names)

                    # Add the number of commands and the number of moves to their respective lists
                    command_list.append(comm)
                    move_list.append(rushhour.get_moves(file))

                    # Adds number of times and prints
                    times += 1
                    print(times)

                    # Resets game
                    rushhour = Rushhour(game_name, size)
                    algorithm = Random()
                    dict = rushhour.dict
                    rushhour.place_cars()
                    comm = 0
                    break

            # Checks if done
            if times >= 1000:
                # Calculates the mean, median and standard deviation of the commands and moves
                mean_comm = statistics.mean(command_list)
                mean_move = statistics.mean(move_list)
                median_comm = statistics.median(command_list)
                median_move = statistics.median(move_list)
                stdev_comm = statistics.stdev(command_list)
                stdev_move = statistics.stdev(move_list)

                # Prints the means, medians and standard deviation of the commands and mean
                print("Gemiddeld", mean_comm, "commands")
                print("Mediaan", median_comm, "commands")
                print("Standaard deviatie", stdev_comm, "commands")
                print("Gemiddeld", mean_move, "moves")
                print("Mediaan", median_move, "moves")
                print("Standaard deviatie", stdev_move, "moves")
                break

        # Checks if non-naive random needs to run
        elif mode == "E":
            # Runs 1000 times
            while times <= 1000:
                # Prompt input from user or algorithm 
                vehicle = algorithm.random_selection(rushhour.cars)
                afstand = algorithm.random_movement()
                command = algorithm.make_move(vehicle, afstand)
                comm += 1
                # Uses input command to move selected vehicle
                rushhour.move_cars(command, mode)

                # Checks if game is solved
                if rushhour.is_solved():
                    rushhour.give_output(file, field_names)
                    
                    # Adds number of moves and commands to their respective lists
                    command_list.append(comm)
                    move_list.append(rushhour.get_moves(file))

                    # Keeps track of the number of runs and prints this
                    times += 1
                    print(times)

                    # Resets game
                    rushhour = Rushhour(game_name, size)
                    algorithm = Random()
                    dict = rushhour.dict
                    rushhour.place_cars()
                    comm = 0

            # Checks if finished
            if times >= 1000:
                # Calculates the mean, median and standard deviation of the moves and commands
                mean_comm = statistics.mean(command_list)
                mean_move = statistics.mean(move_list)
                median_comm = statistics.median(command_list)
                median_move = statistics.median(move_list)
                stdev_comm = statistics.stdev(command_list)
                stdev_move = statistics.stdev(move_list)

                # Prints the previous gotten values
                print("Gemiddeld", mean_comm, "commands")
                print("Mediaan", median_comm, "commands")
                print("Standaard deviatie", stdev_comm, "commands")
                print("Gemiddeld", mean_move, "moves")
                print("Mediaan", median_move, "moves")
                print("Standaard deviatie", stdev_move, "moves")
                break
            break 

        # Checks if non-naive random with cap
        elif mode == "C":
            # Runs 1000 times
            while times <= 1000:
                # Start a while loop, to keep the number of moves under a given number
                while not rushhour.is_solved(): 
                    # Prompt input from user or algorithm 
                    vehicle = algorithm.random_selection(rushhour.cars)
                    # print("v:",vehicle)
                    afstand = algorithm.random_movement()
                    # print("a:",afstand)
                    command = algorithm.make_move(vehicle, afstand)
                    comm += 1
                    # Uses input command to move selected vehicle
                    rushhour.move_cars(command, mode)
                    # Checks if game is solved and ends game

                    if rushhour.is_solved():
                        rushhour.give_output(file, field_names)

                        # Add the number of moves and commands to their lists
                        command_list.append(comm)
                        move_list.append(rushhour.get_moves(file))

                        # Count the number of times and prints these
                        times += 1
                        print(times)

                        # Resets game
                        rushhour = Rushhour(game_name, size)
                        algorithm = Random()
                        dict = rushhour.dict
                        rushhour.place_cars()
                        comm = 0
                        break

                    # Reset if number of moves is bigger than the cap
                    elif len(dict) >= 30000:
                        rushhour = Rushhour(game_name, size)
                        algorithm = Random()
                        dict = rushhour.dict
                        rushhour.place_cars()
                        comm = 0

            # Checks if done
            if times >= 1000: 
                # Calculate the means, medians and standard deviations
                mean_comm = statistics.mean(command_list)
                mean_move = statistics.mean(move_list)
                median_comm = statistics.median(command_list)
                median_move = statistics.median(move_list)
                stdev_comm = statistics.stdev(command_list)
                stdev_move = statistics.stdev(move_list)

                # Prints these values
                print("Gemiddeld", mean_comm, "commands")
                print("Mediaan", median_comm, "commands")
                print("Standaard deviatie", stdev_comm, "commands")
                print("Gemiddeld", mean_move, "moves")
                print("Mediaan", median_move, "moves")
                print("Standaard deviatie", stdev_move, "moves")
                break
            break

        # Checks if breadth first search
        elif mode == "B":
            print(rushhour.place_cars())
            breadth_first_search(rushhour)

        # Checks if depth first search
        elif mode == "D":
            print(rushhour.place_cars())
            depth_first_search(rushhour)

        # Checks if invalid name is given
        else:
            print("invalid mode, valid modes are R, E, C, B or D.")   
            break         
