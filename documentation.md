# Tic-Tac-Toe practical task Nr.1
Using Minimax, implement an AI to play Tic-Tac-Toe optimally.

## Understanding
There are two main files in this project: runner.py and tictactoe.py. tictactoe.py contains all of the logic for playing the game, and for making optimal moves. runner.py contains all of the code to run the graphical interface for the game.

The explanation of each function and how to run the program are available in the `README.md`. But as the most interested function is the `minimax`, let's focus on it little bit more.

The `minimax` function is a recursive algorithm for finding the optimal action for the current player in a game of Tic-Tac-Toe while using alpha-beta pruning to improve efficiency. It begins by determining whether the current player is X or O. If the current player is X (the maximizing player), it initializes variables for tracking the best score, best action, alpha (initially negative infinity), and beta (initially positive infinity). It then iterates through possible actions, recursively evaluating the resulting game states using the `max_value` and `min_value` functions. Alpha-beta pruning is employed to prune branches of the game tree when it is clear that the current player's strategy cannot be improved. The algorithm maintains and updates alpha (the maximum lower bound of possible scores) and beta (the minimum upper bound of possible scores) during the search. If the current player is O (the minimizing player), the process is similar, but it aims to minimize the score while updating alpha and beta accordingly. Ultimately, the function returns the best action for the current player, which represents the optimal move given the current state of the game and the opponent's potential moves. This approach efficiently searches through the game tree to make informed decisions while avoiding unnecessary exploration of unpromising branches.

In the context of Tic-Tac-Toe and the minimax algorithm, "X" is often considered the maximizing player because "X" typically starts the game. The player who makes the first move in a game usually aims to maximize their chances of winning, and the minimax algorithm is designed to help them achieve that goal.

I created this function inspired by https://www.hackerearth.com/blog/developers/minimax-algorithm-alpha-beta-pruning/. 