# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
DATABASE_URL = os.environ['DATABASE_URL'] # server
# DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/others"  # local
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


# A welcome message to test our server
@app.route('/')
def index():
    x = db.session.execute('select 1 as is_alive;').fetchall()
    return "<h1>Welcome to our server !! {}</h1>".format(x)


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)