from flask import Flask, render_template, request, redirect, session, url_for,flash 
from flask_login import LoginManager, login_required, current_user
from user import User
from auth import auth_bp, login_manager
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.register_blueprint(auth_bp)
#login_manager = LoginManager()
login_manager.init_app(app)



@login_manager.unauthorized_handler
def unauthorized_callback():
    flash("You must be logged in to view that page.")
    return redirect(url_for('auth.login'))

'''@login_manager.user_loader
def load_user(user_id):
    print(User.find_by_username(user_id))
    return User.find_by_username(user_id)'''

@app.route("/") #home page before login 
def home():
    return render_template("home.html")


@app.route("/checkin")#get current location and display on map 
@login_required
def checkin():
    print(session)
    return render_template("checkin.html")



@app.route("/user") #userpage
def user():
    # get the username from the session
    username = session.get('username')
    #print(session.get('username')) 
    # if the user is not logged in, redirect to the login page
    if not username:
        return redirect(url_for('login'))
    return render_template('user.html', username=username)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    return render_template('home.html')

# General error handler for all status codes
@app.errorhandler(Exception)
def handle_error(e):
    return render_template('error.html', error=str(e)), getattr(e, 'code', 500)

if __name__ == '__main__':
    app.run(host='0.0.0.0')


app.run()
#test commit