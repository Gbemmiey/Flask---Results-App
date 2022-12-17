import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

from dotenv import dotenv_values

env_variables = dotenv_values()

database_name = env_variables['DATABASE_NAME']
username = env_variables['DATABASE_USERNAME']
password  = env_variables['DATABASE_PASSWORD']
database_uri = env_variables['DATABASE_URI']

database_path = 'postgresql://{}:{}@{}/{}'.format(username, password, database_uri, database_name)

db = SQLAlchemy()

"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
