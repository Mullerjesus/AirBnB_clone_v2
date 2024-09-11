#!/usr/bin/python3
"""Database storage engine using SQLAlchemy ORM."""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.state import State
from models.city import City


class DBStorage:
    """Database storage engine for managing SQLAlchemy sessions and objects."""

    __engine = None
    __session = None

    def __init__(self):
        """Create a new SQLAlchemy engine and session."""
        self.__engine = create_engine('sqlite:///db.sqlite3')  # Replace
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    def all(self, cls=None):
        """Return a dictionary of objects of specific class or all objects."""
        if cls:
            return {obj.id: obj for obj in self.__session.query(cls).all()}

        objects = {}
        for cls in [State, City]:  # Add all model classes here
            for obj in self.__session.query(cls).all():
                objects[obj.id] = obj
        return objects

    def new(self, obj):
        """Add a new object to the session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the database."""
        self.__session.commit()

    def reload(self):
        """Reload objects from the database."""
        self.__session.remove()
        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    def close(self):
        """Close the session."""
        self.__session.remove()
        self.__session = scoped_session(sessionmaker(bind=self.__engine))
