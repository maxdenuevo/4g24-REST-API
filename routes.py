from flask import Flask, jsonify, request
from models import db, User, People, Planet, Favorite

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

@app.route('/people', methods=['GET'])
def get_people():
    people = People.query.all()
    return jsonify([{'id': p.id, 'name': p.name} for p in people])

@app.route('/people/<int:people_id>', methods=['GET'])
def get_person(people_id):
    person = People.query.get_or_404(people_id)
    return jsonify({
        'id': person.id,
        'name': person.name,
        'birth_year': person.birth_year,
        'eye_color': person.eye_color,
        'gender': person.gender,
        'hair_color': person.hair_color,
        'height': person.height,
        'mass': person.mass,
        'skin_color': person.skin_color
    })

@app.route('/people', methods=['POST'])
def create_person():
    data = request.get_json()
    
    if 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400
        
    new_person = People(
        name=data['name'],
        birth_year=data.get('birth_year'),
        eye_color=data.get('eye_color'),
        gender=data.get('gender'),
        hair_color=data.get('hair_color'),
        height=data.get('height'),
        mass=data.get('mass'),
        skin_color=data.get('skin_color')
    )
    
    db.session.add(new_person)
    db.session.commit()
    
    return jsonify({
        'id': new_person.id,
        'name': new_person.name,
        'message': 'Person created successfully'
    }), 201

@app.route('/people/<int:people_id>', methods=['PUT'])
def update_person(people_id):
    person = People.query.get_or_404(people_id)
    data = request.get_json()
    
    if 'name' in data:
        person.name = data['name']
    if 'birth_year' in data:
        person.birth_year = data['birth_year']
    if 'eye_color' in data:
        person.eye_color = data['eye_color']
    if 'gender' in data:
        person.gender = data['gender']
    if 'hair_color' in data:
        person.hair_color = data['hair_color']
    if 'height' in data:
        person.height = data['height']
    if 'mass' in data:
        person.mass = data['mass']
    if 'skin_color' in data:
        person.skin_color = data['skin_color']
    
    db.session.commit()
    
    return jsonify({
        'id': person.id,
        'name': person.name,
        'message': 'Person updated successfully'
    })

@app.route('/people/<int:people_id>', methods=['DELETE'])
def delete_person(people_id):
    person = People.query.get_or_404(people_id)
    db.session.delete(person)
    db.session.commit()
    
    return jsonify({
        'message': 'Person deleted successfully'
    }), 200

@app.route('/planets', methods=['GET'])
def get_planets():
    planets = Planet.query.all()
    return jsonify([{'id': p.id, 'name': p.name} for p in planets])

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planet.query.get_or_404(planet_id)
    return jsonify({
        'id': planet.id,
        'name': planet.name,
        'climate': planet.climate,
        'gravity': planet.gravity,
        'rotation_period': planet.rotation_period,
        'population': planet.population,
        'terrain': planet.terrain
    })

@app.route('/planets', methods=['POST'])
def create_planet():
    data = request.get_json()
    
    if 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400
        
    new_planet = Planet(
        name=data['name'],
        climate=data.get('climate'),
        gravity=data.get('gravity'),
        rotation_period=data.get('rotation_period'),
        population=data.get('population'),
        terrain=data.get('terrain')
    )
    
    db.session.add(new_planet)
    db.session.commit()
    
    return jsonify({
        'id': new_planet.id,
        'name': new_planet.name,
        'message': 'Planet created successfully'
    }), 201

@app.route('/planets/<int:planet_id>', methods=['PUT'])
def update_planet(planet_id):
    planet = Planet.query.get_or_404(planet_id)
    data = request.get_json()
    
    if 'name' in data:
        planet.name = data['name']
    if 'climate' in data:
        planet.climate = data['climate']
    if 'gravity' in data:
        planet.gravity = data['gravity']
    if 'rotation_period' in data:
        planet.rotation_period = data['rotation_period']
    if 'population' in data:
        planet.population = data['population']
    if 'terrain' in data:
        planet.terrain = data['terrain']
    
    db.session.commit()
    
    return jsonify({
        'id': planet.id,
        'name': planet.name,
        'message': 'Planet updated successfully'
    })

@app.route('/planets/<int:planet_id>', methods=['DELETE'])
def delete_planet(planet_id):
    planet = Planet.query.get_or_404(planet_id)
    db.session.delete(planet)
    db.session.commit()
    
    return jsonify({
        'message': 'Planet deleted successfully'
    }), 200

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': u.id, 'username': u.username, 'email': u.email} for u in users])

@app.route('/users/favorites', methods=['GET'])
def get_user_favorites():
    user_id = request.args.get('user_id')
    favorites = Favorite.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'planet_id': f.planet_id,
        'people_id': f.people_id
    } for f in favorites])

@app.route('/favorite/<string:item_type>/<int:item_id>', methods=['POST'])
def add_favorite(item_type, item_id):
    user_id = request.json.get('user_id')
    if not user_id:
        return jsonify({'message': 'user_id is required'}), 400

    new_favorite = Favorite(user_id=user_id)
    if item_type == 'planet':
        new_favorite.planet_id = item_id
    elif item_type == 'people':
        new_favorite.people_id = item_id
    else:
        return jsonify({'message': 'Invalid favorite type'}), 400

    db.session.add(new_favorite)
    db.session.commit()
    return jsonify({'message': 'Favorite added successfully'}), 201

@app.route('/favorite/<string:item_type>/<int:item_id>', methods=['DELETE'])
def remove_favorite(item_type, item_id):
    user_id = request.json.get('user_id')
    if not user_id:
        return jsonify({'message': 'user_id is required'}), 400

    favorite = Favorite.query.filter_by(user_id=user_id).filter(
        (Favorite.planet_id == item_id) if item_type == 'planet' else (Favorite.people_id == item_id)
    ).first()

    if favorite:
        db.session.delete(favorite)
        db.session.commit()
        return jsonify({'message': 'Favorite removed successfully'}), 204

    return jsonify({'message': 'Favorite not found'}), 404

if __name__ == '__main__':
    app.run()