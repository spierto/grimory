# db

from . import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class Persona(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  nome = db.Column(db.String(100), nullable = False)
  anni = db.Column(db.Integer)