#!/usr/bin/python3
"""
This module implements a simple Flask application that returns
the greeting 'Hello HBNB!' when accessed on the root URL.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return a simple greeting.

    This function is mapped to the root URL and returns
    the string 'Hello HBNB!'.
    """
    return "Hello HBNB!"


@app.route('/favicon.ico', methods=['GET'])
def favicon():
    """Handle the favicon request.

    This function returns a 204 No Content response when
    a browser requests the favicon.ico.
    """
    return '', 204  # No content


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
