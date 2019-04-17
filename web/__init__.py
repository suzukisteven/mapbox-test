from app import app
from flask import render_template, abort, request, Response, jsonify, redirect, url_for, Response
from flask_assets import Environment, Bundle
from flask_login import LoginManager, current_user, login_required
from flask_wtf.csrf import CSRFProtect
from .util.assets import bundles
from web.blueprints.users.views import users_blueprint
from web.blueprints.sessions.views import sessions_blueprint
from models.user import User
from models.trip import Trip
import re
import os, time

from geojson import Point, Feature, FeatureCollection
from mapbox import Geocoder, Maps

# Assets
assets = Environment(app)
assets.register(bundles)

# Mapbox
maps = Maps()
geocoder = Geocoder(access_token = os.environ.get("MAPBOX_KEY"))
# perm_geocoder = Geocoder(name='mapbox.places-permanent')

# CSRF Protect
csrf = CSRFProtect(app)

# Login Manager & User Loader settings
login_manager = LoginManager(app)
@login_manager.user_loader
def load_user(id):
    return User.get_or_none(id=id)

login_manager.login_view = "sessions.login"
login_manager.login_message = u"You must be logged in to view this content."
login_manager.login_message_category = "danger"

# Registering Blueprints
app.register_blueprint(users_blueprint, url_prefix="/users")
app.register_blueprint(sessions_blueprint, url_prefix="/sessions")
# app.register_blueprint(something_blueprint, url_prefix="/something")

# Error Routes
@app.errorhandler(404)
def internal_server_error(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Home Route
@app.route("/")
def home():
    # abort(404)
    response = geocoder.forward("Next Academy")
    response_status_code = response.status_code
    response_headers = response.headers
    collection = response.json()
    collection['type'] == 'FeatureCollection'
    first = response.geojson()['features'][0]

    return render_template('home.html', first=first, collection=collection, response=response)
    

# These functions need to be cleaned up.
@app.route('/search', methods=["POST"])
def search():
    query = request.form.get('map_query')
    response = geocoder.forward(query)
    collection = response.json()
    collection['type'] == 'FeatureCollection'
    first = response.geojson()['features'][0]
    latitude = response.geojson()['features'][0]['center'][0]
    longitude = response.geojson()['features'][0]['center'][1]

    return redirect(url_for('map', query=query, latitude=latitude, longitude=longitude, first=first, response=response))


@app.route('/map/<query>', methods=["GET"])
def map(query):
    response = geocoder.forward(query)
    first = response.geojson()['features'][0]
    latitude = response.geojson()['features'][0]['center'][0]
    longitude = response.geojson()['features'][0]['center'][1]
    trips = Trip.select().order_by(Trip.created_at.desc())

    return render_template('map.html', response=response, latitude=latitude, longitude=longitude, first=first, trips=trips)

@app.route('/save_location/<query>', methods=['POST'])
def save_location(query):
    response = geocoder.forward(query)
    latitude = response.geojson()['features'][0]['center'][0]
    longitude = response.geojson()['features'][0]['center'][1]
    first = response.geojson()['features'][0]
    address = first['place_name']
    new_event = Trip(longitude=longitude, latitude=latitude, address=address)

    if new_event.save():
        print('Successfully Saved Trip to DB')
        return redirect(url_for('map', query=query, first=first))
    else:
        print('Failed to Save')
        return redirect(url_for('map', query=query, first=first))
    




