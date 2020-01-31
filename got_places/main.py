from flask import Flask, jsonify
from alchemy.repository.places_repository import get_all_places, find_by_id

app = Flask(__name__)


@app.route('/places')
def index():
    result = get_all_places()
    places = []
    for item in result:
        places.append({'id': item['id'], 'name': item['name']})
    return jsonify(places)


@app.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    result = find_by_id(place_id)
    place = {'id': result[0], 'name': result[1]}
    return jsonify(place)
