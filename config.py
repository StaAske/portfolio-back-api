import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'storage.db')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

class ClientReq(db.Model):
    __tablename__ = 'clientReq'
    request_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    message = db.Column(db.Text)
    date_time = db.Column(db.String(200))

    def __init__(self, name, email, message, date_time):
        self.name = name
        self.email = email
        self.message = message
        self.date_time = date_time

class ClientReqSchema(ma.Schema):
    class Meta:
        model = ClientReq
        fields = ("id", "name", "email", "message", "date_time")
        sqla_session = db.session

class CVStorage(db.Model):
    __tablename__ = 'cvStorage'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    file = db.Column(db.LargeBinary)
