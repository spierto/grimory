from datetime import datetime
from .forms import Auth, NewPage, NewUser
from . import app
from flask import abort, redirect, render_template, request, session, url_for
from .models import Page, User, db

# HOMEPAGE #
@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html', title='Grimory')

# AUTHENTICATION #
@app.route('/auth', methods=['GET', 'POST'])
def auth():
  form = Auth()
  if request.method == 'POST':
    user = User.query.filter_by(email=form.email.data).first()
    if user and user.password == form.password.data:
      session['user_id'] = user.id
      session['username'] = user.name
      #debug
      print("Session saved:", session)
      return redirect('/')
    else:
      abort(401)
  return render_template('auth.html', form=form, title='Login')

# LOGOUT #
@app.route('/logout')
def logout():
  session.pop('username', None)
  return redirect('/')

# NEW USER #
@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    form = NewUser()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    return render_template('new_user.html', form=form, title='Register')

# USER PAGE #
@app.route('/user')
def user():
  pass

# WRITE A NEW PAGE #
@app.route('/write', methods=['GET', 'POST'])
def write():
  form = NewPage()
  if request.method == 'POST' and form.validate():
    if 'user_id' in session:
      author_id = session['user_id']
    else:
      return abort(401)
    
    title = form.title.data
    text = form.text.data
    page = Page(author_id=author_id, title=title, text=text, date = datetime.now())
    db.session.add(page)
    db.session.commit()
    return redirect(url_for('read'))
  return render_template('write.html', form=form, title='Write a new page')

# EDIT A PAGE #
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def page_edit(id):
  page = Page.query.get_or_404(id)
  form = NewPage(obj=page)
  if request.method == 'POST' and form.validate():
    page.title = form.title.data
    page.text = form.text.data
    db.session.add(page)
    db.session.commit()
    return redirect(url_for('read_id', id=page.id))
  return render_template('edit-page.html', form=form, title='Edit this page')

# DELETE A PAGE #
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
  page = Page.query.get_or_404(id)
  db.session.delete(page)
  db.session.commit()
  return redirect(url_for('read', id=page.id))

# READ ARCHIVE OF PAGES #
@app.route('/read')
def read():
  pages = pages = Page.query.order_by(Page.date.desc()).all()
  return render_template('read.html', pages=pages, title='Read')

# READ ONE SPECIFIC PAGE #
@app.route('/read/<int:id>')
def read_id(id):
  page = Page.query.get_or_404(id)
  author_name = page.author.name
  return render_template('read-id.html', page=page, author_name = author_name, title='Reading')

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

@app.route('/testuser')
def testuser():
  users = User.query.all()
  return render_template('test-user.html', users=users, title='Test Users')

@app.route('/debug_session')
def debug_session():
  return f'session: {str(session)}'