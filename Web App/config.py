import os

from dotenv import dotenv_values

env_variables = dotenv_values()

database_name = env_variables['DATABASE_NAME']
username = env_variables['DATABASE_USERNAME']
password = env_variables['DATABASE_PASSWORD']
database_uri = env_variables['DATABASE_URI']

database_path = f'postgresql://{username}:{password}@{database_uri}/{database_name}'
SQLALCHEMY_DATABASE_URI = database_path
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True