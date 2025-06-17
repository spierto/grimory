from flask import Flask, session

app = Flask(__name__)

app.static_folder = 'static'
app.config['SECRET_KEY'] = 'secret-key'

from . import routes
from . import models