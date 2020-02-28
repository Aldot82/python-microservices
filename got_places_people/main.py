from flask import Flask, jsonify
from repository.place_repository import get_places
from repository.people_repository import get_people


app = Flask(__name__)


@app.route('/got-places')
def index():
    places = get_places()
    people = get_people()

    for place in places:
        place['people'] = [person for person in people if person.get('placeId') == place.get('id')]

    return jsonify(places)
