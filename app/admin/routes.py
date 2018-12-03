from werkzeug.urls import url_parse
from flask import render_template, flash, url_for, redirect, request
from flask_login import login_required, login_user, current_user
from app import db
from app.admin.forms import PostForm, LoginForm
from app.models import User, Post
from app.admin import bp

@bp.route("/login", methods={"GET", "POST"})
def login():
    """Login page"""
    if current_user.is_authenticated:
        return redirect(url_for('admin.editorial'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("admin.login"))
        login_user(user)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("admin.editorial")
        return redirect(next_page)
    return render_template("admin/login.html", title="Sign In", form=form)

@bp.route("/editorial")
@login_required
def editorial():
    """Admin Editorial page"""
    return render_template("admin/editorial.html", title="Admin Edtorial")

@bp.route("/editorial/write_post", methods=["GET", "POST"])
@login_required
def write_post():
    """Write Post page"""
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data)
        db.session.add(post)
        db.session.commit()
        flash("The post has been added to the blog!")
        return redirect(url_for("admin.editorial"))
    return render_template("admin/write_post.html", title="Write Post", form=form)
