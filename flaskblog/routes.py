from flask_login import login_user, current_user, logout_user, login_required
from flaskblog.models import User, Post
from flask import render_template, url_for, flash, redirect, request
from flaskblog.forms import RegistrationForm, LoginForm
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
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
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

@app.route("/account")
@login_required
def account():
    return render_template("account.html", title="Account")