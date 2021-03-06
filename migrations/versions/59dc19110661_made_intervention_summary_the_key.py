"""made intervention summary the key

Revision ID: 59dc19110661
Revises: 81998c8b1aee
Create Date: 2020-04-05 12:31:07.309737

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59dc19110661'
down_revision = '81998c8b1aee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_npiinterventions_end_date'), 'npiinterventions', ['end_date'], unique=False)
    op.create_index(op.f('ix_npiinterventions_intervention_summary'), 'npiinterventions', ['intervention_summary'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_npiinterventions_intervention_summary'), table_name='npiinterventions')
    op.drop_index(op.f('ix_npiinterventions_end_date'), table_name='npiinterventions')
    # ### end Alembic commands ###
