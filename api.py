import json
from flask import Blueprint, request, jsonify
from flask_login import current_user, login_user, logout_user
from model import User, Post, db

api = Blueprint("api",__name__, url_prefix="/api")




