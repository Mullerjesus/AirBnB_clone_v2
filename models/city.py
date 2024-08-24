#!/usr/bin/python3
"""
This module defines the City class which represents a city entity
in the AirBnB clone project.
"""
from models.base_model import BaseModel

class City(BaseModel):
    """
    The City class represents a city in the AirBnB clone.
    It inherits from BaseModel.
    """

    def __init__(self, state_id, name):
        """Initializes a new City instance."""
        self.state_id = state_id  # ID of the State to which this city belongs
        self.name = name  # The name of the city

    def __str__(self):
        """Returns a string representation of the City instance."""
        return f"[City] ({self.id}) {self.__dict__}"
