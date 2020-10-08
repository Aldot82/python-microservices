from alchemy.repository.database_conection import create_connection
from sqlalchemy import exc

from models import Place


s = create_connection()


def find_all():
    result = s.query(Place)
    return result


def find_by_id(place_id):
    result = s.query(Place).get(place_id)
    return result


def create_place(person_data):
    place = Place(**person_data)
    try:
        s.add(place)
        s.commit()
    except exc.SQLAlchemyError:
        s.rollback()
        raise
