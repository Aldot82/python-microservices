"""create people table

Revision ID: cdd10b3f96e3
Revises: 
Create Date: 2019-07-27 13:34:59.623219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cdd10b3f96e3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'people',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=False),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('isAlive', sa.Boolean, nullable=False),
        sa.Column('placeId', sa.Integer, nullable=True),
    )


def downgrade():
    op.drop_table('people')
