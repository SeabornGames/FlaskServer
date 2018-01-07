"""
    This module will be imported by each of the endpoint views and models,
    so it will contain anything they will generally need
"""

from seaborn.logger.logger import log
from .config import configuration
from seaborn.flask_server.setup.setup_flask import SetupFlask
from seaborn.flask_server.blueprint.blueprint import ProxyEndpoint

setup_flask = SetupFlask(configuration)
app = setup_flask.app
db = setup_flask.db
conn = ProxyEndpoint()

from seaborn.flask_server.global_import import *