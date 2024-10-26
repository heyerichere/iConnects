from flask import Blueprint

posts = Blueprint('posts', __name__)

from . import routes  # Import routes to register with the blueprint
