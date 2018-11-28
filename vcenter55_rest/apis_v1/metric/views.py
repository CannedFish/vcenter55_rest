# -*- coding: utf8 -*-

from flask_restplus import Namespace, Resource, fields

api = Namespace('metrics', description='Metrics related operations')

vm = api.model('Metric', {})
