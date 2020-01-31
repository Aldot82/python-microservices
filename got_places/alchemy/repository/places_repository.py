from alchemy.repository.database_conection import conn


def get_all_places():
    result = conn.execute('select * from places')
    return result


def find_by_id(place_id):
    res = conn.execute(f'select * from places where id={place_id}')
    place = res.fetchone()
    return place
