from flask import Flask, redirect, render_template
from flask_login import current_user, logout_user, LoginManager
from flask_sqlalchemy import SQLAlchemy
from api import api
from os import environ
from dotenv import load_dotenv
from model import User,Post, db
load_dotenv('.env')


app = Flask("Daily Blog", template_folder="views")
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
db.init_app(app)
with app.app_context():
    db.create_all()
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
def main():
    post = Post.query.order_by(Post.id.desc()).all()
    if current_user.is_authenticated:
        user = User.query.filter_by(id = current_user.id).first()
        print(user.password)
        return render_template('index.html',user=user, post=post)
    else:
        return render_template('index.html',post=post)


@app.route("/<int:id>")
def profile(id):
    if current_user.is_authenticated:
        user = User.query.filter_by(id = id).first()
        post = Post.query.order_by(Post.id.desc()).filter_by(user_id = id).all()
        print(len(post))
        return render_template('profile.html',user=user, post = post)
    else:
        return render_template('home.html')


@app.route("/new-post")
def post():
    if current_user.is_authenticated:
        user = User.query.filter_by(id = current_user.id).first()
        return render_template('post.html',user=user)
    else:
        return render_template('home.html')



@app.route("/login")
def login():
    if current_user.is_authenticated:
        user = User.query.filter_by(id = current_user.id).first()
        return render_template('index.html',user=user)
    else:
        return render_template('login.html')

@app.route("/logout")
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect("/")


app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True)
