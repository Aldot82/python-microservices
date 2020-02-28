import requests


def get_people():
    response = requests.get('http://got_people_app_1:5001/people')
    return response.json()