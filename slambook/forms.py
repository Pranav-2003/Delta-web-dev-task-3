from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from slambook.models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    roll_number = StringField('Roll Number', validators=[DataRequired(), Length(min=9, max=9)])
    department = SelectField('Department', choices=['CSE','CIV','MECH','PROD','MME','ECE','EEE','ICE'])
    batch = StringField('Batch', validators=[DataRequired(), Length(min=4, max=4)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_roll_number(self, roll_number):
        user = User.query.filter_by(id=int(roll_number.data)).first()
        if user:
            raise ValidationError('That roll number is taken. User already exists!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please enter a different one!')

class Searchform(FlaskForm):
    searched = StringField("Searched", validators=[DataRequired()])
    submit = SubmitField("Search")
    
class Updateform(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    roll_number = StringField('Roll Number', validators=[DataRequired(), Length(min=9, max=9)])
    submit = SubmitField('Update')
    
class Commentform(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired(), Length(min=2, max=20)])
    about = TextAreaField('Thoughts about your friendship...', validators=[DataRequired()])
    nickname = StringField('Nickname', validators=[DataRequired()])
    moment = StringField('Best Moments', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
    
    