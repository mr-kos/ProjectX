from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, models
from app.models import User
from app.forms import LoginForm, RegistrationForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter(
            User.email == form.email.data).first()
        if user.email == form.email.data:
            flash('User already exists. Sign In or enter different email.')
        else:
            u = models.User(name=form.name.data, surname=form.surname.data,
                            email=form.email.data, password=form.password.data)
            db.session.add(u)
            db.session.commit()
            flash('Successful registration!')
            flash('Welcome, ' + form.name.data + ' ' + form.surname.data)
            return redirect('/index')
    return render_template('registration.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # if g.user is not None and g.user.is_authenticated():
    #     return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter(
            User.email == form.email.data, User.password == form.password.data).first()
        try:
            flash('Signing in...')
            flash('Login ="' + user.email + '", password=' + user.password)
            flash('Done!')
            session['remember_me'] = form.remember_me.data
            return redirect(url_for('index'))
        except Exception:
            flash("Wrong login or password! Please, try again")
            print("Wrong login or password")
    return render_template('login.html', form=form)
