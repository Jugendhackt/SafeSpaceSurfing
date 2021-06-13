from flask_sqlalchemy import SQLAlchemy
from .models import db, Facility
from .DB_Install import push_data_to_database
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
   push_data_to_database(app)





