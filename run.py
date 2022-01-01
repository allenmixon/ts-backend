#test6

from flask import Flask, jsonify

app = Flask(__name__)

#Call Ready Endpoint
@app.route('/call-ready', methods=['POST'])
def call_ready():
	return jsonify(success='Verified')

if __name__ == '__main__':
    app.run(host='treeserver', port=5001)
