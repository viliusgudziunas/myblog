from werkzeug.urls import url_parse
from flask import render_template, flash, url_for, redirect, request
from flask_login import login_required, login_user, current_user
from app import db
from app.admin.forms import PostForm, LoginForm, EditAboutMeForm, EditAboutThisBlogForm
from app.models import User, Post, About_Me_Post, About_This_Blog_Post
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
    """Admin editorial page"""
    return render_template("admin/editorial.html", title="Admin Edtorial")

@bp.route("/editorial/write_post", methods=["GET", "POST"])
@login_required
def write_post():
    """Write post page"""
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data)
        db.session.add(post)
        db.session.commit()
        flash("The post has been added to the blog!")
        return redirect(url_for("admin.editorial"))
    return render_template("admin/write_post.html", title="Write Post", form=form)

@bp.route("/editorial/write_about_me", methods=["GET", "POST"])
@login_required
def write_about_me():
    """Edit about me page"""
    form = EditAboutMeForm()
    if form.validate_on_submit():
        about_me_post = About_Me_Post(body=form.body.data)
        db.session.add(about_me_post)
        db.session.commit()
        flash("About Me page has been updated.")
        return redirect(url_for("admin.editorial"))
    return render_template("admin/write_about_me.html", title="Edit About Me Page", form=form)

@bp.route("/editorial/write_about_this_blog", methods=["GET", "POST"])
@login_required
def write_about_this_blog():
    """Edit about this blog page"""
    form = EditAboutThisBlogForm()
    if form.validate_on_submit():
        about_this_blog_post = About_This_Blog_Post(body=form.body.data)
        db.session.add(about_this_blog_post)
        db.session.commit()
        flash("About This Blog page has been updated.")
        return redirect(url_for("admin.editorial"))
    return render_template("admin/write_about_this_blog.html", title="Edit About This Blog Page", form=form)
