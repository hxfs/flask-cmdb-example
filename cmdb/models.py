# _*_ coding: utf-8 _*_

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'opm_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(90), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    group_name = db.Column(db.String(50), nullable=False)
    message_num = db.Column(db.Integer)

    def __init__(self, username, password, message, email):
        self.username = username
        self.password = password
        self.email = email
        self.message = message

    def __repr__(self):
        return '<User %r>' % self.username


class Group(db.Model):
    __tablename__ = 'opm_group'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    groupname = db.Column(db.String(50), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('opm_user.id'))

    def __repr__(self, groupname):
        return '<Group %r>' % self.groupname


class Message_status(db.Model):
    __tablename__ = 'opm_message_status'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    send_user = db.Column(db.String(50), nullable=False, unique=True)
    recv_user = db.Column(db.String(50), nullable=False, unique=True)
    send_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Integer, nullable=False)

    def __init__(self, send_user, recv_user, send_time, send_text):
        self.send_user = send_user
        self.recv_user = recv_user
        self.send_time = send_time
        self.send_text = send_text

    def __repr__(self, send_user):
        return '<Message %r>' % self.send_user


class Ticket_type(db.Model):
    __tablename__ = 'opm_ticket_type'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_name = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, type_name):
        self.type_name = type_name

    def __repr__(self, type_name):
        return '<Ticket_type %r>' % self.type_name


class Ticket(db.Model):
    __tablename__ = 'opm_ticket'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ticket_sn = db.Column(db.String(20), nullable=False, unique=True)
    ticket_type = db.Column(
        db.String(50), db.ForeignKey('opm_ticket_type.type_name'))
    ticket_name = db.Column(db.String(50), nullable=False)
    create_user = db.Column(db.String(50), nullable=False)
    recv_user = db.Column(db.String(50), nullable=False)
    ticket_text = db.Column(db.String(255), nullable=False)

    def __init__(self, ticket_sn, ticket_type, ticket_name, create_user,
                 recv_user, ticket_text):
        self.ticket_sn = ticket_sn
        self.ticket_type = ticket_type
        self.ticket_name = ticket_name
        self.create_user = create_user
        self.recv_user = recv_user
        self.ticket_text = ticket_text

    def __repr__(self, send_user):
        return '<Message %r>' % self.send_user
