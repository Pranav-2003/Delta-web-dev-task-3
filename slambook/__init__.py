from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app  = Flask(__name__)
 
app.config['SECRET_KEY'] = 'f8e6c5b914302b637b9130dfa0498389'
 
 
app.config['SQLALCHEMY_DATABASE_URI'] = ' postgresql://nlndqtovnrgeke:763f97bafed23ff10e55c07a0b7bc549882fae6b473f776e9d0be1ce2985f52a@ec2-34-203-182-65.compute-1.amazonaws.com:5432/d9tp38roctgdpj'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from slambook import routes