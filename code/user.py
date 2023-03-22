from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.security import check_password_hash
from models import db, app


#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/zhiyonglee/Documents/GitHub/sc2006lab/code/DB/users.db'
#db.init_app(app)

class User(db.Model):
    __bind_key__="users"
    __tablename__='users'
    username = db.Column(db.String(80), primary_key=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    points = db.Column(db.Integer, default=0)
    
    def __init__(self,username, password_hash, points):
        self.username = username
        self.password_hash = password_hash
        self.points= points  

    def __repr__(self):
        return f'<User: {self.username}>'
    def check_password(self,password):
        return check_password_hash(self.password_hash, password)
    def is_active(self):
        return True
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.username)

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

    