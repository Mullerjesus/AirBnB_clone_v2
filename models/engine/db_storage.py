#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
import os


class DBStorage:
    """Database storage class for interacting with the MySQL database."""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize engine and drop all tables if environment is 'test'."""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        # Create engine for the database
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@{host}/{database}',
            pool_pre_ping=True
        )

        # Drop all tables if environment is 'test'
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects from the database.
        If cls is specified, query only objects of that class.
        """
        if cls:
            objs = self.__session.query(cls).all()
        else:
            objs = self.__session.query(State).all()
        return {
            f"{obj.__class__.__name__}.{obj.id}": obj for obj in objs
        }

    def new(self, obj):
        """Add the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete the object from the current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        self.__session = scoped_session(session_factory)()

    def close(self):
        """Close the current session."""
        self.__session.close()
