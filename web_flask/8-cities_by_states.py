#!/usr/bin/python3
from flask import Flask, render_template
import models
from models.city import City
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states/", strict_slashes=False)
def cities_by_states():
    """ get all cities for each state"""
    if models.type_storage == "db":
        all_states = models.storage.all(State).values()
        return render_template('8-cities_by_states.html', states=all_states)

@app.teardown_appcontext
def teardown(exception):
    """closes the storage on teardown"""
    models.storage.close()


if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
