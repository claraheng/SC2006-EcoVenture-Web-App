from flask_sqlalchemy import SQLAlchemy
from flask import Flask 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/zhiyonglee/Documents/GitHub/sc2006lab/code/DB/users.db'
app.config['SQLALCHEMY_BINDS'] = {
    'users': 'sqlite://///Users/zhiyonglee/Documents/GitHub/sc2006lab/code/DB/users.db',
    'fitnessareas': 'sqlite://///Users/zhiyonglee/Documents/GitHub/sc2006lab/code/DB/areas.db'
    # 'users': 'sqlite://///Users/claraheng/Library/CloudStorage/OneDrive-NanyangTechnologicalUniversity/School/_S2_AY_22_23/SC2006 SOFTWARE ENGINEERING/Group 5 Maggie/SC2006repo/sc2006lab/code/DB/users.db',
    # 'fitnessareas': 'sqlite://///Users/claraheng/Library/CloudStorage/OneDrive-NanyangTechnologicalUniversity/School/_S2_AY_22_23/SC2006 SOFTWARE ENGINEERING/Group 5 Maggie/SC2006repo/sc2006lab/code/DB/areas.db'
}
db = SQLAlchemy(app)

