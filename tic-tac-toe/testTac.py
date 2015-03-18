import gamePerfect
# set the object to begin the game
gmObj = gamePerfect.TicTacToe()
# We are assuming 'X' is the computer
# and 'O' is the user.
# Loop until someone wins the game
start = raw_input('Do you want to start (Y/N) : ')
if start.upper() == 'Y':
    currUser = 'O'
else:
    currUser = 'X'
while not gmObj.check_winner():
    if currUser == 'O':
        # get input from user and update the board
        step = input('Enter the step : ')
        # check if the spot entered by the user is already taken
        while gmObj.board[step] != '#':
            step = input('The spot you entered is filled, re-enter: ')
        gmObj.board[step] = currUser
        currUser = 'X'
    else:
        # get computer's step
        step = gmObj.get_next_move('X')
        gmObj.board[step[1]] =  currUser
        currUser = 'O'
        print 'Computer took the spot numbered-->', step[1]
    print 'current board-->', gmObj.board
# print the winner
if gmObj.get_winner() == 'X':
    print 'Computer won'
elif gmObj.get_winner() == 'O':
    print 'You won'
else:
    print 'GAME DRAW!!!'