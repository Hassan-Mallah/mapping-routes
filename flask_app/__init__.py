from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserManager


db = SQLAlchemy()


def create_app(extra_config_settings={}):
    app = Flask(__name__)
    app.config.from_object('flask_app.settings')
    db.init_app(app)

    from .views import register_blueprints
    register_blueprints(app)

    from .models.tables import User
    user_manager = UserManager(app, db, User)

    with app.app_context():
        try:
            db.drop_all()
        except:
            print('empty DB')
        db.create_all()

    return app
