# _*_ coding: utf-8 _*_
from flask import render_template, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from models import User
import json


def register_view(app):
    def check_login(func):
        @wraps(func)
        def wrapper(*args, **kw):
            if 'login' not in request.full_path:
                if 'username' in session:
                    username = session['username']
                    data = {'username': username}
                    return func(*args, **data)
                else:
                    return redirect(url_for('login'))
        return wrapper

    @app.route('/')
    @app.route('/index')
    @check_login
    def index(*args, **kw):
        return render_template('index.html', **locals())

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            user = User.query.filter_by(username=username).first()
            if user is not None and check_password_hash(user.password,password):
                messages = {
                    "code": 200,
                    "data": {
                        "status": "success",
                        "info": None
                    }
                }
                session['username'] = username
                return json.dumps(messages)
            else:
                messages = {
                    "code": 200,
                    "data": {
                        "status": "failed",
                        "info": "username or password error"
                    }
                }
                return json.dumps(messages)
        return render_template("login.html")

    @app.route('/logout')
    def logout():
        if 'username' in session:
            session.pop('username')
            messages = {
                "code": 200,
                "data": {
                    "status": "success",
                    "info": None
                }
            }
            return json.dumps(messages)
        else:
            return "null"

    @app.route('/vpnuser')
    @check_login
    def vpnuser(*args, **kw):
        return render_template('vpn_user.html', **locals())

    @app.route('/jumpuser')
    @check_login
    def jumpuser(*args, **kw):
        return render_template('jump_user.html', **locals())

    @app.route('/groupname')
    @check_login
    def groupname(*args, **kw):
        return render_template('group.html', **locals())

    @app.route('/opm_user')
    @check_login
    def opm_user(*args, **kw):
        return render_template("opm_user.html", **locals())

    @app.route('/iamuser')
    @check_login
    def iamuser(*args, **kw):
        return render_template("iam.html", **locals())

    @app.route('/test', methods=['GET', 'POST'])
    def test():
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            if username and password:
                user = User.query.filter_by(username=username).first()
                print user.username
                return "POST style"
        else:
            return "GET style"
