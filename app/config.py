'''

In this file we define which variables we want to use in our project and what their definition

'''

import os

DATABASE_TYPE = os.getenv("DATABASE_TYPE", "postgresql")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = int(os.getenv("DATABASE_PORT", 5432)) 
DATABASE_NAME = os.getenv("DATABASE_NAME")

# Define postgres connection
# format for sqlalchemy:
# postgresql://username:password@hostname:hostport/database_name
SQLALCHEMY_DATABASE_URI = f"{DATABASE_TYPE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

