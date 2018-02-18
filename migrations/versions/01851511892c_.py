"""empty message

Revision ID: 01851511892c
Revises: 211dd46c9efc
Create Date: 2018-02-11 19:02:21.367133

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01851511892c'
down_revision = '211dd46c9efc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Lyrics', sa.Column('lyrics', sa.Text(), nullable=True))
    op.add_column('Lyrics', sa.Column('spotify_track_id', sa.String(length=255), nullable=True))
    op.add_column('Lyrics', sa.Column('timestamps', sa.Text(), nullable=True))
    op.drop_index('songtitle', table_name='Lyrics')
    op.create_unique_constraint(None, 'Lyrics', ['spotify_track_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Lyrics', type_='unique')
    op.create_index('songtitle', 'Lyrics', ['songtitle'], unique=True)
    op.drop_column('Lyrics', 'timestamps')
    op.drop_column('Lyrics', 'spotify_track_id')
    op.drop_column('Lyrics', 'lyrics')
    # ### end Alembic commands ###