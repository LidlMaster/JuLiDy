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
        states = queue.pop(0)
        if game.is_solved():
            return True
        else:
            moves = list(range(-(game.size - 1), game.size -1, 1))
            exclude_zero = {0}
            moves = list(num for num in moves if num not in exclude_zero)

            for car in game.cars: 
                temp_car = car             
                for move in moves:
                    command = f"{temp_car} {move}"
                    if game.is_valid(command, car, car):
                        # temp_car = game.move_car(move)
                        print(temp_car)

                        
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



