import psycopg2

from flask import Flask, jsonify, request, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#Login endpoint
@app.route('/login', methods=['POST'])
def login():
	password = request.form.get('pass')
	return f'Your pass sir: {password}'

#Call Ready Endpoint
@app.route('/call-ready', methods=['POST'])
def call_ready():
	return "Awesome yessirrr"

if __name__ == '__main__':
    app.run(host='treeserver', port=5001)
