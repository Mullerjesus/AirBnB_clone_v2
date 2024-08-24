#!/usr/bin/python3
"""
This module initializes the models package.
"""
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
