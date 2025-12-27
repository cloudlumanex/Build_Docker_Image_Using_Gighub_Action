from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route("/", methods=["GET"])
def health_check():
    """
    Basic health endpoint for container validation
    """
    return jsonify({
        "status": "ok",
        "service": "sample-python-app",
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENV", "development")
    }), 200


@app.route("/version", methods=["GET"])
def version():
    """
    Application version endpoint
    """
    return jsonify({
        "version": os.getenv("APP_VERSION", "1.0.0")
    }), 200


if __name__ == "__main__":
    # Flask dev server (sufficient for demo and CI/CD pipelines)
    app.run(host="0.0.0.0", port=5000)
