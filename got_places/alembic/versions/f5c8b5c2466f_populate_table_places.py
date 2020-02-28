"""populate table places

Revision ID: f5c8b5c2466f
Revises: 432159244315
Create Date: 2019-07-17 08:15:59.579208

"""
from alembic import op
import sqlalchemy as sa
from alchemy.metadata import table_places

# revision identifiers, used by Alembic.
revision = 'f5c8b5c2466f'
down_revision = '432159244315'
branch_labels = None
depends_on = None


def upgrade():
    op.bulk_insert(
        table_places, [
            {'name': 'Descaro del rey'},
            {'name': 'Más allá del zumo'},
            {'name': 'Veranolandia'}
        ]
    )


def downgrade():
    pass
