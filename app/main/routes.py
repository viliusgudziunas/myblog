from flask import current_app
from app.main import bp

@bp.route("/")
def index():
    """Index Page"""
    return "Hello World!"
