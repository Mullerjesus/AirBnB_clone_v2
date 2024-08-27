#!/usr/bin/python3

import os  # Import the os module

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """DBStorage class for the database"""

    __engine = None
    __session = None

    def __init__(self):
        """Create the engine"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.getenv("HBNB_MYSQL_USER"),
                os.getenv("HBNB_MYSQL_PWD"),
                os.getenv("HBNB_MYSQL_HOST"),
                os.getenv("HBNB_MYSQL_DB")
            )
        )

    def all(self, cls=None):
        """Returns the dictionary of objects"""
        # Implementation remains the same

    def new(self, obj):
        """Adds a new object to the session"""
        # Implementation remains the same

    def save(self):
        """Commits all changes to the database"""
        # Implementation remains the same

    def reload(self):
        """Creates a new session for the current database"""
        Session = sessionmaker(bind=self.__engine)
        self.__session = scoped_session(Session)

    def remove(self):
        """Removes the current session"""
        self.__session.remove()

    def close(self):
        """Closes the current session"""
        self.remove()
