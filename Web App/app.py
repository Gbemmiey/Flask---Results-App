import json
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify
from flask_moment import Moment
from flask_migrate import Migrate

from models import setup_db



app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = setup_db(app)


migrate = Migrate(app, db)


@app.route("/")
def hello():
    """Return Hello"""
    return render_template('pages/index.html')



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
