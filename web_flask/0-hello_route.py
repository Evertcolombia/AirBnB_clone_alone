#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def home():
    return "hello HNBN"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
