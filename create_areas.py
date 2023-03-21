#create areas for fitnessarea 
from flask import Flask, g, request, jsonify
import sqlite3

app = Flask(__name__)

def connect_db():
    sql = sqlite3.connect('./areas.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, "sqlite3"):
        g.sqlite3_db = connect_db()
    return g.sqlite3_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite3_db.close()

@app.route('/')
def index():
    return '<h1>Hello, testing area database!</h1>'

@app.route('/areas')
def viewareas():
    db = get_db()
    cursor = db.execute('SELECT id, name, latitude, longitude, points, category, description FROM areas')
    results = cursor.fetchall()
    rows = ''
    for row in results:
        rows += f"<h1>The ID is {row[0]}. <br> The Name is {row[1]}. <br> The Latitude is {row[2]}. <br> The Longitude is {row[3]}. <br> The Points is {row[4]}. <br> The Category is {row[5]}. <br> The Description is {row[6]}. </h1> "
    return rows

#CREATE
@app.route('/areas', methods=['POST'])
def create_area():
    db = get_db()
    name = request.json['name']
    latitude = request.json['latitude']
    longitude = request.json['longitude']
    points = request.json['points']
    category = request.json['category']
    description = request.json['description']
    db.execute('INSERT INTO areas (name, latitude, longitude, points, category, description) VALUES (?, ?, ?, ?, ?, ?)', [name, latitude, longitude, points, category, description])
    db.commit()
    return jsonify({'message': 'Area created successfully!'})

#READ
@app.route('/areas/<int:area_id>', methods=['GET'])
def get_area(area_id):
    db = get_db()
    cursor = db.execute('SELECT * FROM areas WHERE id = ?', [area_id])
    result = cursor.fetchone()
    if not result:
        return jsonify({'error': 'Area not found'})
    return f"<h1>The Id is {result['id']}. <br> The Name is {result['name']}. <br> The Latitude is {result['latitude']}. <br> The Longitude is {result['longitude']}. <br> The Points is {result['points']}. <br> The Category is {result['category']}. <br> The Description is {result['description']}. </h1>"
    #return jsonify({'id': result['id'], 'name': result['name'], 'age': result['age']})

#UPDATE
@app.route('/areas/<int:area_id>', methods=['PUT'])
def update_area(area_id):
    db = get_db()
    name = request.json['name']
    latitude = request.json['latitude']
    longitude = request.json['longitude']
    points = request.json['points']
    category = request.json['category']
    description = request.json['description']
    db.execute('UPDATE areas SET name = ?, latitude = ?, longitude = ?, points = ?, category = ?, description = ? WHERE id = ?', [name, latitude, longitude, points, category, description, area_id])
    db.commit()
    return jsonify({'message': 'Area updated successfully!'})


#DELETE
@app.route('/areas/<int:area_id>', methods=['DELETE'])
def delete_area(area_id):
    db = get_db()
    db.execute('DELETE FROM areas WHERE id = ?', [area_id])
    db.commit()
    return jsonify({'message': 'Area deleted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)

