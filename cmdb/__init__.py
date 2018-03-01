# _*_ coding: utf-8 _*_

from flask import Flask
from settings import config
from .models import db
from .views import register_view


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    register_view(app)
    return app
