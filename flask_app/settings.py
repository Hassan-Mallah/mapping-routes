import os
import secrets

DATABASE_URL = os.environ['DATABASE_URL'] # server
# DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/others"  # local
SQLALCHEMY_DATABASE_URI = DATABASE_URL
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = secrets.token_urlsafe(16)

# Flask-User settings
USER_APP_NAME = 'Mapping Routes'
USER_ENABLE_EMAIL = False  # Disable email authentication
USER_ENABLE_USERNAME = True  # Enable username authentication