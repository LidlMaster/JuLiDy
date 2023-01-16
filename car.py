class Car:
    def __init__(self, id, orientation, column, row, length) -> None:
        # Create car object with variables read in from input file
        self.car_id = id
        self.orientation = orientation
        self.column = int(column) - 1
        self.row = int(row) - 1
        self.length = int(length)


    def __str__(self):
        return f"ID: {self.car_id}, Orientation: {self.orientation}, Column: {self.column}, Row: {self.row}, Length: {self.length}"
