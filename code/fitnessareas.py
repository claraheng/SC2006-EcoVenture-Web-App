from models import db, app
from flask import Blueprint, jsonify

areas_bp = Blueprint('fitnessareas', __name__)


class Area(db.Model):
    __bind_key__="fitnessareas"
    __tablename__='areas'
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
    
    @areas_bp.route('/api/areas')
    def loadareas():
        areas_list = Area.query.all()
        areas_dict = [
            {
                'name': area.name,
                'latitude': area.latitude,
                'longitude': area.longitude,
                'points': area.points,
                'category': area.category,
                'description': area.description
            }
            for area in areas_list
        ]
        return jsonify(areas_dict)   
        