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

from queue import Queue
from rushhour import Rushhour
from board import Board
from copy import deepcopy


def breadth_first_search(game):        
    queue = []
    visited = set()
    current_state = deepcopy(game.board)
    queue.append(current_state)
    visited.add(current_state)

    while len(queue) > 0:
        current_state = queue.pop(0)
        if is_solved(current_state):
            return True
        else:
            moves = list(range(-(game.size - 1), game.size -1, 1))
            exclude_zero = {0}
            moves = list(num for num in moves if num not in exclude_zero)

            for car in current_state.cars: 
                temp_car = current_state.car             
                for move in moves:
                    command = f"{temp_car} {move}"
                    if current_state.is_valid(command, temp_car, temp_car.car_id):
                        # temp_car = game.move_car(move)
                        print(temp_car)

def is_solved(self, game) -> bool:
    """Checks if case is solved (checks if red car is in position) """
    # This is inspired by the is_won function of schuifpuzzel.py
    # Go through all cars
    for i in range (len(game.cars)):
        # Get the row of the red car and save it in a variable
        row_x: int
        row_x = int(game.cars['X'].row)
                      
    #             if new_state not in visited:
    #                     current_state = deepcopy(new_state)
    #                     queue.append(current_state, move)
    #                     visited.add(current_state)


                


    #         current_state = game.board
    #         queue.append(current_state)
    #         visited.add(current_state)
    #         print(game.size)

    #         # for move in moves:























    # # while queue:
    # #     current_state = queue.pop(0)
    # #     if game.board.is_solution(current_state):
    # #         return current_state
    # #     for next_state in .board.chart_moves(current_state):
    # #         if next_state not in visited:
    # #             queue.append(next_state)
    # #             visited.append(next_state)
    # # return None



