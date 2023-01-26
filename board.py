import numpy as np # type: ignore
from typing import Any

class Board:
    def __init__(self, size: int) -> None:
        # Create square grid with size dependend on input file
        # Default grid has no cars and will be depicted with only '_' for empty spaces
        self.board: Any
        self.board = np.array([['__' for j in range(size)] for i in range(size)])


    def __repr__(self) -> str:
        return "\n".join(" ".join(row.ljust(3) for row in sublist) for sublist in self.board)

    def chart_moves(self, current_state: np.ndarray) -> List[np.ndarray]:
        possible_moves = []
        for i, row in enumerate(current_state):
            for j, spot in enumerate(row):
                if spot != '__':
                    car = self.cars[spot]
                    if car.orientation == 'H':
                        if j > 0 and current_state[i][j-1] == '__':
                            new_state = current_state.copy()
                            new_state[i][j-1] = spot
                            new_state[i][j+car.length-1] = '__'
                            possible_moves.append(new_state)
                        if j+car.length < len(row) and current_state[i][j+car.length] == '__':
                            new_state = current_state.copy()
                            new_state[i][j+car.length] = spot
                            new_state[i][j] = '__'
                            possible_moves.append(new_state)
                    elif car.orientation == 'V':
                        if i > 0 and current_state[i-1][j] == '__':
                            new_state = current_state.copy()
                            new_state[i-1][j] = spot
                            new_state[i+car.length-1][j] = '__'
                            possible_moves.append(new_state)
                        if i+car.length < len(current_state) and current_state[i+car.length][j] == '__':
                            new_state = current_state.copy()
                            new_state[i+car.length][j] = spot
                            new_state[i][j] = '__'
                            possible_moves.append(new_state)
        return possible_moves

