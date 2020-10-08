from flask import Flask, jsonify
from alchemy.repository.places_repository import find_all, find_by_id, create_place
from sqlalchemy import exc
from flask import request


app = Flask(__name__)


@app.route('/places', methods=['GET',])
def get_all():
    places = find_all()
    places_list = [place.serialize() for place in places]
    return jsonify(places_list), 200


@app.route('/places/<place_id>/', methods=['GET',])
def get_one(place_id):
    place= find_by_id(place_id)
    if place:
        return jsonify(place.serialize()), 200
    return jsonify("Not Found"), 404


@app.route('/places', methods=['POST',])
def post_people():
    place = request.get_json()
    try:
        create_place(place)
        return jsonify("Ok"), 201
    except exc.SQLAlchemyError:
        return jsonify("Error al registrar"), 400
