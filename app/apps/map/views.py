from flask import Blueprint, request, url_for, render_template, flash

map_blueprint = Blueprint('map_blueprint', __name__, template_folder="templates", static_folder="static" )

@map_blueprint.route("/", methods=['POST', 'GET'])
def map():
    return render_template('map.html')