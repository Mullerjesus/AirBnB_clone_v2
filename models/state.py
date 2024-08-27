#!/usr/bin/python3

from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """State class"""

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete, delete-orphan')

    def cities(self):
        """Returns the list of City objects linked to the current State"""
        from models import storage
        if storage.get_engine_type() != "db":
            return [city for city in storage.all('City').values() if city.state_id == self.id]
        return []  # If DBStorage, cities are already managed by SQLAlchemy
