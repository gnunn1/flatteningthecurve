"""added comparison changed name

Revision ID: e46ca5f12457
Revises: 16d59356fa54
Create Date: 2020-03-23 15:07:25.697055

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e46ca5f12457'
down_revision = '16d59356fa54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comparison',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('province', sa.String(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.Column('hundred', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comparison_date'), 'comparison', ['date'], unique=False)
    op.create_index(op.f('ix_comparison_province'), 'comparison', ['province'], unique=False)
    op.drop_index('ix_Comparison_date', table_name='Comparison')
    op.drop_index('ix_Comparison_province', table_name='Comparison')
    op.drop_table('Comparison')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Comparison',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Comparison_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('province', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('count', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('hundred', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Comparison_pkey')
    )
    op.create_index('ix_Comparison_province', 'Comparison', ['province'], unique=False)
    op.create_index('ix_Comparison_date', 'Comparison', ['date'], unique=False)
    op.drop_index(op.f('ix_comparison_province'), table_name='comparison')
    op.drop_index(op.f('ix_comparison_date'), table_name='comparison')
    op.drop_table('comparison')
    # ### end Alembic commands ###
