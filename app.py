from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hi():
    return "<p>Hi!</p>"


@app.route("/drivers", methods=["POST"])
def post_drivers():
    return jsonify()


if __name__ == "__main__":
    app.run()
