# -*- coding: utf8 -*-

from flask_restplus import Namespace, Resource, fields

api = Namespace('images', description='Images related operations')

vm = api.model('Image', {})
