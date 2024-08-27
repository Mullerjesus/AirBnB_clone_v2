#!/usr/bin/python3
import json
from models.base_model import BaseModel
# Import other required models...

class FileStorage:
    """FileStorage class serializes instances to a JSON file and deserializes back to instances"""

    __file_path = "file.json"  # Path to the JSON file
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary __objects"""
        # Implementation remains the same

    def new(self, obj):
        """Adds a new object to the storage"""
        # Implementation remains the same

    def save(self):
        """Saves the current state of __objects to the JSON file"""
        with open(self.__file_path, 'w') as f:
            json.dump(
              {
                  key: obj.to_dict() for key, obj in self.__objects.items()
                  }, f)

    def reload(self):
        """Reloads the objects from the JSON file"""
        # Implementation remains the same

    def close(self):
        """Deserializes the JSON file to objects"""
        self.reload()
