#!/usr/bin/python3

from api.v1.views import app_views
import models
from flask import jsonify


tables = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}

@app_views.route('/status', methods=["GET"], strict_slashes=False)
def status():
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=["GET"], strict_slashes=False)
def stats_count():
    elements = {}
    for k, v in tables.items():
        elements[k] = models.storage.count(v)
    return jsonify(elements)

if __name__ == "__main__":
    pass

