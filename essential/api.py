from flask import Blueprint, render_template, request, jsonify, session
from flask_login import current_user, logout_user, login_user
import random

from model import *
from .email import send_email

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

@essential_api.route("/sent-otp", methods=["POST"])
def send_otp():

    name = request.form.get("name").capitalize()
    email = request.form.get("email")
    otp = str(random.randint(10000, 99999))
    session["otp"] = otp
    mail = send_email(email,"Daily Blog - OTP",render_template("templates/otpemail.html", otp = otp, name = name))
    if mail:
        return jsonify({
            "result" : True,
            "category" : "success",
            "description" : "OTP sent successfully!!"
        })
    return jsonify({
        "result" : False,
        "category" : "danger",
        "description" : "Please try again after sometime!!"
    })


@essential_api.route("/verify-otp", methods=["POST"])
def verify_otp():
    otp = request.form.get("otp-signup")
    if otp == session["otp"]:
        return jsonify({
            "result" : True,
            "category" : "success",
            "description" : "OTP verified successfully!!"
        })
    return jsonify({
        "result" : False,
        "category" : "danger",
        "description" : "Invalid OTP"
    })