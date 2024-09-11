#!/usr/bin/python3


from models.base_model import BaseModel
from models.base import Base


class City(BaseModel, Base):
    """City class for managing cities in the database."""

    __tablename__ = 'cities'
    
    # Define columns here
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    state = relationship("State", back_populates="cities")
