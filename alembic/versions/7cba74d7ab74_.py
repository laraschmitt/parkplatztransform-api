"""

Revision ID: 7cba74d7ab74
Revises: 469715732508
Create Date: 2020-11-25 20:22:57.433784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7cba74d7ab74'
down_revision = '469715732508'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_segments_geometry', table_name='segments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('idx_segments_geometry', 'segments', ['geometry'], unique=False)
    # ### end Alembic commands ###
