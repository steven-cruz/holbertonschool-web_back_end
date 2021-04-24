#!/usr/bin/env python3
"""
    basic flask app
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hola mundo!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
