from typing import Any

class Board:
    def __init__(self, size: int) -> None:
        """Initialize"""
        # Create square grid with size dependend on input file
        # Default grid has no cars and will be depicted with only '_' for empty spaces
        self.board: Any
        self.board = [['__' for j in range(size)] for i in range(size)]

    def __repr__(self) -> str:
        """Get board"""
        return "\n".join(" ".join(row.ljust(3) for row in sublist) for sublist in self.board)


