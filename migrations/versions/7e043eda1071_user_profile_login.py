"""User Profile|Login

Revision ID: 7e043eda1071
Revises: 52441e922b42
Create Date: 2019-05-29 17:21:54.971839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e043eda1071'
down_revision = '52441e922b42'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitch', sa.Column('category', sa.String(length=255), nullable=True))
    op.add_column('pitch', sa.Column('name', sa.String(length=255), nullable=True))
    op.add_column('pitch', sa.Column('pitch', sa.String(length=255), nullable=True))
    op.drop_column('pitch', 'pitchidea')
    op.drop_column('pitch', 'title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitch', sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('pitch', sa.Column('pitchidea', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('pitch', 'pitch')
    op.drop_column('pitch', 'name')
    op.drop_column('pitch', 'category')
    # ### end Alembic commands ###