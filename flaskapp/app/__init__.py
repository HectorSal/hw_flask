from flask import Flask
from config import Config

myapp_obj = Flask(__name__)
myapp_obj.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess'
)

from app import routes
