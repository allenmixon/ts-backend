import jwt
import datetime

from flask import jsonify, request

from lib.queries import validate_user
from lib.helpers import token_required

def add_routes(app):
	@app.route('/')
	def index():
	    return 'Hello World!'

	#Login endpointfrom lib.helpers import token_required
	@app.route('/login', methods=['POST'])
	def login():

		data = request.get_json()
		user = data['user']
		password = data['pass']

		valid = validate_user(user, password)
		
		if valid:
			token = jwt.encode({
					'user' : user, 
					'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
				}, 
				app.config['SECRET_KEY'], 
				algorithm="HS256")

			return jsonify({
				'login' : 'valid',
				'token' : token
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