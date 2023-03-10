from code.classes.rushhour import Rushhour
from code.algorithms.baseline import Random
from sys import argv
from code.algorithms.bfs import breadth_first_search
from code.algorithms.dfs import depth_first_search


if __name__ == "__main__":
    # Check command line arguments and respond with usage in case of wrong input
    if len(argv) not in [2, 3]:
        print("Usage: python main.py <Size>x<Size>_boardnumber")
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

    # Count number of commands
    comm = 0

    # Start game
    while True:
        # Run naive random algorithm
        if mode == "R":
            if comm == 0:
                print(rushhour.place_cars())

            # Prompt input from user or algorithm 
            vehicle = algorithm.random_selection(rushhour.cars)
            afstand = algorithm.random_movement()
            command = algorithm.make_move(vehicle, afstand)
            comm += 1
            # Uses input command to move selected vehicle
            rushhour.move_cars(command, mode)

            # Checks if game is solved and ends game
            if rushhour.is_solved():
                rushhour.give_output(file, field_names)
                print("Won in", rushhour.get_moves(file), "moves")
                print("And with", comm, "commands")
                # from animate_algorithms import Animate
                break  

        # Run non-naive random algorithm
        elif mode == "E":
            if comm == 0:
                print(rushhour.place_cars())

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
                    print("Won in", rushhour.get_moves(file), "moves")
                    print("And with", comm, "commands")
                    # from animate_algorithms import Animate
                    break

                # Reset if number of moves is bigger than the cap
                elif len(dict) >= 30000:
                    rushhour = Rushhour(game_name, size)
                    algorithm = Random()
                    dict = rushhour.dict
                    rushhour.place_cars()
                    comm = 0
            break

        # Move manually
        elif mode == "H":
            print(rushhour.place_cars())
            # Promts User for move input
            command = input("Welke auto wil je waarheen bewegen?").upper()
            comm += 1
            # Uses input command to move selected vehicle
            rushhour.move_cars(command, mode)

            # Checks if game is solved and ends game
            if rushhour.is_solved():
                rushhour.give_output(file, field_names)
                print("Won in", rushhour.get_moves(file), "moves")
                print("And with", comm, "commands")
                break

        elif mode == "B":
            # Runs breadth first search algorithm
            print(rushhour.place_cars())
            breadth_first_search(rushhour)

        elif mode == "D":
            # Runs depth first search algorithm
            print(rushhour.place_cars())
            depth_first_search(rushhour)

        else:
            print("invalid mode, valid modes are H, R, E, B or D.")   
            break         
