from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3 
from flask_login import UserMixin
from models import db, User



'''class User(UserMixin):


    def __repr__(self):
        return f'<User: {self.username}>'
    


    
    query=db.session.query_property()'''

    

    
def find_by_username(username):
            user = User.query.filter_by(username=username).first()
            return user
            # This is just an example implementation, you will need to replace this
            # with your own logic to retrieve a user from a database or some other storage
            # based on the given username.
            #print("checking findbyusername=",username)
            '''connection = sqlite3.connect('DB/users.db')
            cursor=connection.cursor()
            cursor.execute('SELECT * FROM users WHERE username=?',(username,))
            user_data=cursor.fetchone()
            connection.close()
            
            if not user_data:
                return None 
            return User(user_data[0],user_data[1],user_data[2])'''

        

    
def createAccount(username, password, points):
    #if db.session.query(User).filter_by(username=username).first():
    if User.query.filter_by(username=username).first():
        raise ValueError('Username already exists')
    
    password_hash = generate_password_hash(password)
    user = User(username=username, password_hash=password_hash, points=points)
    db.session.add(user)
    db.session.commit()

    