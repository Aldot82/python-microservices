from sqlalchemy import Table, Column, String, Integer, MetaData

metadata = MetaData()

table_places = Table(
    'places', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(25), nullable=False),
)
