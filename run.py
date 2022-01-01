import psycopg2

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#Call Ready Endpoint
@app.route('/call-ready', methods=['POST'])
def call_ready():
	return jsonify(success='Awesome Yessir')

if __name__ == '__main__':
    app.run(host='treeserver', port=5001)
