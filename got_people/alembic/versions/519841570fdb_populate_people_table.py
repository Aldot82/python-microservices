"""populate people table

Revision ID: 519841570fdb
Revises: cdd10b3f96e3
Create Date: 2019-07-27 13:44:43.750996

"""
from alembic import op
import sqlalchemy as sa

from alchemy.metadata import table_people

# revision identifiers, used by Alembic.
revision = '519841570fdb'
down_revision = 'cdd10b3f96e3'
branch_labels = None
depends_on = None


def upgrade():
    op.bulk_insert(
        table_people, [
            {'id': 1, 'name': 'Sensei Lamister', 'isAlive': True, 'placeId': 1},
            {'id': 2, 'name': 'Aiba Stack', 'isAlive': True, 'placeId': 3},
            {'id': 3, 'name': 'Joaquín Nevado', 'isAlive': True, 'placeId': 1},
            {'id': 4, 'name': 'Dedo Gordo', 'isAlive': False, 'placeId': None},
            {'id': 5, 'name': 'Juanito Lamister', 'isAlive': True, 'placeId': 1},
            {'id': 6, 'name': 'Nerf Stack', 'isAlive': True, 'placeId': 3}
        ]
    )


def downgrade():
    pass
