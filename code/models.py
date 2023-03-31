from flask_sqlalchemy import SQLAlchemy
from flask import Flask 
import os


path = os.path.dirname(os.path.realpath(__file__))
usersdb=os.path.join(path,'DB/users.db')
areasdb=os.path.join(path,'DB/areas.db')

app = Flask(__name__)
app.config['USERSDBPATH'] = usersdb
app.config['AREASDBPATH'] = areasdb
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + usersdb
app.config['SQLALCHEMY_BINDS'] = {
    'users': 'sqlite:///' + usersdb,
    'fitnessareas': 'sqlite:///' + areasdb,
}
db = SQLAlchemy(app)
