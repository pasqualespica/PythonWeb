import os
from config import db
from models import Person

# Data to initialize database with
PEOPLE = [
    {'fname': 'Doug', 'lname': 'Farrell'},
    {'fname': 'Kent', 'lname': 'Brockman'},
    {'fname': 'Bunny', 'lname': 'Easter'},
    {'fname': 'Mario', 'lname': 'Rossi'},
    {'fname': 'Pasquale', 'lname': 'Rossi'},
    {'fname': 'Luca', 'lname': 'Rossi'},
    {'fname': 'Teresa', 'lname': 'Rossi'}
]

# Delete database file if it exists currently
if os.path.exists('people.db'):
    os.remove('people.db')

# Create the database
db.create_all()

# Iterate over the PEOPLE structure and populate the database
for person in PEOPLE:
    p = Person(lname=person['lname'], fname=person['fname'])
    db.session.add(p)

db.session.commit()
