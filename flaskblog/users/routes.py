from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import db, bcrypt
from flaskblog.models import User
from flaskblog.users.forms import (
    RegistrationForm,
    LoginForm,
    UpdateAccountForm,
    RequestResetForm,
    ResetPasswordForm,
)
from flaskblog.users.utils import save_picture, send_reset_email


users = Blueprint("users", __name__)


# route for the register page
@users.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(
            username=form.username.data, email=form.email.data, password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created! You are now able to log in!", "success")
        return redirect(url_for("users.login"))

    return render_template("register.html", title="Register", form=form)


# route for the login page
@users.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("main.home"))
        else:
            flash("Login Unsuccessful. Please check email and password", "danger")
    return render_template("login.html", title="Login", form=form)


# route for the logout page
@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))


# route for the account page
@users.route("/account")
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        # This will save the picture in the profile_pics folder
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your account has been updated!", "success")
        return redirect(url_for("users.account"))

    # This will fill the current data with username and email in the form for the current user
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email

    image_file = url_for("static", filename="profile_pics/" + current_user.image_file)
    return render_template(
        "account.html", title="Account", image_file=image_file, form=form
    )


# Viewing all the posts of a user
@users.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get("page", 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    # get the first user with this username, or give the error 404 (not found)

    posts = (
        Post.query.filter_by(author=user)
        .order_by(Post.date_posted.desc())
        .paginate(page=page, per_page=5)
    )
    return render_template("user_posts.html", posts=posts, user=user)


# This function will send the reset email to the user
@users.route("/reset_password", methods=["GET", "POST"])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = RequestResetForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # This will get the user with the given email
        send_reset_email(user)
        flash("An email has been sent with instructions to reset your password", "info")
        # info is a bootstrap class for the blue message
        return redirect(url_for("users.login"))

    return render_template("reset_request.html", title="Reset Password", form=form)


# This function will reset the password of the user
@users.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    user = User.verify_reset_token(token)
    if user is None:
        flash("That is an invalid or expired token", "warning")
        # If the token is invalid or expired, it will flash a message and
        return redirect(url_for("users.reset_request"))
    form = ResetPasswordForm()

    # This will validate the form and reset the password
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user.password = hashed_password
        db.session.commit()
        flash("Your password has been updated! You are now able to log in!", "success")
        return redirect(url_for("users.login"))

    return render_template("reset_token.html", title="Reset Password", form=form)
