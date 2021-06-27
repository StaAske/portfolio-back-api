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

class Projects(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.Text)
    site_link = db.Column(db.String(500))
    github_link = db.Column(db.String(500))
    skills = db.Column(db.String(500))
    image = db.Column(db.LargeBinary)
    date_time = db.Column(db.String(200))

    def __init__(self, title, description, site_link, github_link, skills, image, date_time):
        self.title = title
        self.description = description
        self.site_link = site_link
        self.github_link = github_link
        self.skills = skills
        self.image = image
        self.date_time = date_time
