# __init__.py is a special Python file that allows a directory to become
# a Python package so it can be accessed using the 'import' statement.

from flask import Flask
from flask_script import Manager
from flask.ext import restful
from flask.ext.cors import CORS

app = Flask(__name__)
manager = Manager(app)
api = restful.Api(app)
CORS(app)

from app.startup.create_app import create_app
from framework import errors

app.handle_exception = errors.handle_exception
app.handle_user_exception = errors.handle_exception
