#!/usr/bin/python3
"""This module defines a class to manage DB storage for hbnb clone"""
from sqlalchemy.orm import sessionmaker, scoped_session
# other imports ...

class DBStorage:
    # other methods ...

    def close(self):
        """Close the current SQLAlchemy session"""
        self.__session.remove()
