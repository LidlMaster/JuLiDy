from queue import LifoQueue
from code.classes.rushhour import Rushhour
from code.classes.board import Board
from copy import deepcopy
from random import shuffle
from typing import List, Any, Set

def depth_first_search(game: Rushhour) -> bool:
    """Implements a depth first search algorithm to solve rushhour."""
    # Create the stack
    stack: LifoQueue[Any]
    stack = LifoQueue() # Use a stack instead of a queue
    stack.put(game)

    # Create list  and set to keep track of the previous state spaces and moves
    history: List[List[Any]]
    history = [[]]
    visited: Set[str]
    visited = set()
    visited.add(str(game.board))

    while not stack.empty():
        # Get the right state
        current_state = stack.get()
        current_history = history.pop()

        # Check if solved
        if current_state.is_solved():
            print("Solved!")
            # Print end board and number of moves and state spaces
            print(current_state.board)
            print("Moves:", len(current_history))
            print("State spaces:", len(visited))
            
            # Saving made moves in outputfile
            fieldnames =game.make_field_names()

            for command in current_history:
                game.update_dict(command) 

            game.give_output("output.csv", fieldnames)             
            exit(1)

        # Check if number of moves are above 35,000
        if len(current_history) > 35000:
            continue
        
        # Get the possible moves
        moves = list(range(-(game.size - 1), game.size -1, 1))
        exclude_zero = {0}
        moves = list(num for num in moves if num not in exclude_zero)

        # Shuffle to get a different order of the cars
        cars = list(current_state.cars.keys())
        shuffle(cars)

        # Go through each car
        for car in cars:
            # Shuffle the moves and save the current state
            temp_car = deepcopy(current_state.cars[car])
            shuffle(moves)

            # Go through each move
            for move in moves:
                # Create the command
                command = f"{temp_car.car_id} {move}"

                # Check if move is valid
                if current_state.is_valid(command, temp_car, temp_car.car_id):
                    # Move the car and save the current statespace
                    temp_game = deepcopy(current_state) 
                    temp_game.move_cars(command, "B") 
                    _str = str(temp_game.board)

                    # Check if already visited
                    if _str not in visited:
                        # Add to visited and history
                        visited.add(_str)
                        stack.put(temp_game)
                        history.append(current_history + [command])

    return False
