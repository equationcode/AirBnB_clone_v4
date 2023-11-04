#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid


app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/2-hbnb/', strict_slashes=False)
def hbnb():
    """ HBNB is alive! """
    all_states = storage.all(State).values()
    sorted_states = sorted(all_states, key=lambda k: k.name)
    states_with_cities = []

    for state in sorted_states:
        states_with_cities.append([state, sorted(state.cities, key=lambda k: k.name)])

    all_amenities = storage.all(Amenity).values()
    sorted_amenities = sorted(all_amenities, key=lambda k: k.name)

    all_places = storage.all(Place).values()
    sorted_places = sorted(all_places, key=lambda k: k.name)

    return render_template('2-hbnb.html',
                           states=states_with_cities,
                           amenities=sorted_amenities,
                           places=sorted_places,
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    """ the main function """
    app.run(host='0.0.0.0', port=5001)