"""Dynamic Web Application for Results App"""

from flask import Flask, render_template, flash, redirect, jsonify
from flask_moment import Moment
from flask_migrate import Migrate

from flask import jsonify, make_response, request
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import uuid
import jwt
import datetime

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


class Class(db.Model):
    """Model created for Students"""
    __table__name = 'class'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    class_teacher_id = Column(Integer)


class Subject(db.Model):
    """Model created for Students"""
    __table__name = 'subject'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Student(db.Model):
    """Model created for Students"""
    __table__name = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    access_code = Column(String)
    class_id = Column(Integer)


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


@app.route('/auth', methods=['POST'])
def authenticate_user():
    """Authenticates users"""
    flash("Logged In!")
    return redirect('/')


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


if __name__ == '__main__':
    app.run(debug=True)
