#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def home():
    return "Hello"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c(text=None):
    if text:
        text = text.replace('_', ' ')
        return "C {}".format(text)

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text=None):
    if text:
        return "Python {}".format(text.replace('_', ' '))
    else:
        return "Python is cool"

@app.route("/number/<int:num>", strict_slashes=False)
def number(num):
    return "{} is a number".format(num)

@app.route("/number_template/<int:num>", strict_slashes=False)
def number_template(num):
    return render_template('5-number.html', n=num)

@app.route("/number_odd_or_even/<int:num>", strict_slashes=False)
def number_odd_or_even(num):
    if num % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
    return render_template('6-number_odd_or_even.html', n= num, var=even_odd)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
