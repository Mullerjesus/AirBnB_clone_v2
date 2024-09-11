#!/usr/bin/python3
"""Module for file storage."""

import os
import pickle


class FileStorage:
    """Class for managing file storage."""

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Return a dictionary of objects or all objects of specific class."""
        if cls is None:
            return self.__objects

        cls_name = cls.__name__
        return {
            key: value
            for key, value in self.__objects.items()
            if key.startswith(cls_name)
        }

    def new(self, obj):
        """Add a new object to the storage."""
        if obj is None:
            return

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Save the objects to a file."""
        with open(self.__file_path, 'wb') as file:
            pickle.dump(self.__objects, file)

    def reload(self):
        """Load objects from a file."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'rb') as file:
                self.__objects = pickle.load(file)

    def delete(self, obj=None):
        """Delete an object from the storage."""
        if obj is None:
            return

        key = f"{obj.__class__.__name__}.{obj.id}"
        if key in self.__objects:
            del self.__objects[key]

    def close(self):
        """Call the reload method to ensure objects are reloaded."""
        self.reload()
