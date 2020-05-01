"""empty message

Revision ID: 7d9ad2b97832
Revises: 958c4842efef
Create Date: 2020-04-28 17:12:24.844196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d9ad2b97832'
down_revision = '958c4842efef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('source', sa.Column('region', sa.String(), nullable=True))
    op.add_column('source', sa.Column('type', sa.String(), nullable=True))
    op.create_index(op.f('ix_source_region'), 'source', ['region'], unique=False)
    op.create_index(op.f('ix_source_type'), 'source', ['type'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_source_type'), table_name='source')
    op.drop_index(op.f('ix_source_region'), table_name='source')
    op.drop_column('source', 'type')
    op.drop_column('source', 'region')
    # ### end Alembic commands ###