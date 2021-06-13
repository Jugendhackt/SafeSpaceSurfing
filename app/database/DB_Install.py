import json
from .models import db, Facility


global db_install
db_install = False

def parse_data():
    jsonFile = open("database/new_dataset.json", "rt")
    json_data = json.load(jsonFile)
    return json_data

def push_data_to_database(app):
    global db_install
    if db_install == False:
        with app.app_context():
            data_to_push = parse_data()
            for key, value in data_to_push.items():
                if "name" in value.keys():
                    facilty = Facility(key, value["relations"]["5"], value["relations"]["6"], value["relations"]["9"], value["relations"]["10"], name=value["name"])
                    db.session.add(facilty)
                else:
                    facilty = Facility(key, value["relations"]["5"], value["relations"]["6"], value["relations"]["9"], value["relations"]["10"])
                    db.session.add(facilty)
            db.session.commit()
            print("Data was fetched from file and pushed to database")
            print("Install complete")
            db_install = True