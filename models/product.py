from utils.enums import GenderEnum, CategoryEnum
from sqlalchemy.dialects.postgresql import ENUM
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from utils.db import db


class Product(db.Model):
    """
    Model that represents Products table
    """
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(254), nullable=False)
    brands = db.Column(db.String(254), nullable=False)
    name = db.Column(db.String(254), unique=True, nullable=False)
    site = db.Column(db.String(254), nullable=False)
    price = db.Column(db.String(254), nullable=False)
    category = db.Column(db.String(254), nullable=False)

    blogpost_id = db.Column(db.Integer, db.ForeignKey('blogpost.id'), nullable=False)


class ProductSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = Product
        load_instance = True
        fields = ["id", "gender", "brands", "name", "site", "price", "category", "blogpost_id"]


