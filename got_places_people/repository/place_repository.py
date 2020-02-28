import requests


def get_places():
    response = requests.get('http://got_places_app_1:5000/places')
    return response.json()
