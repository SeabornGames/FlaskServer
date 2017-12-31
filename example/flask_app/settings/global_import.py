from seaborn.flask.blueprint.blueprint import ProxyEndpoint
from seaborn import *
from seaborn.flask.setup.setup_flask import SetupFlask
from seaborn.calling_function import function_kwargs
from seaborn import *

from sqlalchemy import *

import datetime
import random
import json

from .config import configuration

configuration.setup_logging()

setup_flask = SetupFlask(configuration)
app = setup_flask.app
db = setup_flask.db

conn = ProxyEndpoint()
