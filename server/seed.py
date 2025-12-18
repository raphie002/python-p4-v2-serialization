# !/usr/bin/env python3
# server/seed.py
from random import choice as rc
from faker import Faker # type: ignore

from app import app
from models import db, Pet

with app.app_context():

    fake = Faker()

    Pet.query.delete()

    pets = []

    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

    for n in range(10):
        pet = Pet(name=fake.first_name(), species=rc(species))
        pets.append(pet)

    db.session.add_all(pets)

    db.session.commit()