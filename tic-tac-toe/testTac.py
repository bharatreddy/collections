import gamePerfect
# set the object to begin the game
gmObj = gamePerfect.TicTacToe()
# We are assuming 'X' is the computer
# and 'O' is the user.
# Loop until someone wins the game
start = input('Do you want to start (Y/N) : ')
if start.upper() == 'Y':
    currUser = 'O'
else:
    currUser = 'X'
while not gmObj.check_winner():
    if currUser == 'O':
        step = input('Enter the step : ')
        gmObj.board[step] = currUser
        currUser = 'X'
    else:
        step = gmObj.get_next_move('X')
        gmObj.board[step[1]] =  currUser
        currUser = 'X'