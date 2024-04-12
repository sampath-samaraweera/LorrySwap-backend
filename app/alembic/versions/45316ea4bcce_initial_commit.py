"""initial commit

Revision ID: 45316ea4bcce
Revises: 
Create Date: 2024-04-10 16:38:10.169946

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '45316ea4bcce'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fname', sa.String(length=50), nullable=False),
    sa.Column('lname', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('phone', sa.String(length=12), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('gender', sa.String(length=1), nullable=False),
    sa.Column('photo', sa.String(length=255), server_default='../assests/images/default.jpg', nullable=False),
    sa.Column('nic', sa.String(length=15), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password_hash', sa.String(length=256), nullable=False),
    sa.Column('verified', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('nic'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('username')
    )
    op.create_table('driver',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('residence', sa.String(length=50), nullable=False),
    sa.Column('licence_side1', sa.String(length=500), nullable=True),
    sa.Column('licence_side2', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('licence_side1'),
    sa.UniqueConstraint('licence_side2')
    )
    op.create_table('ride',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('location', sa.String(length=20), nullable=False),
    sa.Column('destination', sa.String(length=20), nullable=False),
    sa.Column('location_lat', sa.String(length=50), nullable=False),
    sa.Column('location_lon', sa.String(length=50), nullable=False),
    sa.Column('destination_lat', sa.String(length=50), nullable=False),
    sa.Column('destination_lon', sa.String(length=150), nullable=False),
    sa.Column('date', sa.DATE(), nullable=False),
    sa.Column('time', sa.String(length=150), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('suggestedRide',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('contact_recipient', sa.String(length=15), nullable=False),
    sa.Column('date', sa.DATE(), nullable=False),
    sa.Column('package_type', sa.String(length=50), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('height', sa.Float(), nullable=False),
    sa.Column('length', sa.Float(), nullable=False),
    sa.Column('width', sa.Float(), nullable=False),
    sa.Column('truck_type', sa.String(length=50), nullable=False),
    sa.Column('location', sa.String(length=20), server_default='Colombo', nullable=False),
    sa.Column('destination', sa.String(length=20), server_default='Ratnapura', nullable=False),
    sa.Column('plat', sa.String(length=50), nullable=False),
    sa.Column('plon', sa.String(length=50), nullable=False),
    sa.Column('dlat', sa.String(length=50), nullable=False),
    sa.Column('dlon', sa.String(length=50), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('user_type', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_type')
    op.drop_table('suggestedRide')
    op.drop_table('ride')
    op.drop_table('driver')
    op.drop_table('user')
    # ### end Alembic commands ###
