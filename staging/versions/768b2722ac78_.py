"""empty message

Revision ID: 768b2722ac78
Revises: fa524abadfce
Create Date: 2020-05-06 13:37:02.665337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '768b2722ac78'
down_revision = 'fa524abadfce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mobilitytransportation', sa.Column('source', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('mobilitytransportation', 'source')
    # ### end Alembic commands ###
