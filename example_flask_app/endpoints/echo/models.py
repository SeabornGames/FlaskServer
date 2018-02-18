from example_flask_app.settings.global_import import *
from seaborn_flask_server.models import ApiModel

log.trace("Importing endpoint test.models")


class Echo(db.Model, ApiModel):
    __tablename__ = "echo"
    __table_args__ = {'extend_existing': True}

    echo_key = db.Column(db.String, primary_key=True)
    echo_value = db.Column(db.String)
