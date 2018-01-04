from example_flask_app.settings.global_import import *
from example_flask_app.endpoints.user.models import User
from example_flask_app.endpoints.account.models import Account
from seaborn.flask_server.models import ApiModel

from sqlalchemy.orm import backref

log.trace("Importing endpoint account.access.models")


class Access(db.Model, ApiModel):
    __tablename__ = "account_access"
    __table_args__ = {'extend_existing': True}

    access_id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.account_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('usr.user_id'))

    user = db.relationship(User, backref=backref(
        'account_access', lazy='dynamic', uselist=True))
    account = db.relationship(Account, backref=backref(
        'user_access', lazy='dynamic', uselist=True))
