from flask import Flask
from alchemy.repository.people_repository import get_all_people, get_person, create_person
from flask import jsonify
from flask import request
import logging

app = Flask(__name__)

@app.route('/people', methods = ['GET',])
def get_people():
    people = get_all_people()
    total_people = []
    for person in people:
        total_people.append({'id': person['id'], 'name': person['name'], 
                             'isAlive': person['isAlive'], 'placeId': person['placeId']})
    return jsonify(total_people)


@app.route('/people/<people_id>/', methods = ['GET',])
def get_one(people_id):
    person = get_person(people_id)
    person_object = {'id': person[0], 'name': person[1], 'isAlive': person[2], 'placeId': person[3]}
    return jsonify(person_object)


@app.route('/people', methods = ['POST',])
def post_people():
    person = request.get_json()
    logging.error(msg=person)
    create_person(person)
    return jsonify(201, 'OK')
