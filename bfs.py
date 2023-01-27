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
    history = []
    queue.append(game)
    visited.add(game)
    i = 0

    while len(queue) > 0:
        current_state = queue.pop(0)
        i += 1
        if current_state.is_solved():
            print("Solved!")
            print(current_state.board)
            print("History of moves: ", history)
            print("#moves: ", len(history))
            exit(1)
        
        moves = list(range(-game.size+1, game.size))
        exclude_zero = {0}
        moves = list(num for num in moves if num not in exclude_zero)

        for car in current_state.cars:    
            temp_car = deepcopy(current_state.cars[car])       
            for move in moves:
                command = f"{temp_car.car_id} {move}"
                if current_state.is_valid(command, temp_car, temp_car.car_id):

                    temp_game = deepcopy(current_state) 
                    temp_game.move_cars(command, "B") 
                    
                    _str = str(temp_game.board)
                    if _str not in visited:
                        visited.add(_str)
                        queue.append(temp_game)
                        history.append(command + history[i])
                        
        # print(queue)

    return False

                
























    # # while queue:
    # #     current_state = queue.pop(0)
    # #     if game.board.is_solution(current_state):
    # #         return current_state
    # #     for next_state in .board.chart_moves(current_state):
    # #         if next_state not in visited:
    # #             queue.append(next_state)
    # #             visited.append(next_state)
    # # return None



