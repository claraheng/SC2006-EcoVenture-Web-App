from flask import render_template, request, redirect, g, jsonify, url_for  , Blueprint
from flask_login import login_required
import sqlite3
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

@WhereShouldIGo_bp.route("/whereshouldigo")
@login_required
def whereshouldigo():
    items = [
        {'category': 'Nature Reserves', 'image': 'image1', 'description': 'protected areas of importance for flora, fauna, or features of geological or other special interest'},
        {'category': 'Parks', 'image': 'image2', 'description': 'areas of natural, semi-natural or planted space for  enjoyment and recreation'},
        {'category': 'Wildlife Reserves', 'image': 'image3', 'description': 'large areas of land where wild animals live safely' }
    ]
    return render_template("whereshouldigo.html", items=items)

@WhereShouldIGo_bp.route('/route1', methods=['POST'])
#@login_required
def route1():
    if request.method == 'POST':
        item_id = request.form['item_id']
        button_value = request.form['submit_button']
        if button_value == 'button1':
            return redirect(url_for('WhereShouldIGo.get_areas_by_category', category='Nature Reserve'))
        elif button_value == 'button2':
            return redirect(url_for('WhereShouldIGo.get_areas_by_category', category='Park'))
        elif button_value == item_id + 'button3':
            return redirect(url_for('WhereShouldIGo.get_areas_by_category', category='Wildlife Reserve'))
    # Render the template with the form
    return render_template('whereshouldigo.html')

@WhereShouldIGo_bp.route('/areas/category/<category>', methods=['GET'])
def get_areas_by_category(category):
    db = get_db()

    cursor = db.execute('SELECT * FROM areas WHERE category = ?', [category])
    results = cursor.fetchall()
    if not results:
        return jsonify({'error': 'No areas found for category: {}'.format(category)})
    return render_template('areas_by_category.html', results=results)

@WhereShouldIGo_bp.route('/map/<int:id>')
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
    return render_template('map.html', latitude=latitude, longitude=longitude)

