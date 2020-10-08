from alchemy.repository.database_connection import create_connection
from sqlalchemy import exc

from models import People

s = create_connection()


def find_all():
    result = s.query(People)
    return result


def find_by_id(people_id):
    result = s.query(People).get(people_id)
    return result


def create_person(person_data):
    person = People(**person_data)
    try:
        s.add(person)
        s.commit()
    except exc.SQLAlchemyError:
        s.rollback()
        raise
