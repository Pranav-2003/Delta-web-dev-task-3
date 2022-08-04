from datetime import datetime
from imp import reload
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from slambook import app, db, bcrypt
from slambook.models import User, Comment
from slambook.forms import LoginForm, RegistrationForm, Searchform, Updateform, Commentform
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password')
    return render_template('login.html', form=form)

@app.route("/home", methods=['GET', 'POST'])
@login_required
def home():
    form = Searchform()
    comments = Comment.query.filter_by(receiver_id=current_user.id).order_by(Comment.sno.desc())
    if form.validate_on_submit():
        users = User.query.filter(User.username.like('%' + form.searched.data + '%'))
        return render_template('search.html', users=users)
    return render_template('home.html', form=form, comments=comments)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(id= int(form.roll_number.data), username=form.username.data, email=form.email.data, department=form.department.data, batch=form.batch.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = Updateform()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.id = form.roll_number.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.roll_number.data = current_user.id
    return render_template('account.html', form=form)

@app.route("/comment/<int:rno>", methods=['GET', 'POST'])
@login_required
def comment(rno):
    form = Commentform()
    c=1
    receiver = User.query.filter_by(id=rno).first()
    t = Comment.query.filter_by(author_id=current_user.id, receiver_id=rno).first()
    if t:
        c=0
    if form.validate_on_submit():
        comment = Comment(author_id=current_user.id, username=form.name.data, about=form.about.data, nickname=form.nickname.data, moment=form.moment.data, receiver_id=rno)
        db.session.add(comment)
        db.session.commit()
        flash('Your comments have been sent successfully!')
        return redirect(url_for('home'))
    return render_template('comment.html', form=form, name=receiver.username, t=t, c=c)
    
@app.route("/view/<int:id>", methods=['GET', 'POST'])
@login_required
def view(id):
    comment = Comment.query.filter_by(receiver_id=current_user.id, author_id=id).first()
    return render_template('view.html', comment=comment)

@app.route("/delete/<int:rno>")
def delete(rno):
    comment = Comment.query.filter_by(author_id=current_user.id, receiver_id=rno).first()
    db.session.delete(comment)
    db.session.commit()
    flash('Your comment has been deleted')
    return redirect(url_for('home'))
    
            