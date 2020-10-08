from flask import Flask
from alchemy.repository.people_repository import find_all, find_by_id, create_person
from flask import jsonify
from flask import request
from sqlalchemy import exc


app = Flask(__name__)


@app.route('/people', methods=['GET',])
def get_people():
    people = find_all()
    people_list = [person.serialize() for person in people]
    return jsonify(people_list), 200


@app.route('/people/<people_id>/', methods=['GET',])
def get_one(people_id):
    person = find_by_id(people_id)
    if person:
        return jsonify(person.serialize())
    return jsonify("Not Found"), 404


@app.route('/people', methods=['POST',])
def post_people():
    person = request.get_json()
    try:
        create_person(person)
        return jsonify("Ok"), 201
    except exc.SQLAlchemyError:
        return jsonify("Error al registrar"), 400
