# Breadth_First_Serach( Graph, X ) // Here, Graph is the graph that we already have and X is the source node

# Let Q be the queue
# Q.enqueue( X ) // Inserting source node X into the queue
# Mark X node as visited.

# While ( Q is not empty )
# Y = Q.dequeue( ) // Removing the front node from the queue

# Process all the neighbors of Y, For all the neighbors Z of Y
# If Z is not visited, Q. enqueue( Z ) // Stores Z in Q
# Mark Z as visited

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


def breadth_first_search(game):        
    queue = []
    visited = set()
            

    current_state = game.board
    queue.append(current_state)
    visited.add(current_state)
    print(game.size)

    # for move in moves:























    # while queue:
    #     current_state = queue.pop(0)
    #     if game.board.is_solution(current_state):
    #         return current_state
    #     for next_state in .board.chart_moves(current_state):
    #         if next_state not in visited:
    #             queue.append(next_state)
    #             visited.append(next_state)
    # return None



