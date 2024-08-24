#!/usr/bin/python3
class State(BaseModel):
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

class City(BaseModel):
    __tablename__ = 'cities'
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
