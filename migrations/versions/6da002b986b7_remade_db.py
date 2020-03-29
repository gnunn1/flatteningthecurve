"""remade db

Revision ID: 6da002b986b7
Revises: 5cb0647e1289
Create Date: 2020-03-27 21:12:18.997343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6da002b986b7'
down_revision = '5cb0647e1289'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('internationaldata',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('cases', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_internationaldata_country'), 'internationaldata', ['country'], unique=False)
    op.create_index(op.f('ix_internationaldata_date'), 'internationaldata', ['date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_internationaldata_date'), table_name='internationaldata')
    op.drop_index(op.f('ix_internationaldata_country'), table_name='internationaldata')
    op.drop_table('internationaldata')
    # ### end Alembic commands ###