import os
import jwt

from functools import wraps
from flask import request, jsonify

from dotenv import load_dotenv

load_dotenv()

def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		data = request.get_json()
		token = data['token']

		if not token:
			return jsonify({
				'message' : 'Token is missing'
			}), 403

		try:
			data = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])
		except:
			return jsonify({
				'message' : 'Token is invalid'
			}), 403

		return f(*args, **kwargs)

	return decorated