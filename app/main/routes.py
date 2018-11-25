from flask import current_app, render_template
from app.main import bp

@bp.route("/")
def index():
    """Index page"""
    return render_template("main/index.html", title="Home")

@bp.route("/about_me")
def about_me():
    """About Me page"""
    return render_template("main/about_me.html", title="About Me")
