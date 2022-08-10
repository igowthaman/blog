from flask import Blueprint, render_template, redirect
from flask_login import current_user, logout_user
from model import *

essential_route = Blueprint("essential_route",__name__)

@essential_route.route("/login")
def login():
    if current_user.is_authenticated:
        user = User.query.filter_by(id = current_user.id).first()
        return render_template('index.html',user=user)
    else:
        return render_template('essential/login.html')

@essential_route.route("/logout")
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect("/")