from alchemy.repository.database_connection import conn
from sqlalchemy.sql import text
import logging


def get_all_people():
    result = conn.execute('select * from people')
    return result


def get_person(people_id):
    result = conn.execute(f'select * from people where id={people_id}')
    person = result.fetchone()
    return person


def create_person(person_data):
    data = {"name": person_data["name"], "isAlive": person_data["isAlive"], "placeId": person_data["placeId"], "id": person_data["id"]}
    logging.error(msg=data)
    statement = text("""insert into people("id", "name", "placeId", "isAlive") values(:id, :name, :placeId, :isAlive)""")
    person = conn.execute(statement, **data)
    return person