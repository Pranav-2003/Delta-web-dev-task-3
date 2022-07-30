from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app  = Flask(__name__)
 
app.config['SECRET_KEY'] = 'hardsecretkey'
 
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flask_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False