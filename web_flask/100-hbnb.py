#!/usr/bin/python3
from flask import Flask, render_template
import models
from models.state import State

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def states(state_id=None):
    """ get states and siplay for id or all states"""
    all_states = models.storage.all("State").values()
    amenities = models.storage.all("Amenity").values()
    places = models.storage.all("Place").values()
    return render_template('100-hbnb.html',
            states=all_states, amenities=amenities, places=places)

@app.teardown_appcontext
def teardown(exception):
    """closes the storage on teardown"""
    models.storage.close()


if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
