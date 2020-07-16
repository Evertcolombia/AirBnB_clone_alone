#!/usr/bin/python3
from flask import Flask, Blueprint
import models
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    models.storage.close()

if __name__ == "__main__":
    app.run(
        debug=True,
        host=os.environ.get("HBNB_API_HOST", "0.0.0.0"),
        port=os.environ.get("HBNB_API_PORT", "5000"),
        threaded=True)
