from flask import Blueprint
from essential.api import essential_api
from essential.route import essential_route

essential = Blueprint("essential",__name__)

essential.register_blueprint(essential_route)
essential.register_blueprint(essential_api)