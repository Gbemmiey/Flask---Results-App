from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy

from dotenv import dotenv_values

env_variables = dotenv_values()

database_name = env_variables['DATABASE_NAME']
username = env_variables['DATABASE_USERNAME']
password = env_variables['DATABASE_PASSWORD']
database_uri = env_variables['DATABASE_URI']

database_path = f'postgresql://{username}:{password}@{database_uri}/{database_name}'

db = SQLAlchemy()


def setup_db(app, db_path=database_path):
    """
    setup_db(app)
    binds a flask application and a SQLAlchemy service
    """
    app.config["SQLALCHEMY_DATABASE_URI"] = db_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.drop_all()
    db.create_all()


class Staff(db.Model):
    """
    Model created for school staff
    """
    __tablename__ = 'staff'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)

    def __init__(self, name, role):
        self.name = name
        self.role = role
