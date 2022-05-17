#!/usr/bin/env python3
"""
Basic Flask app
"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'], strict_slashes=False)
def index():
    """display index page"""
    return render_template('0-index.html')


class Config(object):
    """
    Basic Flask app
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


if __name__ == '__main__':
    app.run(debug=True)
