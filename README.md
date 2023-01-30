# JuLiDy's comparing differnt algorithms for solving Rush Hour 
Authors: Judith Hellingman, Dylan Meegdes and Lisl Meester.

The goal of the game Rush Hour is to free the red car so it can exit at a specified edge of the board. This is done by moving the other cars that may be obstructing the exit. 

![](https://github.com/LidlMaster/JuLiDy/blob/main/animation.gif)

## Experiment
The goal of this project is to find an alogorithm that can solve given Rush Hour board configuartions and solve the problem in least number of moves possible. To find this algorithm an experiment will be conducted in which a few promissing algorithms will be constructed and compared to a baseline and to eachother, to find the most efficient one.

In this experiment the baseline algorithm used is a random algorithm that selectes random vehicles on the borards and tries to move them one space in a random direction until solved.

For the experimenta algorithms the following strategies will be used:
- non-naïve random algorithm with a move cap
- Breadth-First Search algorithm (BFS)
- Depth-First Search algorithm (DFS)

## File Format
The board configurations of the given Rush Hour problems a given in the foorms of .csv files. The filenames of which contain the boardsizes and the board number. These are used during initiating the game to selct the correct file and generating the correct boardsize.

Each file contains the following:
Each row has 5 elements. The first number contains carId followed by a letter that describes car-orientation (either "h" (horizontal) or "v" (vertical)). The next two variables form the coördinates on the board, with collumn and row and lastly the carlenght.

## Instructions running algorithms:
To run correctly run the algorithms the usage is as follows.
Firstly to select a board a you must choose a file and use the size an undercore and board the number at the end of the filename.
Possible sizes being : 6x6, 9x9 and 12x12. 
And with 7 different boards to choose form in this repository

The differnt algoritmes are categorised in the code as modes. 
The modes being: Manual (H), Baseline/Random (R), non-naïve Random (E), BFS (B), DFS (D).

An example for a correct command would be:
"$python3 main.py 6x6_3 R"

## Instructions generating animations:
To animate an experimental run the first thing to do is run the algorithm using the command as explained above.
After which you need to change the input in the animate function on line 232. Lastly run the the animate code the following using command:

"$python3 animate_algorithms.py"

## Instructions generating results:
To generate reliable results the algorithms need to be run more than once. Because of that code was implemented in a sperate file, specificly to run an algorithm a thousand times and collect the result in a excel sheet. 
To run this code the following example command can be used:

"$python3 results.py 6x6_3 R"

To access different algorithms and boardconfiguartions use commands as earlier stated above.



