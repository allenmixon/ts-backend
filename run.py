import psycopg2
import jwt
import datetime

from flask import Flask, jsonify, request, redirect, url_for, Response
from flask_cors import CORS
from functools import wraps

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'mykey'

def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token = request.args.get('token')

		if not token:
			return jsonify({'message' : 'Token is missing'}), 403

		try:
			data = jwt.decode(token, app.config['SECRET_KEY'])
		except:
			return jsonify({'message' : 'Token is invalid'}), 403

		return f(*args, **kwargs)

	return decorated

#Login endpoint
@app.route('/login', methods=['POST'])
def login():
	user = request.form.get('user')
	password = request.form.get('pass')
	
	if password == 'starchild':
		token = jwt.encode({'user' : user, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=1)}, app.config['SECRET_KEY'])
		response = jsonify({'token' : token.decode('UTF-8')})

		return response

	return 'Invalid login'

#For testing
@app.route('/protected')
@token_required
def protected():
	return '/protected - Valid login'

#Call Ready Endpoint
@app.route('/call-ready', methods=['POST'])
@token_required
def call_ready():
	return "Awesome yessirrr"

if __name__ == '__main__':
    app.run(host='treeserver', port=5001)
