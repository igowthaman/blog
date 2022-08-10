from flask import Blueprint
from post.api import post_api
from post.route import post_route

post = Blueprint("post",__name__)

post.register_blueprint(post_route)
post.register_blueprint(post_api)