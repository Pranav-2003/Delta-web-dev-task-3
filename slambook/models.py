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
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    comments = db.relationship('Comment', backref='author', lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
    
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
