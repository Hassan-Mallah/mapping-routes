# DATABASE_URL = os.environ['DATABASE_URL'] # server
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/others"  # local
SQLALCHEMY_DATABASE_URI = DATABASE_URL
SQLALCHEMY_TRACK_MODIFICATIONS = True
