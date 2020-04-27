"""empty message

Revision ID: 158e11ad7d91
Revises: 8805fcecd40b
Create Date: 2020-04-25 19:02:37.100443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '158e11ad7d91'
down_revision = '8805fcecd40b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('viz', sa.Column('phu', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('viz', 'phu')
    # ### end Alembic commands ###