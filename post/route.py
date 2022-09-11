from flask import Blueprint, render_template, redirect
from flask_login import current_user, logout_user
from model import *

post_route = Blueprint("post_route",__name__)


@post_route.route("/new-post")
def post1():
    if current_user.is_authenticated:
        user = User.query.filter_by(id = current_user.id).first()
        return render_template('post.html',user=user)
    else:
        return render_template('home.html')


@post_route.route("/post/<int:post_id>")
def post(post_id):
    if current_user.is_authenticated:
        user = User.query.filter_by(id = current_user.id).first()
        dpost = Post.query.filter_by(id = post_id).first()
        return render_template('post.html',user=user, post=dpost)
    else:
        return render_template('home.html')


@post_route.route("/post/new")
def new_post():
    if current_user.is_authenticated:
        user = User.query.filter_by(id = current_user.id).first()
        return render_template('new-post.html',user=user)
    else:
        return render_template('home.html')
