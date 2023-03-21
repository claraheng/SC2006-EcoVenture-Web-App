#classfile for fitness areas
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///areas.db'
db = SQLAlchemy(app)

class Area(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    latitude = db.Column(db.Float(), nullable=False)
    longitude = db.Column(db.Float(), nullable=False)
    points = db.Column(db.Integer(), nullable=False)
    category = db.Column(db.String(length=30), nullable=False)
    description = db.Column(db.String(length=1024), nullable=False)

    def __init__(self, name: str, latitude: float, longitude: float, points: int, category: str, description: str):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.points = points
        self.category = category
        self.description = description

    def __repr__(self):
        return f'Area {self.name}'