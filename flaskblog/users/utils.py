import os, secrets
from PIL import Image
from flask import url_for
from flask_mail import Message
from flaskblog import app, mail


# This function will save the picture in the profile_pics folder
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext  # This will save the picture with a random name
    picture_path = os.path.join(app.root_path, "static/profile_pics", picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)

    return picture_fn


# This function will send the reset email to the user
def send_reset_email(user):
    token = user.get_reset_token()
    # This will get the token for the user
    msg = Message(
        "Password Reset Request", sender="noreply@demo.com", recipients=[user.email]
    )
    msg.body = f"""To reset your password, visit the following link:
{ url_for("users.reset_token", token=token, _external=True) }

If you did not make this request then simply ignore this email and no changes will be made.
"""
    mail.send(msg)
