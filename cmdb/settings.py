# _*_ coding: utf-8 _*_

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Dev(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:redhat@localhost/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
    DEBUG = True


config = {
    'default': Dev
}
