# JuLiDy's comparing different algorithms for solving Rush Hour 
Authors: Judith Hellingman, Dylan Meegdes and Lisl Meester.

The goal of the game Rush Hour is to free the red car so it can exit at a specified edge of the board. This is done by moving the other cars that may be obstructing the exit. 

![](https://github.com/LidlMaster/JuLiDy/blob/main/animations/animation.gif)

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
_< $python3 main.py 6x6_3 R" >_

To install requirements for this project use the following command:

_< pip install -r requirements.txt >_

This will install the extensions matplotlib en pandas.

## Instructions generating animations:
To animate an experimental run the first thing to do is run the algorithm using the command as explained above.
After which you need to change the input in the animate function on line 232. Lastly run the the animate code the following using command:

_< $python3 animate_algorithms.py >_

## Instructions generating results:
To generate reliable results the algorithms need to be run more than once. Because of that code was implemented in a sperate file, specificly to run an algorithm a thousand times and collect the result in a excel sheet. 
To run this code the following example command can be used:

_< $python3 results.py 6x6_3 R >_

To access different algorithms and boardconfiguartions use commands as earlier stated above.

## Results
After running the planned experiments a few interesting results were found. Firstly when comparing the results of the different random algorithm implementations in figure 1, a difference can be found between the algorithm with an implemented move limiter and the other ranodm algorithms. This is a logical result seeing as a manual cap has been implemented on the ammount of moves that can be performed. What is more dissapointing however is the lack of difference between te baseline random algorithm and the non-naive algorithm. We had predicted that the non-naive random algorithm would be significantly more efficient in solving a game, because it is able to move a vehicle more then one space at a time. This would allow a vehicle to perform a move that would take the baseline random algorithm two or more moves to achieve. But Figure 1 clearly shows no significant difference between these two algorithms.

![](https://github.com/LidlMaster/JuLiDy/blob/main/figures/Means%20of%20random%20algorithms.png)
_Figure 1: In this graph the results of the differnt means of the number of moves preformed during a game from the variations of the random algorithm can be seen compared. In order to calculate these means the algorithms were run a thousand times._

Another insteresting result can be seen in figure 2. When comparing a BFS and DFS algorithms, it is clearly shown that a BFS algorithms can find a path to a solution that is more efficient in number of moves. It also shows that at least in our case a BFS can be performed on a bigger board without needing more RAM memory space to find a solution. Hoever both a BFS and DFS took more RAM memoryspace than was available on our computers when trying to solve game 9x9_5 or more complicated or games with a bigger sized board. What also can be concluded is hat both BFS and DFS agorithms are more efficient in terms of number of moves compared to ay of the random algorithms. Seeing as the number of moves performed by the BFS and DFS algorithms stays under 2500, the lowest number of moves preformed by the non-naive random algrithm on game 6x6_2. But while the number of moves is more efficient, it can also clearly be seen that the random algorithms are far more efficient processingwise. As the random algorithms can solve al the boards a 1000 times without going over the RAM memory limit, while the DFS kills its proces from board 4 or higher and the bfs algorithms kills the proces from board 5 and higher.

![](https://github.com/LidlMaster/JuLiDy/blob/main/figures/Means%20of%20bfs%20and%20dfs%20algorithms.png)
_Figure 2: In this graph the results of the the number of moves preformed during a game from the Breadth-First Search and Depth-First serach algorithms can be compared. Because these algorithms will alway look for similar paths this code was only run once top obtain these resuts._

![](https://github.com/LidlMaster/JuLiDy/blob/main/figures/Random%20mean%20vs%20median.png)
_Figure 3: In this graph the the mean different moves and the median number of moves form the baseline random algorithm can be compared. In order to calculate these results the algorithms were run a thousand times._

![](https://github.com/LidlMaster/JuLiDy/blob/main/figures/Non-naive%20random%20mean%20vs%20median.png)
_Figure 4: In this graph the the mean different moves and the median number of moves form the non-naive random algorithm can be compared. To achieve a non-naive algorithm code was implemeted that makes it possible for the vehicles in the game to move more then one space at the time. In order to calculate these results the algorithms were run a thousand times._

![](https://github.com/LidlMaster/JuLiDy/blob/main/figures/Non-naive%20random%20cap%20mean%20vs%20median.png)
_Figure 5: In this graph the the mean different moves and the median number of moves form the non-naive random algorithm with a limit on how many moves can be performed can be compared. This limit was put on a cap of 30000 moves to get a efficient balance between efficient number of moves and a functional runtime. In order to calculate these results the algorithms were run a thousand times._