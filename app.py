from flask import Flask, jsonify, request
from sqlalchemy.orm import scoped_session, sessionmaker
from contextlib import contextmanager

from db import Driver, Client, Order, engine

Session = scoped_session(sessionmaker(autoflush=True, autocommit=False, bind=engine))


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()


app = Flask(__name__)


@app.route("/")
def hi():
    return "<p>Hi!</p>"


@app.route("/drivers", methods=["POST"])
def post_drivers():
    content = request.get_json()
    with session_scope() as session:
        new_driver = Driver(name=content["name"], car=content["car"])
        session.add(new_driver)
    return jsonify(content)


if __name__ == "__main__":
    app.run()
