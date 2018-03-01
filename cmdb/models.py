# _*_ coding: utf-8 _*_

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'userinfo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(200))
    email = db.Column(db.String(40), nullable=False)

    def __init__(self, username, password, message, email):
        self.username = username
        self.password = password
        self.email = email
        self.message = message

    def __repr__(self):
        return '<User %r>' % self.username
