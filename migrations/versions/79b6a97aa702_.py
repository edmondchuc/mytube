"""empty message

Revision ID: 79b6a97aa702
Revises: 
Create Date: 2020-04-12 00:18:21.954843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79b6a97aa702'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=64), nullable=False),
    sa.Column('given_name', sa.String(length=64), nullable=False),
    sa.Column('family_name', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=320), nullable=False),
    sa.Column('picture_url', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_user_user_id'), 'user', ['user_id'], unique=True)
    op.create_table('video',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=False),
    sa.Column('filename', sa.String(length=64), nullable=False),
    sa.Column('original_filename', sa.String(length=64), nullable=False),
    sa.Column('upload_datetime', sa.DateTime(), nullable=False),
    sa.Column('content_type', sa.String(length=32), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('video_comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.String(length=128), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('video_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['video_id'], ['video.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('video_comment')
    op.drop_table('video')
    op.drop_index(op.f('ix_user_user_id'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
