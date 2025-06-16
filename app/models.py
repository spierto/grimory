# db

from datetime import datetime
from . import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(100), nullable = False)
  email = db.Column(db.String(100), unique = True, nullable = False)
  pages = db.relationship('Page', backref = 'author', lazy = True)

class Page(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(200), nullable = False)
  author = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
  text = db.Column(db.Text, nullable = False)
  date = db.Column(db.DateTime, default=datetime.now())