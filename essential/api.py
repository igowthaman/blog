from flask import Blueprint, render_template, request, jsonify
from flask_login import current_user, logout_user, login_user
from model import *

essential_api = Blueprint("essential_api",__name__,url_prefix="/api")

@essential_api.route("/login", methods=["POST"])
def login():
    if current_user.is_authenticated:
        logout_user()
    email = request.form.get("email")
    password = request.form.get("password")
    print(email)
    user = User.query.filter_by(email = email).first()

    if user:
        if user.password == password:
            login_user(user, remember = True)
            return jsonify({
                "result" : True,
                "category" : "success",
                "description" : "Logined successfull!!"
            })
        else:
            return jsonify({
                "result" : False,
                "category" : "danger",
                "description" : "Invalid password"
            })
    else:
        return jsonify({
            "result" : False,
            "category" : "danger",
            "description" : "Account not found"
        })

        
@essential_api.route("/signup", methods=["POST"])
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
        "description" : "Account created successfully!!"
    })
