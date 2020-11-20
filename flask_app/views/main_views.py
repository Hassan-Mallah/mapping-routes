from flask_app import db
from flask import Blueprint, redirect, render_template

main_blueprint = Blueprint('main', __name__, url_prefix='')

print('hey')
@main_blueprint.route('/')
def index():
    x = db.session.execute('select 1 as is_alive;').fetchall()
    return "<h1>Welcome to our server !! {}</h1>".format(x)
