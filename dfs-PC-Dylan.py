from queue import LifoQueue
from rushhour import Rushhour
from board import Board
from copy import deepcopy

def depth_first_search(game):
    stack = LifoQueue() # Use a stack instead of a queue
    stack.put(game)
    history = [[]]
    visited = set()
    visited.add(str(game.board))
    while not stack.empty():
        current_state = stack.get() # Use the `get()` method instead of `pop(0)`
        current_history = history.pop()
        if current_state.is_solved():
            print("Solved!")
            print(current_state.board)
            print(current_history[:len(current_history)])
            print(len(current_history))
            print(len(visited))
            exit(1)

        if len(current_history) > 150:
            continue

        moves = list(range(-(game.size - 1), game.size -1, 1))
        exclude_zero = {0}
        moves = list(num for num in moves if num not in exclude_zero)

        for car in current_state.cars:    
            temp_car = deepcopy(current_state.cars[car])       
            for move in moves:
                command = f"{temp_car.car_id} {move}"
                if current_state.is_valid(command, temp_car, temp_car.car_id):
                    temp_game = deepcopy(current_state) 
                    temp_game.move_cars(command, "B") 
                    _str = str(temp_game.board)
                    if _str not in visited:
                        visited.add(_str)
                        stack.put(temp_game) # Use the `put()` method instead of `append()`
                        history.append(current_history + [command])

    return False
