import os

class Config:
    SECRET_KEY = (
        "5791628bb0b13ce0c676dfde280ba245"  # This is the secret key for the app
    )
    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///site.db"  # This is the path to the database
    )
    MAIL_SERVER = (
        "smtp.googlemail.com"  # smtp is a protocol for sending emails
    )
    MAIL_PORT = 587  # port for the email server
    MAIL_USE_TLS = True  # Transport Layer Security
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")  # email address
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")  # email password
    # https://myaccount.google.com/apppasswords

