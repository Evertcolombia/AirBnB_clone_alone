from api.v1.views import app_views
import models
from models.state import State
from flask import abort, jsonify, request, make_response

@app_views.route('/states', methods=["GET"], strict_slashes=False)
def states_list():
    states = []
    all_states = models.storage.all("State")
    for st in all_states.values():
        states.append(st.to_dict())
    return jsonify(states)

@app_views.route('/states/<string:state_id>', methods=["GET"], strict_slashes=False)
def state_by_id(state_id):
    state = models.storage.get("State", state_id)

    if state is None:
        abort(404)
    return jsonify(state.to_dict())

@app_views.route('states/<string:state_id>', methods=["DELETE"], strict_slashes=False)
def delete_state(state_id):
    state = models.storage.get("State", state_id)
    if state is None:
        abort(404)
    state.delete()
    models.storage.save()
    return jsonify({})

@app_views.route('/states', methods=["POST"], strict_slashes=False)
def create_state():
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if not request.get_json():
        return make_response(jsonify({'error': 'Missing Name'}), 400)
    state = State(**request.get_json())
    state.save()
    state = jsonify(state.to_dict())
    return make_response(state, 201)

@app_views.route('/states/<string:state_id>', methods=["PUT"], strict_slashes=False)
def update_sate(state_id):
    selected_state = models.storage.get("State", state_id)
    if selected_state is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a Json'}), 400)

    for key in request.get_json():
        if key != 'id' and key != 'created_at' and key != 'updated_at': 
            setattr(selected_state, key, request.json[key])
    selected_state.save()
    return jsonify(selected_state.to_dict())
    
if __name__ == "__main__":
    pass