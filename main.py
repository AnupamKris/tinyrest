from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/api", methods=["GET"])
def api():
    return jsonify({"message": "Hello World!"})

if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")

