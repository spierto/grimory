from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('diaryhome.html')

@app.route('/auth')
def auth():
  return '<h1>Auth</h2>'

@app.route('/write')
def write():
  return render_template('write.html')

@app.route('/read')
def read():
  return render_template('diarypages.html')