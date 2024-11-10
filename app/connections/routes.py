from flask import render_template, url_for, redirect
from . import connections

@connections.route('/connections')
# @login_required
def show_connections():
    return render_template('connections.html')