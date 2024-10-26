from flask import render_template, redirect, url_for, flash

from . import auth

@auth.route('/login', methods=['GET', 'POST'])
def login(): 
    return render_template('auth/signin.html')


@auth.route('/signup', methods=['GET', 'POST'])
def signup(): 
    return render_template('auth/signin.html')