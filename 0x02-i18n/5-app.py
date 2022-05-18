#!/usr/bin/env python3
"""
Basic Flask app
"""


from flask import Flask, render_template, request, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
babel = Babel(app)


@app.route('/', methods=['GET', 'POST'], strict_slashes=False)
def index():
    """display index page"""
    return render_template('5-index.html')


class Config(object):
    """
    Basic Flask app
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ get locale from request """
    locale = request.args.get('locale')
    if locale is not None:
        return locale
    else:
        return request.accept_languages.best_match(Config.LANGUAGES)


def get_user() -> Union[dict, None]:
    """ returns a user dictionary """
    login_as = request.args.get("login_as", False)
    if login_as:
        user = users.get(int(login_as), False)
        if user:
            return user
    return None


@app.before_request
def before_request():
    """ find a user if any, and set it as a global on flask.g.user"""
    g.user = get_user()


if __name__ == '__main__':
    app.run(debug=True)