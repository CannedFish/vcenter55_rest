# -*- coding: utf8 -*-

from flask_restplus import Namespace, Resource, fields

api = Namespace('network', description='Networks related operations')

vm = api.model('Network', {})
