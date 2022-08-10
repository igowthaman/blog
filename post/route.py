from flask import Blueprint, render_template, redirect
from flask_login import current_user, logout_user
from model import *

post_route = Blueprint("post_route",__name__)