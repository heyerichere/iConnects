from flask import Blueprint

posts = Blueprint('posts', __name__, static_folder='statics', static_url_path='/posts/statics')

from . import routes  # Import routes to register with the blueprint