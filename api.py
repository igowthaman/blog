import json
from flask import Blueprint, request, jsonify
from flask_login import current_user, login_user, logout_user
from model import User, Post, db

api = Blueprint("api",__name__, url_prefix="/api")

@api.route("/login", methods=["POST"])
def login():
    if current_user.is_authenticated:
        logout_user()
    email = request.form.get("email")
    password = request.form.get("password")
    print(email)
    user = User.query.filter_by(email = email).first()
    # print(user.email)
    if user:
        if user.password == password:
            login_user(user, remember = True)
            return jsonify({
                "result" : True,
                "category" : "success",
                "Description" : "Logined successfull!!"
            })
        else:
            return jsonify({
                "result" : False,
                "category" : "danger",
                "Description" : "Invalid password"
            })
    else:
        return jsonify({
            "result" : False,
            "category" : "danger",
            "Description" : "Account not found"
        })
@api.route("/signup", methods=["POST"])
def signup():
    if current_user.is_authenticated:
        logout_user()
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    print(name,email,password)
    user = User(name=name,email=email,password=password)
    db.session.add(user)
    db.session.flush()
    db.session.commit()
    print(user.id)
    login_user(user, remember = True)
    return jsonify({
        "result" : True,
        "category" : "success",
        "Description" : "Account created successfully!!"
    })

@api.route("/post", methods=["POST"])
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

