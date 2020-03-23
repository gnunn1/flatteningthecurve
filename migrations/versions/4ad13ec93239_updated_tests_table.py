"""updated tests table

Revision ID: 4ad13ec93239
Revises: 95ae449be7ba
Create Date: 2020-03-23 12:56:59.844493

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4ad13ec93239'
down_revision = '95ae449be7ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('covidtests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('negative', sa.Integer(), nullable=True),
    sa.Column('investigation', sa.Integer(), nullable=True),
    sa.Column('positive', sa.Integer(), nullable=True),
    sa.Column('resolved', sa.Integer(), nullable=True),
    sa.Column('deaths', sa.Integer(), nullable=True),
    sa.Column('total', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_covidtests_date'), 'covidtests', ['date'], unique=False)
    op.drop_index('ix_covids_date', table_name='covids')
    op.drop_index('ix_covids_province', table_name='covids')
    op.drop_table('covids')
    op.drop_index('ix_covidDate_date', table_name='covidDate')
    op.drop_index('ix_covidDate_province', table_name='covidDate')
    op.drop_table('covidDate')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('covidDate',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"covidDate_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('province', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='covidDate_pkey')
    )
    op.create_index('ix_covidDate_province', 'covidDate', ['province'], unique=False)
    op.create_index('ix_covidDate_date', 'covidDate', ['date'], unique=False)
    op.create_table('covids',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('province', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('count', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('hundred', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='covids_pkey')
    )
    op.create_index('ix_covids_province', 'covids', ['province'], unique=False)
    op.create_index('ix_covids_date', 'covids', ['date'], unique=False)
    op.drop_index(op.f('ix_covidtests_date'), table_name='covidtests')
    op.drop_table('covidtests')
    # ### end Alembic commands ###