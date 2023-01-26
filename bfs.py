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


def breadth_first_search(self, game):        
    queue = []
    visited = set()
    current_state = deepcopy(game.board)
    queue.append(current_state, None)
    visited.add(current_state)

    move = list(range(game.size))


    for move in moves:
        if move.is_valid():
            new_state = game.board(move)
                
        if new_state not in visited:
                current_state = deepcopy(new_state)
                queue.append(current_state, move)
                visited.add(current_state)


        


    initial_state = game.board.get_board_state()

    queue.append(initial_state)
    while queue:
        current_state = queue.pop(0)
        if self.board.is_solution(current_state):
            return current_state
        for next_state in self.board.chart_moves(current_state):
            if next_state not in visited:
                queue.append(next_state)
                visited.append(next_state)
    return None



