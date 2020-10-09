from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

db = os.getenv('DATABASE_URL')


def create_connection():
    engine = create_engine(db)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
