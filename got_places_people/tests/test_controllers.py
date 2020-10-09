import json
from unittest.mock import patch


@patch('main.get_places')
@patch('main.get_people')
def test_find_all(mock_people, mock_places, client):
    person = {'id': 1, 'name': 'first', 'isAlive': True, 'placeId': 1}
    person_2 = {'id': 2, 'name': 'second', 'isAlive': True, 'placeId': 2}
    person_3 = {'id': 3, 'name': 'third', 'isAlive': True, 'placeId': 1}

    people = [person, person_2, person_3]

    city = {'id': 1, 'name': 'first'}
    city2 = {'id': 2, 'name': 'second'}

    cities = [city, city2]

    mock_people.return_value = people
    mock_places.return_value = cities

    expected = [
        {
            "id": 1,
            "name": "first",
            "people": [
                {
                    "id": 1,
                    "isAlive": True,
                    "name": "first",
                    "placeId": 1
                },
                {
                    "id": 3,
                    "isAlive": True,
                    "name": "third",
                    "placeId": 1
                },
            ]
        },
        {
            "id": 2,
            "name": "second",
            "people": [
                {'id': 2, 'name': 'second', 'isAlive': True, 'placeId': 2}
            ]
        },
    ]

    res = client.get('/got-places')
    assert res.status_code == 200
    assert expected == json.loads(res.get_data())

