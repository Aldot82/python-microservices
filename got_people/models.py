from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class People(Base):

    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    isAlive = Column(Boolean)
    placeId = Column(Integer)

    def __init__(self, name, isAlive, placeId):
        self.name = name
        self.isAlive = isAlive
        self.placeId = placeId

    def serialize(self):
        return {"id": self.id, "name": self.name, "isAlive": self.isAlive, "placeId": self.placeId}