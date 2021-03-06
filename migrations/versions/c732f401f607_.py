"""empty message

Revision ID: c732f401f607
Revises: f396a9263093
Create Date: 2021-11-16 20:52:43.815736

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c732f401f607'
down_revision = 'f396a9263093'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogpost', sa.Column('products', postgresql.ARRAY(sa.Integer()), nullable=True))
    op.add_column('products', sa.Column('blogpost_id', sa.Integer(), nullable=False))
    op.drop_constraint('products_blogposts_id_fkey', 'products', type_='foreignkey')
    op.create_foreign_key(None, 'products', 'blogpost', ['blogpost_id'], ['id'])
    op.drop_column('products', 'blogposts_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('blogposts_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.create_foreign_key('products_blogposts_id_fkey', 'products', 'blogpost', ['blogposts_id'], ['id'])
    op.drop_column('products', 'blogpost_id')
    op.drop_column('blogpost', 'products')
    # ### end Alembic commands ###
