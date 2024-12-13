from flaskblog import db, login_manager
from datetime import datetime
from flask_login import UserMixin

# The user_loader decorator allows for the Flask-Login extension to load a user by their ID. The user_loader callback is used to reload the user object from the user ID stored in the session.
# It is j=just something that has to be done, specified in the documentation also.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship(
        "Post", backref="author", lazy=True
    )  # This establishes a one-to-many relationship between the User and Post classes.
    # lazy argument defines when SQLAlchemy will load the data from the database. True means that SQLAlchemy will load the data as necessary in one go using a standard select statement. lazy=true means it will load the data in one go as necessary.

    # The __repr__ method returns a string representation of an object that should ideally be detailed enough for a developer to recreate the object.
    # It's meant to be more detailed and "official" compared to __str__, which is meant for readable, user-friendly output.
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
