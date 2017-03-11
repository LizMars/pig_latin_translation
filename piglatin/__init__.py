"""Pig Latin Translation Microservice."""
from flask import Flask
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)


from piglatin import main
