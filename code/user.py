from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.security import check_password_hash
from models import db




class User(db.Model):
    __bind_key__="users"
    __tablename__='users'
    username = db.Column(db.String(80), primary_key=True, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    points = db.Column(db.Integer, default=0)
    
    def __init__(self,username, email, password_hash, points):
        self.username = username
        self.email = email
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
 
    
def createAccount(username, email, password, points):
    if User.query.filter_by(username=username).first():
        raise ValueError('Username already exists')
    if User.query.filter_by(email=email).first():
        raise ValueError('Email already exists')
    
    password_hash = generate_password_hash(password)
    user = User(username=username, email=email, password_hash=password_hash, points=points)
    db.session.add(user)
    db.session.commit()
    
def check_username(username):
    if len(username) > 50:
        print(len(username))
        return False 
    return True 

def check_email(email): 
    if len(email) < 7 or len(email) > 50:
        return False 
    if "@" not in email:
        return False
    domain = email.split("@")[1]
    if "." not in domain or (domain.split(".")[1] not in ["com", "sg"]):
        return False 
    return True


 
    