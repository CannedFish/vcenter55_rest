# -*- coding: utf8 -*-

from flask import Blueprint
from flask_restplus import Api

from .auth import api as auth_ns
from .vm import api as vm_ns
from .disk import api as disk_ns
from .network import api as network_ns
from .image import api as image_ns
from .metric import api as metric_ns

blueprint = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(
    blueprint,
    title='RESTful API for vCenter 5.5',
    version='1.0',
    description='A description',
    # All API metadatas
)

api.add_namespace(auth_ns, path='/auth')
api.add_namespace(vm_ns, path='/vm')
api.add_namespace(disk_ns, path='/disk')
api.add_namespace(network_ns, path='/network')
api.add_namespace(image_ns, path='/image')
api.add_namespace(metric_ns, path='/metric')

