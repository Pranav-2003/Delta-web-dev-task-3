from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app  = Flask(__name__)
 
app.config['SECRET_KEY'] = 'f8e6c5b914302b637b9130dfa0498389'
 
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tsdtsupldfsjnu:d34cbf1f65d43a61f8f866b147c76c79eedb452466c5bf801da07b4dbed14771@ec2-3-208-79-113.compute-1.amazonaws.com:5432/dahhrchllm58nl'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from slambook import routes