# _*_ coding: utf-8 _*_
from flask import render_template, request, session, redirect, url_for
from models import User
import json


def register_view(app):
    @app.route('/')
    @app.route('/index')
    def index():
        if 'username' in session:
            username = session['username']
            data = {"username": username}
            return render_template("index.html", **locals())
        else:
            return redirect(url_for('login'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            user = User.query.filter_by(username=username).first()
            if user is not None and password == user.password:
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
