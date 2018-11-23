from flask import current_app, render_template
from app.main import bp

@bp.route("/")
def index():
    """Index Page"""
    return render_template("index.html", title="Home")
