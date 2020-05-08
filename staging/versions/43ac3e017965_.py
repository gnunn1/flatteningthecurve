"""empty message

Revision ID: 43ac3e017965
Revises: 768b2722ac78
Create Date: 2020-05-06 13:43:40.030803

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43ac3e017965'
down_revision = '768b2722ac78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mobilitytransportation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('source', sa.String(), nullable=True),
    sa.Column('region', sa.String(), nullable=True),
    sa.Column('transportation_type', sa.String(), nullable=True),
    sa.Column('value', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_mobilitytransportation_date'), 'mobilitytransportation', ['date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_mobilitytransportation_date'), table_name='mobilitytransportation')
    op.drop_table('mobilitytransportation')
    # ### end Alembic commands ###