from datetime import datetime
from email.policy import default
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from slambook import db, login_manager, app
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    department = db.Column(db.String(7), nullable=False)
    batch = db.Column(db.String(4), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    comments = db.relationship('Comment', backref='author', lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
    
    
class Comment(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    username = db.Column(db.String(20), nullable=False)
    about = db.Column(db.String(100), nullable=False)
    nickname = db.Column(db.String(30))
    moment = db.Column(db.String(50))
    receiver_id = db.Column(db.Integer, nullable=False)
    
