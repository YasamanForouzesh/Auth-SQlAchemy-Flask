from flask import Blueprint,render_template, redirect, url_for,request, flash
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import *
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(email=email).first()
    # print(password)
    # print(user.password)
    # print(check_password_hash(user.password, password))
    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    # if user:
    #     print("Hello")
    #     return "hello user is in"
    if user:
        print("user in")
        if check_password_hash(user.password, password):
            print("correct")
            login_user(user, remember=remember)
            return redirect(url_for('main.profile'))
            # return "Welcome to your page"
        else:
            print("incorrect")
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page
    else:
        print("incorrect")
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page
    
@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    passi =generate_password_hash(password, method='sha256')
    print(passi)
    new_user = User(email=email, name=name, password=passi)
    user = User.query.filter_by(email=email).first()
    
    # print(user.password)
    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    print(user)
    # code to validate and add user to database goes here
    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
