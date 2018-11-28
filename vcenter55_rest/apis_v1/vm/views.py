# -*- coding: utf8 -*-

from flask_restplus import Namespace, Resource, fields

api = Namespace('vms', description='VMs related operations')

vm = api.model('VM', {})
