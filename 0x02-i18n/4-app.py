#!/usr/bin/env python3
"""
Basic Flask app
"""


from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Basic Flask app
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('4-app.Config')


@babel.localeselector
def get_locale():
    """ get locale from request """
    locale = request.args.get('locale')
    if locale is not None and locale in Config.LANGUAGES:
        return locale
    else:
        return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """display index page"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
