from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app  = Flask(__name__)
 
app.config['SECRET_KEY'] = 'f8e6c5b914302b637b9130dfa0498389'
 
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fzuxyucaqzxqhx:a461bd0673c24485cc0c21ed5b5374eb45ede018a39722657968e3f8f9c838b7@ec2-44-209-186-51.compute-1.amazonaws.com:5432/ddfaktscvpnce5'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from slambook import routes