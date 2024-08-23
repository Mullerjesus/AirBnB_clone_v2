#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    """Handles storage of objects in JSON format"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves the objects to a JSON file"""
        with open(self.__file_path, 'w') as f:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, f)

    def reload(self):
        """Loads objects from the JSON file"""
        try:
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
                for key, value in objs.items():
                    cls_name = value['__class__']
                    self.new(eval(cls_name)(**value))
        except FileNotFoundError:
            pass

    def close(self):
        """Deserializes the JSON file to objects."""
        self.reload()
