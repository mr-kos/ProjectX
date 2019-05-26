from flask_wtf import Form
from wtforms import TextField, BooleanField, PasswordField
from wtforms.validators import Required, Email

class LoginForm(Form):
    email = TextField('login', validators = [Required()])
    password = PasswordField('password', validators = [Required()])
    remember_me = BooleanField('remember_me', default=False)

class RegistrationForm(Form):
    name = TextField('name', validators = [Required()])
    surname = TextField('surname', validators = [Required()])
    email = TextField('login', validators = [Required()])
    password = PasswordField('password', validators = [Required()])
    password_submit = PasswordField('password_submit', validators = [Required()])
