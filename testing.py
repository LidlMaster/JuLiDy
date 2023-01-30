from rushhour import Rushhour
from board import Board
from baseline import Random
import random
from sys import argv
from bfs import breadth_first_search
from dfs import depth_first_search
import statistics


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
    file = 'output.csv'
    command_list = []
    move_list = []
    times = 0
    comm = 0

    # Start game
    while True:
        if mode == "R":
            while times <= 1000:
                if comm == 0:
                    print(rushhour.place_cars())
                # Prompt input from user or algorithm 
                vehicle = algorithm.random_selection(rushhour.cars)
                afstand = algorithm.random_movement(rushhour)
                command = algorithm.make_move(vehicle, afstand)
                comm += 1
                # Uses input command to move selected vehicle
                rushhour.move_cars(command, mode)
                # Checks if game is solved and ends game
                if rushhour.is_solved():
                    rushhour.give_output(file, field_names)
                    #print("Won in", rushhour.get_moves(file), "moves")
                    #print("And with", comm, "commands")
                    command_list.append(comm)
                    move_list.append(rushhour.get_moves(file))
                    times += 1
                    rushhour = Rushhour(game_name, size)
                    algorithm = Random()
                    dict = rushhour.dict
                    rushhour.place_cars()
                    comm = 0
                    #print(times)
                    # from animate_algorithms import Animate
                    break
            if times >= 1000: 
                mean_comm = statistics.mean(command_list)
                mean_move = statistics.mean(move_list)
                median_comm = statistics.median(command_list)
                median_move = statistics.median(move_list)
                stdev_comm = statistics.stdev(command_list)
                stdev_move = statistics.stdev(move_list)
                print("Gemiddeld", mean_comm, "commands")
                print("Mediaan", median_comm, "commands")
                print("Standaard deviatie", stdev_comm, "commands")
                print("Gemiddeld", mean_move, "moves")
                print("Mediaan", median_move, "moves")
                print("Standaard deviatie", stdev_move, "moves")
                break
                    
        elif mode == "E":
            while times <= 1000:
                # if comm == 0:
                #     print(rushhour.place_cars())
                # Start a while loop, to keep the number of moves under a given number
                while not rushhour.is_solved(): 
                    # Prompt input from user or algorithm 
                    vehicle = algorithm.random_selection(rushhour.cars)
                    # print("v:",vehicle)
                    afstand = algorithm.random_movement(rushhour)
                    # print("a:",afstand)
                    command = algorithm.make_move(vehicle, afstand)
                    comm += 1
                    # Uses input command to move selected vehicle
                    rushhour.move_cars(command, mode)
                    # Checks if game is solved and ends game
                    if rushhour.is_solved():
                        rushhour.give_output(file, field_names)
                        # print("Won in", rushhour.get_moves(file), "moves")
                        # print("And with", comm, "commands")
                        command_list.append(comm)
                        move_list.append(rushhour.get_moves(file))
                        times += 1
                        rushhour = Rushhour(game_name, size)
                        algorithm = Random()
                        dict = rushhour.dict
                        rushhour.place_cars()
                        comm = 0
                        print(times)
                        # from animate_algorithms import Animate
                        break
                    # Reset if number of moves is bigger than the cap
                    elif len(dict) >= 30000:
                        rushhour = Rushhour(game_name, size)
                        algorithm = Random()
                        dict = rushhour.dict
                        rushhour.place_cars()
                        comm = 0
            if times >= 1000: 
                mean_comm = statistics.mean(command_list)
                mean_move = statistics.mean(move_list)
                median_comm = statistics.median(command_list)
                median_move = statistics.median(move_list)
                stdev_comm = statistics.stdev(command_list)
                stdev_move = statistics.stdev(move_list)
                print("Gemiddeld", mean_comm, "commands")
                print("Mediaan", median_comm, "commands")
                print("Standaard deviatie", stdev_comm, "commands")
                print("Gemiddeld", mean_move, "moves")
                print("Mediaan", median_move, "moves")
                print("Standaard deviatie", stdev_move, "moves")
                break
            break
        elif mode == "H":
            print(rushhour.place_cars())
            # Promts User for move input
            command = input("Welke auto wil je waarheen bewegen?").upper()
            # Uses input command to move selected vehicle
            rushhour.move_cars(command, mode)

            # Checks if game is solved and ends game
            if rushhour.is_solved():
                rushhour.give_output(file, field_names)
                print("Won in", rushhour.get_moves(file), "moves")
                print("And with", comm, "commands")
                break
        elif mode == "B":
            print(rushhour.place_cars())
            breadth_first_search(rushhour)
        elif mode == "D":
            print(rushhour.place_cars())
            depth_first_search(rushhour)
        else:
            print("invalid mode, valid modes are H, R, E, B or D.")   
            break         
