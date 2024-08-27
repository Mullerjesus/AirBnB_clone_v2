#!/usr/bin/python3

# Ensure that the following imports align with your project's structure.
from models.base_model import Base
from models.state import State
from models.city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace the DATABASE_URI with the actual database URI for your project
DATABASE_URI = 'mysql+mysqldb://hbnb_dev:hbnb_pwd@localhost/hbnb_dev_db'

def setup_database():
    try:
        # Create a new engine instance
        engine = create_engine(DATABASE_URI)

        # Bind the engine to the Base class, so the declaratives can be accessed through a DBSession instance
        Base.metadata.bind = engine

        # Create all tables in the engine. This is equivalent to "Create Table" statements in raw SQL.
        Base.metadata.create_all(engine)

        print("Tables created successfully!")

    except Exception as e:
        print(f"An error occurred while setting up the database: {e}")

if __name__ == "__main__":
    setup_database()
