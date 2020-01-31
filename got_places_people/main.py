from flask import Flask, jsonify
import requests
import json
import logging
app = Flask(__name__)


@app.route('/places')
def index():
    total_dict = {}
    total_list = []
    places = get_places()
    people = get_people()
    
    for place in places:
        total_list.append(place)

    for place in total_list:  
        place['people'] = [person for person in people if person.get('placeId') == place.get('id')]
    
    return jsonify(total_list)


def get_places():
    response = requests.get('http://got_places_app_1:5000/places')
    return response.json()


def get_people():
    response = requests.get('http://got_people_app_1:5001/people')
    return response.json()
