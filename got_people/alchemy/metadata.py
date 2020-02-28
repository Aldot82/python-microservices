from sqlalchemy import Table, Column, String, Integer, MetaData, Boolean

metadata = MetaData()

table_people = Table(
    'people', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(25), nullable=False),
    Column('isAlive', Boolean, nullable=False),
    Column('placeId', Integer, nullable=True),
)
