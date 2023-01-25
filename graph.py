from queue import Queue

class Graph:
    # Constructor
    def __init__(self, num_of_nodes, directed=True):
        self.num_of_nodes = num_of_nodes
        self.nodes = range(self.m_num_of_nodes)
		
        # Directed or Undirected
        self.directed = directed
		
        # Graph representation - Adjacency list
        # We use a dictionary to implement an adjacency list
        self.neighbours = {node: set() for node in self.nodes}      
	
    # Add edge to the graph
    def add_edge(self, node1, node2, weight=1):
        self.neighbours[node1].add((node2, weight))

        if not self.directed:
            self.neighbours[node2].add((node1, weight))
    
    # Print the graph representation
    def print_adj_list(self):
      for key in self.neighbours.keys():
        print("node", key, ": ", self.neighbours[key])