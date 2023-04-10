from models import db, app
from fitnessareas import Area
from user import User
import requests,math
from flask import session, Blueprint,render_template
from flask_login import login_required
import json


checkin_bp = Blueprint('checkin', __name__)


@checkin_bp.route('/showPoints')
@login_required
def showPoints():
    username = session.get('username')
    user = User.query.filter_by(username=username).first()
    return render_template("myPoints.html",user = user)



@checkin_bp.route('/check_in', methods=['GET'])
@login_required
def check_in():
    username = session.get('username')
    user = User.query.filter_by(username=username).first()
    if not user:
        raise ValueError('User not found')
    
    # Get user's current location using a location services API
    location = get_user_location()  # This function should use a location services API to get the user's current location
    
    # Find the fitness area closest to the user's current location
    closest_area = get_closest_fitness_area(location)
    
    # Check if the user is within the proximity of the closest fitness area
    if is_user_within_proximity(location, closest_area):
        user.points += closest_area.points
        db.session.commit()
        #return f'Checked in at {closest_area.name}, {user.username} now has {user.points} points.'
        return render_template("checkin.html",user = user, closest_area = closest_area  )
    else:
        error = "You are not within the proximity of any fitness area"
        return render_template("user.html", error = error )
        
def get_user_location():
    # This function should use a location services API to get the user's current location
    # and return a tuple of (latitude, longitude) values
    '''response = requests.get("https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCHFCLcZvBCRrkFPKDLtMUq_ijnTQ1aRXE")
    location_data = response.json()'''
    url = "https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCHFCLcZvBCRrkFPKDLtMUq_ijnTQ1aRXE"
    headers = {'content-type': 'application/json'}
    data = {}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    location_data = json.loads(response.content.decode('utf-8'))

    latitude = location_data["location"]["lat"]
    longitude = location_data["location"]['lng']
    return (latitude, longitude)

def get_closest_fitness_area(location):
    # Find the fitness area closest to the user's current location
    areas = Area.query.all()
    closest_area = None
    min_distance = float('inf')

    for area in areas:
        distance = calculate_distance(location, (area.latitude, area.longitude))
        if distance < min_distance:
            min_distance = distance
            closest_area = area
    return closest_area

def is_user_within_proximity(user_location, area):
    # Check if the user is within the proximity of the closest fitness area
    distance = calculate_distance(user_location, (area.latitude, area.longitude))
    if distance <= 0.1:
        return True
    else:
        return False

def calculate_distance(location1, location2):
    # Calculate the distance between two locations using the haversine formula
    lat1, lon1 = location1
    lat2, lon2 = location2
    R = 6371  # Earth radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    return distance
