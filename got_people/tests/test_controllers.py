import json
from unittest.mock import patch
from models import People


@patch('main.find_all')
def test_find_all(mock, client):
    p1 = {'name': 'first', 'isAlive': True, 'placeId': 1}
    p2 = {'name': 'second', 'isAlive': False, 'placeId': 2}
    created1 = People(**p1)
    created2 = People(**p2)
    mock.return_value = [created1, created2]
    res = client.get('/people')
    assert res.status_code == 200
    assert 2 == len(json.loads(res.get_data()))


@patch('main.create_person')
def test_post_people(mock, client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {'name': 'Black Wolf', 'isAlive': True, 'placeId': 3}
    mock.return_value=data
    res = client.post('/people', data=json.dumps(data), headers=headers)
    assert res.status_code == 201


@patch('main.find_by_id')
def test_by_id(mock, client):
    person = {'name': 'name', 'isAlive': True, 'placeId': 1}
    created = People(**person)
    mock.return_value = created
    res = client.get('/people/1/')
    assert res.status_code == 200



