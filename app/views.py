from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, models
from app.models import User
from app.forms import LoginForm, RegistrationForm


@app.route('/')
@app.route('/index')
@login_required
def index():
    # user = g.user
    return render_template('main.html')

# @app.before_request
# def before_request():
#     g.user = current_user


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter(
            User.email == form.email.data).first()
        if user is not None:
            flash('User already exists. Sign In or enter different email.')
        else:
            u = models.User(name=form.name.data, surname=form.surname.data,
                            email=form.email.data)
            u.set_password(form.password.data)
            db.session.add(u)
            db.session.commit()
            flash('Successful registration!')
            login_user(u, remember = True)
            return redirect('/index')
    return render_template('registration.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter(
            User.email == form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid e-mail or password')
            return redirect(url_for('login'))
        flash('Signing in...Done!')
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
