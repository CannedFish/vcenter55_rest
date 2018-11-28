# -*- coding: utf8 -*-

from flask_restplus import Namespace, Resource, fields

api = Namespace('disks', description='Disks related operations')

vm = api.model('Disk', {})
