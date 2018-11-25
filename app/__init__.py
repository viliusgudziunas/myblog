import os
from flask import Flask, current_app
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment
from flask_login import LoginManager
from config import Config

bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()
moment = Moment()
login = LoginManager()

def create_app(config_class=Config):
    """Constructs a Flask application instance"""
    app = Flask(__name__)
    app.config.from_object(config_class)

    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    moment.init_app(app)
    login.init_app(app)

    from app.admin import bp as admin_bp
    app.register_blueprint(admin_bp, url_prefix="/admin")

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app

from app import models
