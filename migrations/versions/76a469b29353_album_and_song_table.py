"""Album and Song Table

Revision ID: 76a469b29353
Revises: 316fa21a4347
Create Date: 2018-05-29 00:04:48.743739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76a469b29353'
down_revision = '316fa21a4347'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('album',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('albumname', sa.String(length=100), nullable=True),
    sa.Column('albumlogo', sa.String(length=400), nullable=True),
    sa.Column('albumlink', sa.String(length=500), nullable=True),
    sa.Column('artist_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_album_albumname'), 'album', ['albumname'], unique=True)
    op.create_table('song',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('songname', sa.String(length=100), nullable=True),
    sa.Column('songlink', sa.String(length=500), nullable=True),
    sa.Column('album_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['album_id'], ['album.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_song_songname'), 'song', ['songname'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_song_songname'), table_name='song')
    op.drop_table('song')
    op.drop_index(op.f('ix_album_albumname'), table_name='album')
    op.drop_table('album')
    # ### end Alembic commands ###
