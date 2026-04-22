from flask import Flask, request, jsonify

app = Flask(__name__)

# 🔐 simple security check
API_KEY = "secret123"

@app.route('/callback', methods=['POST'])
def callback():
    if request.headers.get("X-API-KEY") != API_KEY:
        return "Forbidden", 403

    data = request.json
    print("🔥 Callback received:", data)

    return jsonify({"status": "received"}), 200


@app.route('/')
def home():
    return "Frontend callback server is running"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)