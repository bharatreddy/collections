def get_score(winner):
    # scoring system according to minimax algo.
    # If the winner is the computer, return a score
    # of +1, if opponent wins give a score of -1, else
    # if its a draw return 0.
    if winner == 'computer':
        return 1
    elif winner == 'opponent':
        return -1
    else:
        return 0