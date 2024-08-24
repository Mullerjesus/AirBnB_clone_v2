#!/usr/bin/python3  
"""  
This module implements the DBStorage class for managing  
the database connections and sessions.  
"""  
from sqlalchemy import create_engine  
from sqlalchemy.orm import sessionmaker  

class DBStorage:  
    """  
    The DBStorage class manages the database storage and retrieval of instances.  
    """  
    __engine = None  
    __session = None  

    def __init__(self):  
        """Initializes the DBStorage class and creates the engine."""  
        self.__engine = create_engine('mysql://user:pwd@localhost/db_name')  

    def all(self):  
        """Returns all objects in the database."""  
        return self.__session.query(State).all()  

    def close(self):  
        """Closes the current session."""  
        self.__session.remove()
