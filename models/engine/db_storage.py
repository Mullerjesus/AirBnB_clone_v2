#!/usr/bin/python3
from models import storage  
from sqlalchemy import create_engine  
from sqlalchemy.orm import sessionmaker, scoped_session  

class DBStorage:  
    """DBStorage class for the database"""  
    
    __engine = None  
    __session = None  

    def __init__(self):  
        """Create the engine"""  
        # Implementation remains the same  

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
        # Implementation remains the same  

    def remove(self):  
        """Removes the current session"""  
        # Close the session and remove it  
        self.__session.remove()  

    def close(self):  
        """Closes the session"""  
        self.remove()
