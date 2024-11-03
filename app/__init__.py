import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.signin'  # Redirect to login page if not authenticated

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    # db.init_app(app)
    # migrate.init_app(app, db)
    # login_manager.init_app(app)

    # Register models
    # from .auth.models import Student, Alum

    # Register blueprints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .posts import posts as posts_blueprint
    app.register_blueprint(posts_blueprint)
    
    return app
