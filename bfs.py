# Follow the below method to implement BFS traversal.

# Declare a queue and insert the starting vertex.
# Initialize a visited array and mark the starting vertex as visited.
# Follow the below process till the queue becomes empty:
# Remove the first vertex of the queue.
# Mark that vertex as visited.
# Insert all the unvisited neighbors of the vertex into the queue.
# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/


# BFS pseudocode:
# create a queue Q 
# mark v as visited and put v into Q 
# while Q is non-empty 
#     remove the head u of Q 
#     mark and enqueue all (unvisited) neighbours of u
# https://www.programiz.com/dsa/graph-bfs

#Judith Hellingman — vandaag om 11:00
# https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/breadth-first-search-bfs-algorithm/

from rushhour import Rushhour
from copy import deepcopy
from typing import List, Set

def breadth_first_search(game: Rushhour) -> bool:
    # Create the queue
    queue: List[str]
    queue = [game]

    # Create list and set to keep track of previous state spaces
    history: List[List[str]]
    history = [[]]
    visited: Set[str]
    visited = set()
    visited.add(str(game.board))

    while len(queue) > 0:
        # Get the right state
        current_state = queue.pop(0)
        current_history = history.pop(0)

        # Check if solved
        if current_state.is_solved():
            print("Solved!")
            # Print end board and the number of moves and state spaces
            print(current_state.board)
            print("moves:", len(current_history))
            print("state spaces:", len(visited))
            
            # Saving made moves in outputfile
            fieldnames =game.make_field_names()

            for command in current_history:
                game.update_dict(command) 

            game.give_output("output.csv", fieldnames)             
            exit(1)

        # Get possible moves
        moves = list(range(-(game.size - 1), game.size -1, 1))
        exclude_zero = {0}
        moves = list(num for num in moves if num not in exclude_zero)

        # Go through each car
        for car in current_state.cars:
            # Save the state space
            temp_car = deepcopy(current_state.cars[car])

            # Go through moves   
            for move in moves:
                # Get command
                command = f"{temp_car.car_id} {move}"

                # Check if command is valid
                if current_state.is_valid(command, temp_car, temp_car.car_id):
                    # Save the state space and move cars
                    temp_game = deepcopy(current_state) 
                    temp_game.move_cars(command, "B") 
                    _str = str(temp_game.board)

                    # Check if board is previously visited
                    if _str not in visited:
                        # Save state space
                        visited.add(_str)
                        queue.append(temp_game)
                        history.append(current_history + [command])

    return False