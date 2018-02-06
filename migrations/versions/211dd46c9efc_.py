"""empty message

Revision ID: 211dd46c9efc
Revises: 
Create Date: 2018-02-05 23:08:14.904428

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '211dd46c9efc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Users')
    # ### end Alembic commands ###
