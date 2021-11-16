import json
from models import Blogpost, BlogpostSchema
from flask import Blueprint
from utils.db import session
from sqlalchemy import or_

blogpost_api = Blueprint("blogpost_api", __name__)


@blogpost_api.route("/blogpost", methods=["GET"])
@blogpost_api.route("/blogpost/<limit>/<offset>")
def get_blogpost(limit=20, offset=0):
    """
    Get function for all blog posts api call
    @param limit: limit for query with default value
    @param offset: offset for query with default value
    :return: a json object of the call
    """
    all_blogposts = session.query(Blogpost).limit(limit).offset(offset).all()
    blogpost_schema = BlogpostSchema(many=True)
    response = blogpost_schema.dump(all_blogposts)

    return json.dumps(response)


@blogpost_api.route("/<int:blog_id>", methods=["GET"])
def get_blogpost_by_id(blog_id):
    """
    Get function for a single blog post api call.
    @param blog_id: blog_id for query
    :return: a json object of a single blogpost
    """
    blogpost_by_id = session.query(Blogpost).get(blog_id)
    blogpost_schema = BlogpostSchema(many=False)
    response = blogpost_schema.dump(blogpost_by_id)

    return json.dumps(response)


@blogpost_api.route("/filter/<param>", methods=["GET"])
@blogpost_api.route("/filter/<param>/<limit>/<offset>")
def get_blog_post_by_filter(param, limit=20, offset=0):
    """
    Get function with filter by gender for blog post api call
    @param param: gender for query to filter
    @param limit: limit for query with default value
    @param offset: offset for query with default value
    :return: a json object of filtered param
    """
    blogpost_filtered_by_gender = session.query(Blogpost).filter(or_(
        Blogpost.name.like(param),
        Blogpost.gender.like(param),
        Blogpost.text.like(param),
        Blogpost.category.like(param),
    )).limit(limit).offset(offset)
    blogpost_schema = BlogpostSchema(many=True)
    response = blogpost_schema.dump(blogpost_filtered_by_gender)

    return json.dumps(response)





