from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(extra_config_settings={}):
    app = Flask(__name__)
    app.config.from_object('app.settings')
    db.init_app(app)
    from .views import register_blueprints
    register_blueprints(app)

    return app
