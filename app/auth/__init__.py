from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import routes #import routes to register with the blueprint
