from flask import Flask,Blueprint, render_template, request, redirect, url_for, flash,session
from flask_login import LoginManager, login_user, logout_user, login_required
from user import User, sqlite3



auth_bp = Blueprint('auth', __name__)
login_manager = LoginManager()
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(username):
        connection=sqlite3.connect('DB/users.db')
        cursor=connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username=?',(username,))
        user_data=cursor.fetchone()
        connection.close()
        
        if not user_data:
            return None
        
        return User(user_data[0],user_data[1],user_data[2])

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.find_by_username(username)

        if user and (User.check_password(user,password)):
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

