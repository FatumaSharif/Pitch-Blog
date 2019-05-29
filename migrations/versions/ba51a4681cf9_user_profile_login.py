"""User Profile|Login

Revision ID: ba51a4681cf9
Revises: ee6bced5ea09
Create Date: 2019-05-29 14:16:12.174710

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba51a4681cf9'
down_revision = 'ee6bced5ea09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitch', 'upvote')
    op.drop_column('pitch', 'downvote')
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('email', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'password_hash')
    op.drop_column('users', 'email')
    op.drop_column('users', 'bio')
    op.add_column('pitch', sa.Column('downvote', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('pitch', sa.Column('upvote', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
