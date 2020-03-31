import os


# TO DO: CONVERT INTO ENVIRONMENT VARIABLES (nano .bash_profile >> os.environ.get)
class Config:
    # HASH
    SECRET_KEY = '0a86b4b6d6d9e48e6b34a9a3cbe90a83'
    # CREATING DATABASE >> SQLLITE
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'
    # MAIL CLIENT (using Google)
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'thelonelytraveller.blog@gmail.com'
    MAIL_PASSWORD = '!Ktv0134597'

# EXAMPLE
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('EMAIL_USER')
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
