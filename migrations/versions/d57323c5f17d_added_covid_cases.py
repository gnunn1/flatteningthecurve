"""added covid cases

Revision ID: d57323c5f17d
Revises: 3555975028ae
Create Date: 2020-03-23 14:14:44.674742

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd57323c5f17d'
down_revision = '3555975028ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('covid', sa.Column('age', sa.String(length=120), nullable=True))
    op.add_column('covid', sa.Column('case_id', sa.Integer(), nullable=True))
    op.add_column('covid', sa.Column('country', sa.String(length=120), nullable=True))
    op.add_column('covid', sa.Column('locala', sa.String(length=120), nullable=True))
    op.add_column('covid', sa.Column('province', sa.String(length=120), nullable=True))
    op.add_column('covid', sa.Column('region', sa.String(length=120), nullable=True))
    op.add_column('covid', sa.Column('sex', sa.String(length=120), nullable=True))
    op.add_column('covid', sa.Column('travel', sa.Integer(), nullable=True))
    op.add_column('covid', sa.Column('travelh', sa.String(length=120), nullable=True))
    op.create_index(op.f('ix_covid_case_id'), 'covid', ['case_id'], unique=False)
    op.drop_column('covid', 'negative')
    op.drop_column('covid', 'investigation')
    op.drop_column('covid', 'deaths')
    op.drop_column('covid', 'resolved')
    op.drop_column('covid', 'positive')
    op.drop_column('covid', 'total')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('covid', sa.Column('total', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('covid', sa.Column('positive', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('covid', sa.Column('resolved', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('covid', sa.Column('deaths', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('covid', sa.Column('investigation', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('covid', sa.Column('negative', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_covid_case_id'), table_name='covid')
    op.drop_column('covid', 'travelh')
    op.drop_column('covid', 'travel')
    op.drop_column('covid', 'sex')
    op.drop_column('covid', 'region')
    op.drop_column('covid', 'province')
    op.drop_column('covid', 'locala')
    op.drop_column('covid', 'country')
    op.drop_column('covid', 'case_id')
    op.drop_column('covid', 'age')
    # ### end Alembic commands ###
