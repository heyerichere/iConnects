from flask import render_template
from . import main

@main.route('/')
def home(): 
    return render_template('main/home.html')

@main.route('/profile')
def profile(): 
    return render_template('main/profile.html')

@main.route('/connections')
def connections(): 
    return render_template('main/connections.html')