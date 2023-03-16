'''from models import db, User
from werkzeug.security import generate_password_hash

def createAccount(username, password,points):
    if User.query.filter_by(username=username).first():
        raise ValueError('Username already exists')
    
    password_hash = generate_password_hash(password)
    user = User(username=username, password_hash=password_hash, points=points)
    db.session.add(user)
    db.session.commit()'''
