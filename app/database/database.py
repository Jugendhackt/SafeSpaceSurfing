from flask_sqlalchemy import SQLAlchemy
from .models import db, Facility
import json

def init_app(app):

    #passes the app(flask object) to the sql alchemey library
    db.init_app(app)

    #Generates the Database models
    db.create_all(app=app)

    #parses data from the default_facilities file and 
    #adds the information into the database
    parse_and_pull_data(app)

def parse_and_pull_data(app):
    with app.app_context():
        jsonFile = open("database/default_facilities.json", "rt")
        json_data = json.load(jsonFile)
        for item in json_data["Facilities"]:
            facility = Facility(item)
            db.session.add(facility)
        db.session.commit()
        print(str(len(json_data['Facilities'])) + " facilities added to the database")



