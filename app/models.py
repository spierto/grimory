# db

from datetime import datetime

from sqlalchemy import MetaData
from . import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)
metadata_obj = MetaData()

class User(db.Model):
  metadata_obj
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(100), nullable = False)
  email = db.Column(db.String(100), unique = True, nullable = False)
  password = db.Column(db.String(16), nullable = False)
  pages = db.relationship('Page', backref = 'author', lazy = True)

class Page(db.Model):
  metadata_obj
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(200), nullable = False)
  author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
  text = db.Column(db.Text, nullable = False)
  date = db.Column(db.DateTime, default=datetime.now())