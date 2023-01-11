class Board:
    def __init__(self, size):
        self.board = [['_' for j in range(size)] for i in range(size)]

    def __repr__(self):
        return "\n".join([" ".join(row) for row in self.board])
