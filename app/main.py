#imports the flask framework
from flask import Flask
#Imports database handler
from database import database
#Imports restful flask
from flask_restful import Api

#import the api endpoint
from apps.api.views import facility_data

#imports the login view
from apps.login.views import login_blueprint
from apps.map.views import map_blueprint

def create_app():
    #Creates an Flask application
    app = Flask(__name__)
    #Defines the configuration of the application
    app.config.from_object('config.DevelopmentConfig')

    #Creates a restuful api instance
    api = Api(app)

    #Initializes the database
    database.init_app(app)

    #registers the login blueprint
    app.register_blueprint(login_blueprint, url_prefix='/login')
    app.register_blueprint(map_blueprint, url_prefix='/map')

    #defines an api endpoints
    api.add_resource(facility_data, "/api/v1/facilities/<int:osm_level>/<path:osm_relation>")

    return app



if __name__ == '__main__':
    create_app().run()

