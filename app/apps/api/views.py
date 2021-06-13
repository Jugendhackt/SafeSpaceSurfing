from flask_restful import Resource, abort, marshal_with, fields
from database.database import db, Facility

facility_resource_fields = {
    'f_id':fields.Integer,
    'osm_id':fields.String,
    'name':fields.String,
    'description':fields.String
}

class facility_data(Resource):
    @marshal_with(facility_resource_fields)
    def get(self, osm_level, osm_relation):
        self.check_osm_level(osm_level)
        self.check_osm_relation(osm_relation)
        osm_facilities = []
        if int(osm_level) == 5:
            osm_facilities = Facility.query.filter_by(osm_admin_lvl5=osm_relation).all()
        if int(osm_level) == 6:
            osm_facilities = Facility.query.filter_by(osm_admin_lvl6=osm_relation).all()
        if int(osm_level) == 9:
            osm_facilities = Facility.query.filter_by(osm_admin_lvl9=osm_relation).all()
        if int(osm_level) == 10:
            osm_facilities = Facility.query.filter_by(osm_admin_lvl10=osm_relation).all()
        if not osm_facilities:
            abort(404, message="Nothing found")
        return osm_facilities
    
    def check_osm_level(self, osm_level):
        if int(osm_level) != 5 and int(osm_level) != 6 and int(osm_level) != 9 and int(osm_level) != 10:
            abort(400, message="Open Street Map Level should contain the number 5,6,9 or 10")

    def check_osm_relation(self, osm_relation):
        if osm_relation.find('/') != -1:
            split_data = osm_relation.split("/")
            print(split_data[1].isdigit())
            if split_data[1].isdigit() == True:
                if split_data[0] == "relation":
                    return
        abort(400, message="Open Street Map relation is defined with (relation/<number>)")