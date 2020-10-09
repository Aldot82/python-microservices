import json
from unittest.mock import patch
from models import Place


@patch('main.find_all')
def test_find_all(mock, client):
    p1 = {'name': 'first'}
    p2 = {'name': 'second'}
    created1 = Place(**p1)
    created2 = Place(**p2)
    mock.return_value = [created1, created2]
    res = client.get('/places')
    assert res.status_code == 200
    assert 2 == len(json.loads(res.get_data()))


@patch('main.create_place')
def test_post_people(mock, client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {'name': 'my place'}
    mock.return_value=data
    res = client.post('/places', data=json.dumps(data), headers=headers)
    assert res.status_code == 201


@patch('main.find_by_id')
def test_by_id(mock, client):
    place = {'name': 'name'}
    created = Place(**place)
    mock.return_value = created
    res = client.get('/places/1/')
    assert res.status_code == 200



