# -*- coding: utf8 -*-

from flask_restplus import Namespace, Resource, fields

api = Namespace('auth', description='Authetication related operations')

vm = api.model('Auth', {})
