from sqlalchemy.dialects.postgresql import ENUM, ARRAY
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from utils.db import db


class Blogpost(db.Model):
    """
    Model that represents Blogpost table
    """
    __tablename__ = 'blogpost'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(254), nullable=False)
    gender = db.Column(db.String(254), nullable=False)
    text = db.Column(db.String(254), nullable=False)
    category = db.Column(db.String(254), nullable=False)
    products = db.Column(ARRAY(db.Integer), nullable=True)
    product = db.relationship('Product', backref='blogpost', lazy=True)


class BlogpostSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = Blogpost
        load_instance = True
