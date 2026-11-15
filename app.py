
import os
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

APP_VERSION = "1.0.0"
GIT_SHA = os.environ.get("GIT_SHA", "local")


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/health")
def health():
    return jsonify(status="healthy"), 200


@app.get("/api/info")
def info():
    return jsonify(
        app="cicd-demo",
        version=APP_VERSION,
        commit=GIT_SHA
    )


@app.post("/api/echo")
def echo():
    data = request.get_json(silent=True)

    if data is None:
        return jsonify(error="Send a JSON body"), 400

    return jsonify(received=data), 201


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080))
    )
