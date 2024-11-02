from flask import render_template, url_for
from flask_login import login_user, login_required, logout_user
from . import main

@main.route('/')
def index():
    return render_template(url_for(url_for('auth', 'signin.html')))

@main.route('/home')
@login_required
def home(): 
    return render_template(url_for('main', 'home.html'))

@main.route('/profile')
@login_required
def profile(): 
    return render_template(url_for('main', 'profile.html'))

@main.route('/connections')
@login_required
def connections(): 
    return render_template(url_for('main', 'connections.html'))

