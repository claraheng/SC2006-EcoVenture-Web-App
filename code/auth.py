from flask import Flask,Blueprint, render_template, request, redirect, url_for, flash,session
from flask_login import LoginManager, login_user, logout_user, login_required
from user import User, find_by_username
import sqlite3
from flask_cors import CORS # frontend
from flask import jsonify # frontend
from models import app
from models import db

# frontend
CORS(app)

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
        user = find_by_username(username)
        if user and user.check_password(password):
            session['username'] = user.username
            login_user(user)
            return redirect(url_for('user', username=user.username))
            # return jsonify({'message':'Logged in successfully'})
        else:
            error = 'Invalid username or password. Please try again.'
            return render_template('login.html', error=error)
            # return jsonify({'message': 'Invalid username or password'}), 401
    return render_template('login.html')
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

