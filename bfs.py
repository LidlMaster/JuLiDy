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
    queue.append(game)
    visited.add(game)

    while len(queue) > 0:
        # print("begin")
        current_state = queue.pop(0)
        if current_state.is_solved():
            print("Solved!")
            exit(1)

        print(current_state.board)
        print(" ")
        
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
                    # print(len(visited))
                    # print(len(queue))   
                    
                    _str = str(temp_game.board)
                    if _str not in visited:
                        # print("123")
                        # print(len(visited))
                        # print(len(queue))
                        visited.add(_str)
                        queue.append(temp_game)
                        
        # print(queue)

    return False

            # # remove car from current position
            # game.board[temp_car.row][temp_car.column] = '__'
            # # update car position
            # temp_car.row += move
            # temp_car.column += move
            # # add car to new position
            # game.board[temp_car.row][temp_car.column] = temp_car.car_id

                        
# def is_solved(current_state) -> bool:
#     """Checks if case is solved (checks if red car is in position) """
#     # This is inspired by the is_won function of schuifpuzzel.py
#     # Go through all cars
#     for i in range (len(current_state.cars)):
#         # Get the row of the red car and save it in a variable
#         row_x: int
#         row_x = int(current_state.cars['X'].row)
#         if current_state.board.board[row_x][-2] == "X" and current_state.board.board[row_x][-1] == "X":
#             return True

                      
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



