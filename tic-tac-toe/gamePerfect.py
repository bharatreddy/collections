class TicTacToe(object):
    """
    A class for playing TicTacToe using 
    the Minimax algorithm.
    """
    def __init__(self):
        # set up the board. We'll use an array of length 9 (3x3)
        # to represent the board. The layout is shown below
        # 0 | 1 | 2
        # 3 | 4 | 5
        # 6 | 7 | 8
        # Also we'll use 'X', 'O' to represent the players
        # empty slots will be represented using #.
        self.board = ''.join( [ '#' for i in range(9) ] )