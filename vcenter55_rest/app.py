# -*- coding: utf8 -*-

import logging.config
import os

from flask import Flask
from vcenter55_rest import settings
from vcenter55_rest.database import DB
from vcenter55_rest.api_v1 import blueprint as api_v1

app = Flask(__name__)
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'logging.conf'))
logging.config.fileConfig(logging_conf_path)
LOG = logging.getLogger(__name__)

def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME

    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS

def initialize_app(flask_app):
    configure_app(flask_app)
    flask_app.register_blueprint(api_v1)
    DB.ins(app)

def main():
    initialize_app(app)
    LOG.info('>>>>> Starting development server at http://{}/api/ <<<<<' \
            % (app.config['SERVER_NAME'])
    app.run(debug=settings.FLASK_DEBUG)

if __name__ == "__main__":
    main()

