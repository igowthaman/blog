from flask import Flask, render_template
from flask_login import current_user, LoginManager
from os import environ
from dotenv import load_dotenv
from essential import essential
from post import post
from model import User,Post, db
load_dotenv('.env')

from flask_pymongo import PyMongo 
mongo = PyMongo()


app = Flask("Memoir", template_folder=environ.get('VIEW'))
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
    post = db.session.query(Post, User).with_entities(
        Post.id, Post.content, Post.title, Post.user_id, User.name, Post.created_at 
    ).order_by(Post.id.desc()).all()
    if current_user.is_authenticated:
        user = User.query.filter_by(id = current_user.id).first()
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
        return render_template('index.html')


app.register_blueprint(essential)
app.register_blueprint(post)


if __name__ == '__main__':
    app.run(debug=True)
