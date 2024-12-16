# imports

from flask_login import login_user, current_user, logout_user, login_required
import os, secrets
from PIL import Image
from flaskblog.models import User, Post
from flask import render_template, url_for, flash, redirect, request
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flaskblog import app, db, bcrypt


posts = [
    {
        "author": "Granth Agarwal",
        "title": "Blog Post 1",
        "content": """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed odio lorem, ornare nec iaculis non, maximus eget augue. Phasellus elementum ultrices justo ut aliquet. Ut consequat tortor ac commodo porttitor. Aenean facilisis enim nibh, nec commodo risus interdum porta. Suspendisse diam urna, lobortis id ligula tristique, semper varius lacus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Proin vel diam risus. Vestibulum a quam eget mi vestibulum malesuada. Curabitur varius in enim eu varius. Integer vestibulum augue at enim efficitur auctor. Etiam non leo at nunc mattis consequat. """,
        "date_posted": "October 23rd, 2024",
    },
    {
        "author": "Ayush Jain",
        "title": "Blog Post 2",
        "content": """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed odio lorem, ornare nec iaculis non, maximus eget augue. Phasellus elementum ultrices justo ut aliquet. Ut consequat tortor ac commodo porttitor. Aenean facilisis enim nibh, nec commodo risus interdum porta. Suspendisse diam urna, lobortis id ligula tristique, semper varius lacus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Proin vel diam risus. Vestibulum a quam eget mi vestibulum malesuada. Curabitur varius in enim eu varius. Integer vestibulum augue at enim efficitur auctor. Etiam non leo at nunc mattis consequat. """,
        "date_posted": "October 24th, 2024",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
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
        return redirect(url_for("login"))

    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check email and password", "danger")
    return render_template("login.html", title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext     # This will save the picture with a random name
    picture_path = os.path.join(app.root_path, "static/profile_pics", picture_fn)

    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)

    return picture_fn

@app.route("/account")
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
        return redirect(url_for("account"))

    # This will fill the current data with username and email in the form for the current user
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email

    image_file = url_for("static", filename="profile_pics/" + current_user.image_file)
    return render_template("account.html", title="Account", image_file=image_file, form=form)

