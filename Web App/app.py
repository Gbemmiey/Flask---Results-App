import json
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify
from flask_moment import Moment
from flask_migrate import Migrate

from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
db = SQLAlchemy(app)
moment = Moment(app)
app.config.from_object('config')

migrate = Migrate(app, db)


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


@app.route("/")
def hello():
    """Return Hello"""
    return render_template('pages/index.html')


@app.route("/login")
def display_login():
    """Displays login page"""
    return render_template('forms/login.html')

@app.route("/signup")
def display_signup():
    """Displays login page"""
    return render_template('forms/signup.html')


@app.errorhandler(404)
def not_found(error):
    """
    Error handler for 404
    """
    return jsonify({
        'success': False,
        'error': 404,
        'message': 'Not Found'
    }), 404

@app.errorhandler(422)
def unprocessable_entity(error):
    """
    Error handler for 422
    """
    return jsonify({
        'success': False,
        'error': 422,
        'message': 'Unprocessable Entity'
    }), 422
