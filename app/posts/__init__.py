from flask import Blueprint

posts = Blueprint('posts', __name__, template_folder='templates')

from . import routes  # Import routes to register with the blueprint