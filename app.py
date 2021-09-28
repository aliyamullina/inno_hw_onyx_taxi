from flask import Flask, jsonify, request
from db import Driver, Client, Order

app = Flask(__name__)


@app.route("/")
def hi():
    return "<p>Hi!</p>"


@app.route("/drivers", methods=["POST"])
def post_drivers():
    content = request.get_json()
    return jsonify(content)


if __name__ == "__main__":
    app.run()
