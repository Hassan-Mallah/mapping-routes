from flask_app import db
from flask import Blueprint, render_template, flash, request
from flask_user import current_user, login_required
from flask_app.models.interface import create_route, all_records, one_record
from flask_app.models.tables import Route, User

main_blueprint = Blueprint('main', __name__, url_prefix='')


@main_blueprint.route('/', methods=["GET", "POST"])
@login_required
def index():
    if request.form:
        name = request.form['name']
        amount = request.form['amount']
        user_id = current_user.id
        create_route(name, int(amount), user_id)
        flash('Route created', 'success')

    return render_template('home_page.html')


@main_blueprint.route('/all_routes')
# @login_required
def all_routes():
    users = all_records(User)
    return render_template('all_routes.html', users=users)


@main_blueprint.route('route_view/<int:id>', methods=["GET"])
# @login_required
def route_view(id):
    route = one_record(Route, id=id)
    return render_template('route_view.html', route=route)


@main_blueprint.route('user_routes', methods=["GET"])
@login_required
def user_routes():
    id = current_user.id
    user = one_record(User, id=id)
    return render_template('user_routes.html', user=user)
