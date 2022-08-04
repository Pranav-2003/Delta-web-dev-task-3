from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app  = Flask(__name__)
 
app.config['SECRET_KEY'] = 'f8e6c5b914302b637b9130dfa0498389'
 
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://qurugnbrvjnnvx:bca1f1255d29dd433d3534b69bec322a27389f19722a21d93f81161773e2adcf@ec2-107-22-122-106.compute-1.amazonaws.com:5432/ddfg2o90610lq7'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from slambook import routes