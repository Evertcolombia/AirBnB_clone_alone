#!/usr/bin/python3

from flask import Flask, render_template
import models
from models.state import State

app = Flask(__name__)

@app.route("/states_list/", strict_slashes=False)
def state_list():
    all_objects = models.storage.all(State).values()
    print(type(all_objects))
    return render_template('7-states_list.html', states=all_objects)

@app.teardown_appcontext
def teardown(exception):
    """closes the storage on teardown"""
    models.storage.close()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
