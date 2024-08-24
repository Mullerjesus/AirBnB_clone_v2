#!/usr/bin/python3  
"""  
This module implements the FileStorage class for managing  
the serialization and deserialization of data to and from a JSON file.  
"""  
import json  

class FileStorage:  
    """  
    The FileStorage class serializes instances to a JSON file and  
    deserializes JSON file to instances.  
    """  
    __file_path = "file.json"  
    __objects = {}  

    def all(self):  
        """Returns the dictionary __objects."""  
        return self.__objects  

    def reload(self):  
        """Deserializes the JSON file to __objects."""  
        try:  
            with open(self.__file_path, 'r') as f:  
                self.__objects = json.load(f)  
        except FileNotFoundError:  
            pass  

    def close(self):  
        """Deserializes the JSON file to objects."""  
        self.reload()
