from flask import Flask, jsonify, send_from_directory
from scanner import run_scan
import os

app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/api/scan", methods=["GET"])
def api_scan():
    try:
        results = run_scan()
        return jsonify({"status": "success", "data": results})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    print("Starting Web Stock Scanner on http://localhost:5000")
    app.run(debug=True, port=5000)
