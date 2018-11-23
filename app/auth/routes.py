from flask import redirect, url_for, flash, request, render_template
from werkzeug.urls import url_parse
from flask_login import login_user
from flask_login import current_user
from app.auth import bp
from app.auth.forms import LoginForm
from app.models import User

@bp.route("/login", methods={"GET", "POST"})
def login():
    """Login page"""
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("auth.login"))
        login_user(user)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("main.index")
        return redirect(next_page)
    return render_template("auth/login.html", title="Sign In", form=form)
