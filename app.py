# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/others"  # local
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://postgres:postgres@postgres:5432"  # server
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///still-harbor-31837"  # server
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