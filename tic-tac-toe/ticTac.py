from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route("/")
def starter():
    return render_template('ttt-index.html')

def next_move(board):
    # given the current board retreive the next move.
    # import the library
    import gamePerfect
    gmObj = gamePerfect.TicTacToe()
    # set the board
    gmObj.board = board
    # return computer's step
    step = gmObj.get_next_move('X')
    return step[1]

if __name__ == "__main__":
    app.debug=True
    app.run()