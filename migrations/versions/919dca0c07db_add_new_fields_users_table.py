"""add new fields users table

Revision ID: 919dca0c07db
Revises: 9bcaba563535
Create Date: 2022-02-07 16:55:03.984270

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '919dca0c07db'
down_revision = '9bcaba563535'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
