#!/usr/bin/python3

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Displays cities by states retrieved from the database.
    """
    states = storage.all("State").values()
    cities = storage.all("City").values()

    return render_template('cities_by_states.html', states=sorted(states, key=lambda state: state.name), cities=cities)

@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage session after each request.
    """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
