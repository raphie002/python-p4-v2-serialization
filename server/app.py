# server/app.py
#!/usr/bin/env python3
from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Welcome to the pet directory!'}
    return make_response(body, 200)


if __name__ == '__main__':
    app.run(port=5555, debug=True)


@app.route('/pets/<int:id>')
def pet_by_id(id):
    pet = Pet.query.filter(Pet.id == id).first()

    if pet:
        return make_response(pet.to_dict(), 200)
    else:
        return make_response({'message': f'Pet {id} not found.'}, 404)


@app.route('/species/<string:species>')
def pet_by_species(species):
    pets_query = Pet.query.filter_by(species=species).all()
    
    pets_data = [pet.to_dict() for pet in pets_query]
    
    body = {
        'count': len(pets_data),
        'pets': pets_data
    }
    return make_response(body, 200)