from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy import literal

db = SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(225))
    is_active = db.Column(db.Boolean, default=True, server_default=literal(True))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Post(db.Model, UserMixin):
    __tablename__ = "post"
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(225))
    content = db.Column(db.String(2550))
    is_active = db.Column(db.Boolean, default=True, server_default=literal(True))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)