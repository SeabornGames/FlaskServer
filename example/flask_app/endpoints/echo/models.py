from example.flask_app.settings.global_import import *
from seaborn.flask_server.models import ApiModel

#1log.trace("Importing endpoint test.models")


class Echo(db.Model, ApiModel):
    __table_args__ = {'extend_existing': True}
    __tablename__ = "echo"
    echo_key = db.Column(db.String, primary_key=True)
    echo_value = db.Column(db.String)
