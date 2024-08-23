import json
from models.base_model import BaseModel

class FileStorage:
    """This class manages the storage of objects in a JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def reload(self):
        """Reloads the object from the JSON file."""
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass  # Ignore file not found error

    def close(self):
        """Deserializes the JSON file to objects."""
        self.reload()  # Call the reload method to load data from the JSON file. 
