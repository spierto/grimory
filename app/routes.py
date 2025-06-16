from datetime import datetime
from .forms import NewPage, NewUser
from . import app
from flask import redirect, render_template, request, url_for
from .models import Page, User, db

# HOMEPAGE #
@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html', title='Grimory')

# SUCCESS #
@app.route('/success')
def success():
  return '<h1>Success</h1>'

# NEW USER #
@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    form = NewUser()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('success'))
    return render_template('new_user.html', form=form, title='Create New User')

# AUTHENTICATION #
@app.route('/auth', methods=['GET', 'POST'])
def auth():
  if request.method == 'POST':
    return '<h1>Autenticazione in corso...</h1>'
  else:
    return '<h1>Pagina di login</h1><p>...</p>'

# USER PAGE #
@app.route('/user')
def user():
  pass

# WRITE A NEW PAGE #
@app.route('/write', methods=['GET', 'POST'])
def write():
  form = NewPage()
  if request.method == 'POST' and form.validate():
    author_id = 0
    title = form.title.data
    text = form.text.data
    page = Page(author_id=author_id, title=title, text=text, date = datetime.now())
    db.session.add(page)
    db.session.commit()
    return redirect ('/success')
  return render_template('write.html', form=form, title='Write a new page')

# EDIT A PAGE #
@app.route('/write/<int:id>/edit', methods=['GET', 'POST'])
def page_edit():
  page = Page.query_or_404(id)
  form = NewPage(obj=page)
  if request.method == 'POST' and form.validate():
    title = form.title.data
    text = form.text.data
    page = NewPage(title=title, text=text)
    db.session.commit()
    return redirect ('/success')
  return render_template('write.html', form=form, title='Edit this page')

# DELETE A PAGE #
@app.route('/delete/<int:placeholder_id>')
def delete(placeholder_id):
  return f'<h1>Delete id: {placeholder_id}</h1>'

# READ ARCHIVE OF PAGES #
@app.route('/read')
def read():
  pages = Page.query.all()
  return render_template('read.html', pages=pages, title='Read')

# READ ONE SPECIFIC PAGE #
@app.route('/read/<int:id>')
def read_id(id):
  return f'<h1>Read id: {id}</h1>'

# FILTER PAGES BASED ON DATE #
@app.route('/read/<month>')
def read_month(month):
  return f'<h1>Read by month: {month}</h1>'

### TESTS ###

# test: template base
@app.route('/testtemp')
def testtemplate():
  return render_template('prova.html', title='Test title')
# fine test

# test: card read
@app.route('/read-test')
def readtest():
  pages = Page.query.all()
  return render_template('read-new.html', pages=pages, title='Test read')