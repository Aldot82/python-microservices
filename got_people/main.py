from flask import Flask
from alchemy.repository.people_repository import get_all_people, get_person, create_person
from flask import jsonify
from flask import request
import logging

app = Flask(__name__)


@app.route('/people', methods=['GET',])
def get_people():
    people = get_all_people()
    people_list = [person.serialize() for person in people]
    return jsonify(people_list)


@app.route('/people/<people_id>/', methods=['GET',])
def get_one(people_id):
    person = get_person(people_id)
    return jsonify(person.serialize())


@app.route('/people', methods=['POST',])
def post_people():
    person = request.get_json()
    res = create_person(person)
    return jsonify(201, res)
