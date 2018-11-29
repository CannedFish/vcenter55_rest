# -*- coding: utf8 -*-

from flask_sqlalchemy import SQLAlchemy

class DB(object):

    db = None

    @classmethod
    def ins(cls, app = None):
        if db is None:
            db = SQLAlchemy(app)
        return db

