"""empty message

Revision ID: 22357fc10edc
Revises: 97a2e1332ade
Create Date: 2020-04-11 16:03:15.458262

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22357fc10edc'
down_revision = '97a2e1332ade'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('internationaltesting',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('region', sa.String(), nullable=True),
    sa.Column('cumulative_testing', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_internationaltesting_date'), 'internationaltesting', ['date'], unique=False)
    op.create_index(op.f('ix_internationaltesting_region'), 'internationaltesting', ['region'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_internationaltesting_region'), table_name='internationaltesting')
    op.drop_index(op.f('ix_internationaltesting_date'), table_name='internationaltesting')
    op.drop_table('internationaltesting')
    # ### end Alembic commands ###