
from flask import Flask
from flask_cors import CORS
from os import getenv
from dotenv import load_dotenv

from lib.routes import add_routes

load_dotenv()

def create_app():
	app = Flask(__name__)
	CORS(app)

	app.config['SECRET_KEY'] = getenv('SECRET_KEY')

	add_routes(app)

	return app
