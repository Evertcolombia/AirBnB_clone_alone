#!/usr/bin/python3
from flask import Flask, render_template
import models
from models.state import State

app = Flask(__name__)


@app.route("/states/", strict_slashes=False)
@app.route("/states/<state_id>", strict_slashes=False)
def states(state_id=None):
    """ get states and siplay for id or all states"""
    all_states = models.storage.all("State")
    if state_id is not None:
        state_id = "State." + state_id
    return render_template('9-states.html',
            states=all_states, state_id=state_id)

@app.teardown_appcontext
def teardown(exception):
    """closes the storage on teardown"""
    models.storage.close()


if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
