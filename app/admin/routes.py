from flask import render_template, flash, url_for, redirect
from flask_login import login_required
from app import db
from app.admin.forms import PostForm
from app.models import Post
from app.admin import bp

@bp.route("/editorial")
@login_required
def editorial():
    """Admin Editorial page"""
    return render_template("admin/home.html", title="Admin Edtorial")

@bp.route("/editorial/write_post", methods=["GET", "POST"])
@login_required
def write_post():
    """Write Post page"""
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author="Admin")
        db.session.add(post)
        db.session.commit()
        flash("The post has been added to the blog!")
        return redirect(url_for("admin.editorial"))
    return render_template("admin/write_post.html", title="Write Post", form=form)
