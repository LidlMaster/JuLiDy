import numpy as np

class Board:
    def __init__(self, size):
        # Create square grid with size dependend on input file
        # Default grid has no cars and will be depicted with only '_' for empty spaces
        self.board = np.array([['_' for j in range(size)] for i in range(size)])

    def __repr__(self):
        return "\n".join([" ".join(row) for row in self.board])
