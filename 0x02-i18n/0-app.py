#!/usr/bin/env python3

"""
This module holds a simple module to
learn and practice i18n in flask
"""

from flask import Flask,  render_template
from flask_babel import Babel


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders a basic html template
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
