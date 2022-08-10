from flask import Blueprint, render_template, request, jsonify
from flask_login import current_user, logout_user, login_user
from model import *
import json

post_api = Blueprint("post_api",__name__,url_prefix="/api")

@post_api.route("/post/new", methods=["POST"])
def post():
    data = json.loads(request.data)
    title = data["title"]
    content = data["content"]
    user = int(data["user"])
    post = Post(title=title,content=content,user_id=user)
    db.session.add(post)
    db.session.flush()
    db.session.commit()
    return jsonify({
        "result" : True,
        "category" : "success",
        "Description" : "Post created successfully!!"
    })

@post_api.route("/post/delete", methods=["DELETE"])
def delete():
    data = json.loads(request.data)
    if "id" not in data:
        return {
            "result" : False,
            "category" : "danger",
            "Description" : "Post deletion failed"
        }
    
    post = Post.query.filter_by(id = data[id]).first()
    post.is_active  = False
    db.session.flush()
    db.session.commit()
    return {
        "result" : True,
        "category" : "success",
        "Description" : "Post deleted successfully!!"
    }