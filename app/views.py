from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm, RegistrationForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')


@app.route('/registration', methods = ['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Successful registration!')
        flash('Welcome, ' + form.name.data + ' ' + form.surname.data)
        return redirect('/index')
    return render_template('registration.html', form=form)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Successful sign in!')
        flash('Login ="' + form.email.data + '", password=' + str(form.password.data))
        return redirect('/index')
    return render_template('login.html', form=form)