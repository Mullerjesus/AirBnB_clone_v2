#!/usr/bin/python3

class FileStorage:
    """FileStorage class serializes instances to a JSON file."""

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary __objects."""
        # Implementation

    def new(self, obj):
        """Adds a new object to __objects."""
        # Implementation

    def save(self):
        """Saves the current state of __objects to __file_path."""
        # Implementation

    def reload(self):
        """Reloads the objects from the JSON file."""
        # Implementation

    def close(self):
        """Deserializes the JSON file to objects."""
        self.reload()
