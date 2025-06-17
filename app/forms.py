from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField
from wtforms.validators import DataRequired, Email

class NewPage(FlaskForm):
  title = StringField('Title', validators=[DataRequired()])
  text = TextAreaField('Text', validators=[DataRequired()])

class NewUser(FlaskForm):
  name = StringField('Name', validators=[DataRequired()])
  email = StringField('E-mail', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])

class Auth(FlaskForm):
  email = StringField('E-mail', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])