from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)  # This is the database instance
bcrypt = Bcrypt(app)  # This is the encryption instance
login_manager = LoginManager(app)  # This is the login manager instance
login_manager.login_view = (
    "users.login"  # this is the function name of the route for the login page
)
login_manager.login_message_category = (
    "info"  # bootstrap class for the message (nicely coloured blue thingy)
)


mail = Mail(app)  # This is the mail instance

# environ is a dictionary that stores the environment variables of the system

from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main

# This is the blueprint for the users, posts and main routes
app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)