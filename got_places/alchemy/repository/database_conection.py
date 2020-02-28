from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_connection():
    engine = create_engine(
        'postgresql+psycopg2://postgres:Aldot_2406@db:5432/lugares')
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
