#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    """Base class for all models in the AirBnB project"""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel"""
        # Implementation of initialization
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Updates the updated_at attribute"""
        self.updated_at = datetime.now()
        # Save logic

    def to_dict(self):
        """Convert the instance to a dictionary"""
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            # Additional attributes
        }


class Base(BaseModel):
    """Base for SQLAlchemy models"""
    __abstract__ = True
