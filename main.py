from rushhour import Rushhour
from board import Board
from car import Car

if __name__ == "__main__":

    from sys import argv

    # Check command line arguments and respond with usage in case of wrong input
    if len(argv) != 2:
        print("Usage: python rushhour.py <Size>x<Size>_boardnumber")
        exit(1)

    # Load the requested game
    game_name = argv[1]

    # strip input filename for size of board
    size = int(game_name[0])
    if game_name[1].isdigit():
        size = size * 10
        size += int(game_name[1])

    # Create board
    # board = Board(size)

    # Create game
    rushhour = Rushhour(game_name, size)

    print(rushhour.place_cars())
    
    # Start game
    while True:
        # Prompt input from user or algorithm 
        command = input("Welke auto wil je waarheen bewegen?").upper()

        # Uses input command to move selceted vehicle
        rushhour.move_cars(command)

        # Checks if game is solved and ends game
        if rushhour.is_solved():
            break

    
