from flask import Flask,Blueprint, render_template, request, redirect, url_for, flash,session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from user import User


auth_bp = Blueprint('auth', __name__)
login_manager = LoginManager()
login_manager.login_view = 'login'



#def load_user(user_id):
#    return User.get(user_id)

@login_manager.user_loader
def load_user(user_id):
    #print("check user id = ",user_id)
    id = User.findByID(user_id)
    print("check load user id = ",id)
    return id

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.find_by_username(username)
        print("login check user",user)

        if user and (password == user.password):
            session['username'] = user.username
            login_user(user)
            return redirect(url_for('user', username=user.username))
        else:
            error = 'Invalid username or password. Please try again.'
            return render_template('login.html', error=error)
    
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
