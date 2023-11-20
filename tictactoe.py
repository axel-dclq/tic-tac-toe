"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_X = sum(row.count(X) for row in board)
    count_O = sum(row.count(O) for row in board)

    return X if count_X == count_O else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Initialize a set to store all the possible actions
    possible_actions = set()

    # Loop to get all the EMPTY possitions
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    
    # Security
    if board[i][j] != EMPTY:
        raise Exception("Invalid action")
    
    # Copy of the current board
    new_board = [row[:] for row in board]

    # Add the new action
    new_board[i][j] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows and columns for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]
    
    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None




def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # If there is a winner the game is ended
    if winner(board) is not None:
        return True
    
    # If the board is full the game is ended
    return all(cell is not EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board using alpha-beta pruning.
    """
    current_player = player(board)

    def max_value(board, alpha, beta):
        # Check if the game has ended or if a terminal state is reached
        if terminal(board):
            return utility(board)
        v = -math.inf
        for action in actions(board):
            # Recursively explore child nodes and evaluate their utility
            v = max(v, min_value(result(board, action), alpha, beta))
            alpha = max(alpha, v)
            # Prune if the beta value is less than or equal to the alpha value
            if beta <= alpha:
                break  # Beta cut-off
        return v

    def min_value(board, alpha, beta):
        # Check if the game has ended or if a terminal state is reached
        if terminal(board):
            return utility(board)
        v = math.inf
        for action in actions(board):
            # Recursively explore child nodes and evaluate their utility
            v = min(v, max_value(result(board, action), alpha, beta))
            beta = min(beta, v)
            # Prune if the beta value is less than or equal to the alpha value
            if beta <= alpha:
                break  # Alpha cut-off
        return v

    if current_player == X:
        # If the current player is X (maximizing player)
        best_score = -math.inf  # Initialize the best score as negative infinity
        best_action = None  # Initialize the best action as None
        alpha = -math.inf  # Initialize alpha as negative infinity (used for pruning)
        beta = math.inf  # Initialize beta as positive infinity (used for pruning)

        # Iterate through possible actions
        for action in actions(board):
            score = min_value(result(board, action), alpha, beta)  # Calculate the score using min_value
            if score > best_score:
                best_score = score  # Update the best score if a better score is found
                best_action = action  # Update the best action
            alpha = max(alpha, score)  # Update alpha with the maximum score found so far

        return best_action  # Return the best action for the maximizing player
    else:
        # If the current player is O (minimizing player)
        best_score = math.inf  # Initialize the best score as positive infinity
        best_action = None  # Initialize the best action as None
        alpha = -math.inf  # Initialize alpha as negative infinity (used for pruning)
        beta = math.inf  # Initialize beta as positive infinity (used for pruning)

        # Iterate through possible actions
        for action in actions(board):
            score = max_value(result(board, action), alpha, beta)  # Calculate the score using max_value
            if score < best_score:
                best_score = score  # Update the best score if a better score is found
                best_action = action  # Update the best action
            beta = min(beta, score)  # Update beta with the minimum score found so far

        return best_action  # Return the best action for the minimizing player


if __name__ == '__main__':
    board = [[X, X, O],
            [X, O, X],
            [O, X, O]]
    
    print(winner(board))