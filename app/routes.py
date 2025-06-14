from . import app
from flask import render_template, request

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

# write a new page (new)
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

# test: read con csv
def formatta(riga):
  return f'<li>{riga["data"]}:\n<strong>{riga["titolo"]}</strong>:\n{riga["testo"]}</li>'

import csv
@app.route('/test')
def test():
  with open('test-entry.csv', 'r') as f:
    output = '<h1>Read</h1><h2>Entries</h2>'
    output += '<ul>'
    for row in csv.DictReader(f, delimiter= ','):
      output += formatta(row)
    output += '</ul>'
  return output

# fine test

# read one specific entry
@app.route('/read/<int:placeholder_id>')
def read_id(placeholder_id):
  return f'<h1>Read id: {placeholder_id}</h1>'

# filter entries based on date
@app.route('/read/<month>')
def read_month(month):
  return f'<h1>Read by month: {month}</h1>'