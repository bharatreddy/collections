from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
@app.route("/")
def starter():
    return render_template('ttt-index.html')

if __name__ == "__main__":
    app.debug=True
    app.run()