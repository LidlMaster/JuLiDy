from car import Car
from board import Board

class Rushhour:

    def __init__(self, game):
        # Create dictionary of cars and load in cars form input file
        self.cars = {}
        self.load_cars(f"gameboards/Rushhour{game}.csv")

    def load_cars(self, filename):
        """ Read in input file, strip variables per car and stores it in a cars dictionary """
        with open(filename) as f:
            next(f)
            counter = 0
            for line in f:
                if not line.strip():
                    break
                data = line.strip().split(",")
                car = Car(data[0], data[1], data[2], data[3], data[4])
                self.cars[counter] = car
                print(self.cars[counter])
                counter+=1

    def place_cars(self):
        """ Place cars in constructed grid using coördinates and length from the cars dictionary """
        for car in self.cars:
            if self.cars[car].orientation == "H":
                for i in range(self.cars[car].column, self.cars[car].column + self.cars[car].length):
                    board.board[self.cars[car].row][i] = self.cars[car].car_id
            else:
                for i in range(self.cars[car].row, self.cars[car].row + self.cars[car].length):
                    board.board[i][self.cars[car].column] = self.cars[car].car_id

        return board
    
    def move_cars(self):
        """ Reads input commands to select car object and move it the input ammount of spaces. 
        Takes oriëntatin of car object into consideration for direction of movement. Cars can only move forward or backwards not sideways."""
        pass
    
    def is_valid(self):
        """ Checks if input move is valid """
        pass

    def is_solved(self):
        """Checks if case is solved (checks if red car is in position) """
        pass

if __name__ == "__main__":

    from sys import argv

    # Check command line arguments and respond with usage in case of wrong input
    if len(argv) != 2:
        print("Usage: python rushhour.py <Size>x<Size>_boardnumber")

    # Load the requested game
    game_name = argv[1]

    # strip input filename for size of board
    size = int(game_name[0])
    if game_name[1].isdigit():
        size = size * 10
        size += int(game_name[1])

    # Create board
    board = Board(size)

    # Create game
    rushhour = Rushhour(game_name)

    print(rushhour.place_cars())


    # for i in range(len(rushhour.cars)):
    #     print(rushhour.cars[i].car_id)
