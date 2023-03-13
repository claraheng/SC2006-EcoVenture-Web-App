#extension file 
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
login_manager=LoginManager() 

def init_app(app):
    db.init_app(app)
    login_manager.init_app(app)

