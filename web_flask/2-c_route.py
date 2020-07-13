#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def home():
    return "Hello"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c(text=None):
    if (text):
        text = text.replace('_', ' ')
        return "C {}".format(text)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
