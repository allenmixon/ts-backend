from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/call-ready', methods=['POST'])
def call_ready():
	return jsonify(success=True)

if __name__ == "__main__":
	app.run(debug=True)