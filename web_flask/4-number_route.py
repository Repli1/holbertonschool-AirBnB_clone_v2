#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_fun(text):
    return "C " + str(text).replace("_", " ")


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_cool(text):
    return "Python " + str(text).replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number_is(n):
    return str(n) + " is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
