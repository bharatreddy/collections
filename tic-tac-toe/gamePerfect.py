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

    def check_winner(self):
        # Here we check if there is winner in the board.
        # Check the rows for winners.
        for i in range(3):
            if ( (self.board[i*3] == self.board[i*3+1]) and \
                (self.board[i*3] ==  self.board[i*3+2]) and self.board[i] != '-' ):
                return True
        # Check the columns for winners.
        for i in range(3):
           if ( (self.board[i] == self.board[i+3]) and \
                (self.board[i] ==  self.board[i+6]) and self.board[i] != '-' ):
                return True
        # Check the diagonal elements
        # There are two possibilities elements 0, 4 and 8 or 2, 4 and 6.
        if ( self.board[0] == self.board[4] and \
            self.board[4] == self.board[8] and self.board[4] != '-' ):
            return  True
        if ( self.board[2] == self.board[4] and \
            self.board[4] == self.board[6] and self.board[4] != '-' ):
            return  True