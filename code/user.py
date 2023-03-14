from werkzeug.security import check_password_hash
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id, username, password, totalPoints):
        self.id = id
        self.username = username
        self.password = password
        self.points= totalPoints  

    def __repr__(self):
        return f'<User: {self.username}>'
    
    def is_active(self):
        return True
    
    def find_by_username(user_id):
            # This is just an example implementation, you will need to replace this
            # with your own logic to retrieve a user from a database or some other storage
            # based on the given username.
            #print("checking findbyusername=",username)

            for user in users:
                if user.username == user_id:
                    print("Pass user check")
                    return user
            return None
        
    def findByID(user_id):
        for user in users:
            print("findbyID user=",user.id,"id=",user_id)
            if int(user.id) == int(user_id):
                print("pass id check")
                return user
        return None
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
    
    @staticmethod
    def get(user_id):
        users = User.get_all()
        for user in users:
            if user.id == user_id:
                return user
        return None

    @staticmethod
    def get_all():
        return users
        
users = [
            User(1, 'john', 'password',0),
            User(2, 'jane', 'password',0),
            User(3, 'bob', 'password',0),
        ]
