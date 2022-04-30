import os
import jwt
import datetime

from flask import Flask, jsonify, request, redirect, url_for, Response
from flask_cors import CORS

from lib.queries import validate_user
from lib.helpers import token_required

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route('/')
def index():
    return 'Hello World!'

#Login endpointfrom lib.helpers import token_required
@app.route('/login', methods=['POST'])
def login():

	data = request.get_json()
	user = data['user']
	password = data['pass']
	
	if validate_user(user, password):
		token = jwt.encode({
				'user' : user, 
				'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
			}, 
			app.config['SECRET_KEY'], 
			algorithm="HS256")

		return jsonify({
			'login' : 'valid',
			'token' : token.decode("utf-8")
		})

	return jsonify({
		'login' : 'invalid'
	})

#Call Ready Endpoint
@app.route('/call-ready', methods=['POST'])
@token_required
def call_ready():
	return jsonify({
			'status' : 'token validated'
		})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
    #app.run(host='treeserver', port=5001)
