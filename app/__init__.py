import os
from flask import Flask, current_app
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    """Constructs a Flask application instance"""
    app = Flask(__name__)
    app.config.from_object(config_class)

    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app

from app import models
