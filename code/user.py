from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3 
from flask_login import UserMixin



class User(UserMixin):
    def __init__(self,username, password, points):
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.points= points  

    def __repr__(self):
        return f'<User: {self.username}>'
    
    def is_active(self):
        return True
    
    def check_password(self,password):
        return check_password_hash(self.password_hash, password)
    
    
    
    def find_by_username(username):
            # This is just an example implementation, you will need to replace this
            # with your own logic to retrieve a user from a database or some other storage
            # based on the given username.
            #print("checking findbyusername=",username)
            connection = sqlite3.connect('DB/users.db')
            cursor=connection.cursor()
            cursor.execute('SELECT * FROM users WHERE username=?',(username,))
            user_data=cursor.fetchone()
            connection.close()
            
            if not user_data:
                return None 
            return User(user_data[0],user_data[1],user_data[2])
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.username)
    