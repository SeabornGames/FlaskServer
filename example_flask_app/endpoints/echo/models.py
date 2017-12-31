from test.flask_app.settings.global_import import *
from seaborn.flask.models import ApiModel
import logging

log = logging.getLogger(__name__)
log.debug("Importing endpoint test.models")


class Echo(db.Model, ApiModel):
    __tablename__ = "echo"
    echo_key = db.Column(db.String, primary_key=True)
    echo_value = db.Column(db.String)
