from flask import render_template, url_for, redirect
from . import posts

@posts.route('/connections')
# @login_required
def show_posts():
    return render_template('connections.html')