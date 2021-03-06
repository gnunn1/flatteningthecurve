"""changed column name

Revision ID: 9c48cb93c506
Revises: dc927bcd64fa
Create Date: 2020-04-05 14:11:12.775705

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c48cb93c506'
down_revision = 'dc927bcd64fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('internationalrecovered', sa.Column('recovered', sa.Integer(), nullable=True))
    op.drop_column('internationalrecovered', 'deaths')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('internationalrecovered', sa.Column('deaths', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('internationalrecovered', 'recovered')
    # ### end Alembic commands ###
