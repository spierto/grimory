from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

# homepage
@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html')

# navbar
@app.route('/navbar')
def navbar():
  return render_template('navbar.html')

# authentication
@app.route('/auth', methods=['GET', 'POST'])
def auth():
  if request.method == 'POST':
    return '<h1>Autenticazione in corso...</h1>'
  else:
    return '<h1>Pagina di login</h1><p>...</p>'

# write a new page
@app.route('/write')
def write():
  return render_template('write.html')

# edit a page
@app.route('/edit/<int:placeholder_id>')
def edit(placeholder_id):
  return f'<h1>Edit id: {placeholder_id}</h1>'

# delete a page
@app.route('/delete/<int:placeholder_id>')
def delete(placeholder_id):
  return f'<h1>Delete id: {placeholder_id}</h1>'

# read: archive of entries
@app.route('/read')
def read():
  return render_template('read.html')

# read one specific entry
@app.route('/read/<int:placeholder_id>')
def read(placeholder_id):
  return f'<h1>Read id: {placeholder_id}</h1>'

# filter entries based on date
@app.route('/read/<month>')
def read_month():
  return '<h1>Read by month</h1>'