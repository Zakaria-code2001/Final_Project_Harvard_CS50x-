from flask import Flask


def create_app():
    """ Creation of a Flask application """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '12345678910'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app
