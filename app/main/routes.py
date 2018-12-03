from flask import current_app, render_template
from app.main import bp
from app.models import Post

@bp.route("/")
def index():
    """Index page"""
    posts = Post.query.all()
    return render_template("main/index.html", title="Home", posts=posts)

@bp.route("/about_me")
def about_me():
    """About me page"""
    return render_template("main/about_me.html", title="About Me")

@bp.route("/about_this_blog")
def about_this_blog():
    """About this blog page"""
    return render_template("main/about_this_blog.html", title="About This Blog")
