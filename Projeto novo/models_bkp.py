from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from app import db

class User(db.model, UserMixin):
    id = db.column(db.string, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    