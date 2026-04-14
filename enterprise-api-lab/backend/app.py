from flask import Flask, request, jsonify
from flask_cors import CORS
from auth import generate_token, verify_token
import uuid

app = Flask(__name__)
CORS(app)

request_count = 0

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")

    if username != "admin":
        return jsonify({"message": "Invalid user"}), 401

    token = generate_token(username)

    return jsonify({
        "token": token
    })

def check_auth():
    token = request.headers.get("Authorization")
    return token and verify_token(token)

@app.route('/process', methods=['POST'])
def process():
    global request_count

    if not check_auth():
        return jsonify({"message": "Unauthorized"}), 403

    request_count += 1
    request_id = str(uuid.uuid4())

    data = request.json
    name = data.get("name")

    return jsonify({
        "message": f"Hello {name}",
        "request_number": request_count,
        "request_id": request_id
    })

@app.route('/stats')
def stats():
    return jsonify({
        "total_requests": request_count
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)