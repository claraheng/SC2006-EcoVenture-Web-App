from flask import Flask, render_template, request, redirect, session, url_for 
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

#static definition of users for testing purposes 
users = {
    'user1': 'password1',
    'user2': 'password2'
}


@app.route("/") #default page
def login():
    return render_template("login.html") 


@app.route("/checkin") #get current location and display on map 
def index():
    return render_template("checkin.html")

@app.route("/home") #home page before login 
def home():
    return render_template("home.html")

@app.route("/user") #userpage
def user():
    # get the username from the session
    username = session.get('username')
    # if the user is not logged in, redirect to the login page
    if not username:
        return redirect(url_for('login'))
    return render_template('user.html', username=username)


@app.route('/login', methods=['POST']) #can only access this route via POST request 
def authenticate():
    # check if the username and password are correct
    if request.form['username'] in users and request.form['password'] == users[request.form['username']]:
        # store the username in the session
        session['username'] = request.form['username']
        return redirect(url_for('user'))
    else:
        # if the username or password is incorrect, show an error message
        return render_template('login.html', error='Invalid username or password')
    
# General error handler for all status codes
@app.errorhandler(Exception)
def handle_error(e):
    return render_template('error.html', error=str(e)), getattr(e, 'code', 500)

if __name__ == "__main__":
   port = int(os.environ.get("PORT", 5000))
   app.run(host="0.0.0.0", port=port)


app.run()
#test commit