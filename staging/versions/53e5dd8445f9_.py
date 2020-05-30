"""empty message

Revision ID: 53e5dd8445f9
Revises: 0d0d42ac0c04
Create Date: 2020-05-19 18:56:45.511549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53e5dd8445f9'
down_revision = '0d0d42ac0c04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('viz', sa.Column('text_bottom', sa.String(), nullable=True))
    op.add_column('viz', sa.Column('text_top', sa.String(), nullable=True))
    op.drop_column('viz', 'text')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('viz', sa.Column('text', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('viz', 'text_top')
    op.drop_column('viz', 'text_bottom')
    # ### end Alembic commands ###