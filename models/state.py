#!/usr/bin/python3
"""
This module defines the State class which represents a state entity
in the AirBnB clone project.
"""
from models import storage
from models.city import City


class State:
    def __init__(self, name):
        """Initializes a new State instance."""
        self.name = name
        self.id = None  # Use None instead of ...

    def cities(self):
        """Returns a list of cities related to this state."""
        return [
            city for city in storage.all(City).values()
            if city.state_id == self.id
        ]
