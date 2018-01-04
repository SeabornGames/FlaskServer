"""
    This module will be imported by each of the endpoint views and models,
    so it will contain anything they will generally need
"""
from .config import configuration
from logging import getLogger
from seaborn.flask_server.setup.setup_flask import SetupFlask
from seaborn.flask_server.blueprint.blueprint import ProxyEndpoint

#log = configuration.setup_logging()
#log = getLogger(__name__)
setup_flask = SetupFlask(configuration)
app = setup_flask.app
db = setup_flask.db
conn = ProxyEndpoint()

from seaborn.flask_server import *