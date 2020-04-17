"""test to see if this works

Revision ID: 38b498e051db
Revises: 6c3fdcfb94c8
Create Date: 2020-04-17 15:44:30.855958

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38b498e051db'
down_revision = '6c3fdcfb94c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('governmentresponse',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('country_code', sa.String(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('s1_school_closing', sa.Integer(), nullable=True),
    sa.Column('s1_is_general', sa.Integer(), nullable=True),
    sa.Column('s1_notes', sa.String(), nullable=True),
    sa.Column('s2_workplace_closing', sa.Integer(), nullable=True),
    sa.Column('s2_is_general', sa.Integer(), nullable=True),
    sa.Column('s2_notes', sa.String(), nullable=True),
    sa.Column('s3_cancel_public_events', sa.Integer(), nullable=True),
    sa.Column('s3_is_general', sa.Integer(), nullable=True),
    sa.Column('s3_notes', sa.String(), nullable=True),
    sa.Column('s4_close_public_transport', sa.Integer(), nullable=True),
    sa.Column('s4_is_general', sa.Integer(), nullable=True),
    sa.Column('s4_notes', sa.String(), nullable=True),
    sa.Column('s5_public_information_campaigns', sa.Integer(), nullable=True),
    sa.Column('s5_is_general', sa.Integer(), nullable=True),
    sa.Column('s5_notes', sa.String(), nullable=True),
    sa.Column('s6_restrictions_on_internal_movement', sa.Integer(), nullable=True),
    sa.Column('s6_is_general', sa.Integer(), nullable=True),
    sa.Column('s6_notes', sa.String(), nullable=True),
    sa.Column('s7_international_travel_controls', sa.Integer(), nullable=True),
    sa.Column('s7_notes', sa.String(), nullable=True),
    sa.Column('s8_fiscal_measures', sa.BigInteger(), nullable=True),
    sa.Column('s8_notes', sa.String(), nullable=True),
    sa.Column('s9_monetary_measures', sa.Float(), nullable=True),
    sa.Column('s9_notes', sa.String(), nullable=True),
    sa.Column('s10_emergency_investment_in_healthcare', sa.BigInteger(), nullable=True),
    sa.Column('s10_notes', sa.String(), nullable=True),
    sa.Column('s11_investement_in_vaccines', sa.BigInteger(), nullable=True),
    sa.Column('s11_notes', sa.String(), nullable=True),
    sa.Column('s12_testing_framework', sa.Integer(), nullable=True),
    sa.Column('s12_notes', sa.String(), nullable=True),
    sa.Column('s13_contact_tracing', sa.Integer(), nullable=True),
    sa.Column('s13_notes', sa.String(), nullable=True),
    sa.Column('confirmed_cases', sa.Integer(), nullable=True),
    sa.Column('confirmed_deaths', sa.Integer(), nullable=True),
    sa.Column('stringency_index', sa.Float(), nullable=True),
    sa.Column('stringency_index_for_display', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_governmentresponse_country'), 'governmentresponse', ['country'], unique=False)
    op.create_index(op.f('ix_governmentresponse_date'), 'governmentresponse', ['date'], unique=False)
    op.create_table('npiinterventions_usa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('county', sa.String(), nullable=True),
    sa.Column('npi', sa.String(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('citation', sa.String(), nullable=True),
    sa.Column('note', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_npiinterventions_usa_npi'), 'npiinterventions_usa', ['npi'], unique=False)
    op.create_index(op.f('ix_npiinterventions_usa_state'), 'npiinterventions_usa', ['state'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_npiinterventions_usa_state'), table_name='npiinterventions_usa')
    op.drop_index(op.f('ix_npiinterventions_usa_npi'), table_name='npiinterventions_usa')
    op.drop_table('npiinterventions_usa')
    op.drop_index(op.f('ix_governmentresponse_date'), table_name='governmentresponse')
    op.drop_index(op.f('ix_governmentresponse_country'), table_name='governmentresponse')
    op.drop_table('governmentresponse')
    # ### end Alembic commands ###
