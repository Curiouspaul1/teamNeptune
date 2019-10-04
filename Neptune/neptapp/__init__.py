from flask import Flask
from flask-sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 

app = Flask(__name__)

import os
uri = os.environ.get('dburi')
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

import application.models
import application.views
