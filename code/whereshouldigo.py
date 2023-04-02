from flask import render_template, request, redirect, g, jsonify, url_for  , Blueprint
from flask_login import login_required
import sqlite3
from weather import getRegion, getForecast
from checkin import get_user_location, calculate_distance
from models import app

WhereShouldIGo_bp = Blueprint('WhereShouldIGo', __name__)
app.config['DATABASE'] = 'DB/areas.db'

def get_db():
    db = getattr(g, '_database', None)
    print("TEST")
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite3_db.close()

#@WhereShouldIGo_bp.route("/whereshouldigo")
@app.route('/whereshouldigo')
#@login_required
def whereshouldigo():
    items = [
        {'category': 'Nature Reserves', 'image': 'image1', 'description': 'Protected areas of importance for flora, fauna, or features of geological or other special interest.'},
        {'category': 'Parks', 'image': 'image2', 'description': 'Areas of natural, semi-natural or planted space for  enjoyment and recreation.'},
        {'category': 'Wildlife Reserves', 'image': 'image3', 'description': 'Large areas of land where wild animals live safely.' }
    ]
    return render_template("whereshouldigo.html", items=items)

@app.route('/results')
def results():
    query = request.args.get('query')
    conn = sqlite3.connect('DB/areas.db')
    c = conn.cursor()
    c.execute("SELECT * FROM areas WHERE name LIKE ?", ('%' + query + '%',))
    results = c.fetchall()
    conn.close()

     # Get user's current location
    location = get_user_location()
    
    # Calculate distance to each area in results
    for i, result in enumerate(results):
        lat, lng = result[2], result[3]
        area_location = (lat, lng)
        distance = calculate_distance(location, area_location)
        results[i] = result + (distance,)
        
        # Get weather conditions for this area
        region = getRegion(lat, lng)
        weather = getForecast(region)
        results[i] = results[i] + (weather,)

    # Sort results by distance in ascending order
    results = sorted(results, key=lambda x: x[-2])

    return render_template('results.html', query=query, results=results)

#@WhereShouldIGo_bp.route('/route1', methods=['POST'])
@app.route('/route1', methods=['POST'])
#@login_required
def route1():
    if request.method == 'POST':
        item_id = request.form['item_id']
        button_value = request.form['submit_button']
        if button_value == 'button1':
            return redirect(url_for('get_areas_by_category', category='Nature Reserves'))
        elif button_value == 'button2':
            return redirect(url_for('get_areas_by_category', category='Parks'))
        elif button_value == item_id + 'button3':
            return redirect(url_for('get_areas_by_category', category='Wildlife Reserves'))
    # Render the template with the form
    return render_template('whereshouldigo.html')

#@WhereShouldIGo_bp.route('/areas/category/<category>', methods=['GET'])
@app.route('/areas/category/<category>', methods=['GET'])
def get_areas_by_category(category):
    db = get_db()

    cursor = db.execute('SELECT * FROM areas WHERE category = ?', [category])
    results = cursor.fetchall()
    if not results:
        return jsonify({'error': 'No areas found for category: {}'.format(category)})
    user_location = get_user_location()
    
    for i in range(len(results)):
        row = results[i]
        lat = row['latitude']
        lng = row['longitude']

        # Calculate distance between user's location and area location
        area_location = (lat, lng)
        distance_km = calculate_distance(user_location, area_location)
        
        # Get weather for area
        region = getRegion(lat, lng)
        weather = getForecast(region)
        
        area_dict = dict(row)
        area_dict['distance_km'] = distance_km
        area_dict['weather'] = weather
        results[i] = area_dict

    # Sort results by distance in ascending order
    results = sorted(results, key=lambda x: x['distance_km'])
    
    return render_template('areas_by_category.html', results=results, category=category)

#@WhereShouldIGo_bp.route('/map/<int:id>')
@app.route('/map/<int:id>')
def show_map(id):
    # Connect to the database
    conn = sqlite3.connect('DB/areas.db')

    # Create a cursor object
    c = conn.cursor()

    # Execute a SELECT statement to retrieve the latitude and longitude values for the specified id
    c.execute('SELECT latitude, longitude FROM areas WHERE id=?', (id,))

    # Fetch the first row as a tuple
    row = c.fetchone()

    # Close the cursor and database connection
    c.close()
    conn.close()

    # If no row was found, return a 404 error
    if row is None:
        return 'Area not found', 404

    # Extract the latitude and longitude values from the row
    latitude, longitude = row

    # Render a template that displays the location on a map
    travel = {
        'destination': f"{latitude},{longitude}",
    }

    return render_template('directions.html', travel=travel)

if __name__ == '__main__':
    app.run()