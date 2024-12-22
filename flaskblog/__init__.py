from flask import Flask
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin
from flask_mail import Mail

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = (
    "5791628bb0b13ce0c676dfde280ba245"  # This is the secret key for the app
)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///site.db"  # This is the path to the database
)
db = SQLAlchemy(app)  # This is the database instance
bcrypt = Bcrypt(app)  # This is the encryption instance
login_manager = LoginManager(app)  # This is the login manager instance
login_manager.login_view = (
    "login"  # this is the function name of the route for the login page
)
login_manager.login_message_category = (
    "info"  # bootstrap class for the message (nicely coloured blue thingy)
)
app.config["MAIL_SERVER"] = (
    "smtp.googlemail.com"  # smtp is a protocol for sending emails
)
app.config["MAIL_PORT"] = 587  # port for the email server
app.config["MAIL_USE_TLS"] = True  # Transport Layer Security
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")  # email address
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")  # email password
# https://myaccount.google.com/apppasswords

mail = Mail(app)  # This is the mail instance

# environ is a dictionary that stores the environment variables of the system

from flaskblog import routes
