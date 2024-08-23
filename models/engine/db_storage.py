#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel

class DBStorage:


    """Handles storage of objects in a SQL database"""

    __engine = None
    __session = None

    def __init__(self):
        """Creates the engine and the session"""
        self.__engine = create_engine\n
        ('mysql+mysqldb://hbnb_dev:hbnb_dev_pwd@localhost/hbnb_dev_db')
        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    def all(self, cls=None):
        """Returns a dictionary of objects"""
        if cls:
            return self.__session.query(cls).all()
        return self.__session.query(BaseModel).all()

    def new(self, obj):
        """Adds a new object to the session"""
        self.__session.add(obj)

    def save(self):
        """Commits the current session"""
        self.__session.commit()

    def reload(self):
        """Loads the table in the database"""
        BaseModel.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    def close(self):
        """Removes the current session"""
        self.__session.remove()
