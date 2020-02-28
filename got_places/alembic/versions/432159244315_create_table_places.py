"""create table places

Revision ID: 432159244315
Revises: 
Create Date: 2019-07-16 19:59:02.670322

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '432159244315'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'places',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
    )


def downgrade():
    op.drop_table('places')
