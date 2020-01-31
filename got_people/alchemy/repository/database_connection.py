from sqlalchemy import create_engine


def create_connection():
    engine = create_engine(
        'postgresql+psycopg2://postgres:aldot2406@db:5432/people')
    connection = engine.connect()
    return connection

conn = create_connection()
