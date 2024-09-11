#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json

class FileStorage:
    # other methods ...

    def close(self):
        """Call the reload method for deserializing the JSON file to objects"""
        self.reload()
