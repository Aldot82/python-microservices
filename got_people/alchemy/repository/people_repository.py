from alchemy.repository.database_connection import s
from models import People


def get_all_people():
    result = s.query(People)
    return result


def get_person(people_id):
    result = s.query(People).get(people_id)
    return result


def create_person(person_data):
    person = People(**person_data)
    r = s.add(person)
    return r
