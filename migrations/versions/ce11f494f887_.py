"""empty message

Revision ID: ce11f494f887
Revises: c732f401f607
Create Date: 2021-11-16 21:00:42.407957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce11f494f887'
down_revision = 'c732f401f607'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('blogpost_category_key', 'blogpost', type_='unique')
    op.drop_constraint('blogpost_gender_key', 'blogpost', type_='unique')
    op.drop_constraint('blogpost_name_key', 'blogpost', type_='unique')
    op.drop_constraint('blogpost_text_key', 'blogpost', type_='unique')
    op.drop_constraint('products_brands_key', 'products', type_='unique')
    op.drop_constraint('products_category_key', 'products', type_='unique')
    op.drop_constraint('products_gender_key', 'products', type_='unique')
    op.drop_constraint('products_price_key', 'products', type_='unique')
    op.drop_constraint('products_site_key', 'products', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('products_site_key', 'products', ['site'])
    op.create_unique_constraint('products_price_key', 'products', ['price'])
    op.create_unique_constraint('products_gender_key', 'products', ['gender'])
    op.create_unique_constraint('products_category_key', 'products', ['category'])
    op.create_unique_constraint('products_brands_key', 'products', ['brands'])
    op.create_unique_constraint('blogpost_text_key', 'blogpost', ['text'])
    op.create_unique_constraint('blogpost_name_key', 'blogpost', ['name'])
    op.create_unique_constraint('blogpost_gender_key', 'blogpost', ['gender'])
    op.create_unique_constraint('blogpost_category_key', 'blogpost', ['category'])
    # ### end Alembic commands ###
