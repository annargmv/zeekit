import json
from models import Product, ProductSchema
from flask import Blueprint
from utils.db import session
from sqlalchemy import or_

products_api = Blueprint("products_api", __name__)


@products_api.route("/products", methods=["GET"])
@products_api.route("/products/<limit>/<offset>")
def get_products(limit=20, offset=0):
    """
    Get function for all products api call
    @param limit: limit for query with default value
    @param offset: offset for query with default value
    :return: a json object of the call
    """
    all_products = session.query(Product).limit(limit).offset(offset).all()
    product_schema = ProductSchema(many=True, )
    response = product_schema.dump(all_products)

    return json.dumps(response)


@products_api.route("/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    """
    Get function for a single products api call.
    @param product_id: product_is for query
    :return: a json object of a single blogpost
    """
    product_by_id = session.query(Product).get(product_id)
    blogpost_schema = ProductSchema(many=False)
    response = blogpost_schema.dump(product_by_id)

    return json.dumps(response)


@products_api.route("/filter/<param>", methods=["GET"])
@products_api.route("/filter/<param>/<limit>/<offset>")
def get_products_by_filter(param, limit=20, offset=0):
    """
    Get function with filter by gender for products api call
    @param param: gender for query to filter
    @param limit: limit for query with default value
    @param offset: offset for query with default value
    :return: a json object of filtered param
    """
    product_filtered_by_gender = session.query(Product).filter(or_(
        Product.name.like(param),
        Product.gender.like(param),
        Product.brands.like(param),
        Product.site.like(param),
        Product.price.like(param),
        Product.blogpost_id == (param),
        Product.category.like(param),
    )).limit(limit).offset(offset)
    blogpost_schema = ProductSchema(many=True)
    response = blogpost_schema.dump(product_filtered_by_gender)

    return json.dumps(response)
