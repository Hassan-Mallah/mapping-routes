from flask_app.models.tables import session, Route, Point


# create route based on name, amount, user_id
def create_route(name, amount, user_id):
    import random

    route = create(Route, name=name, user_id=user_id)
    coords = [(float((random.random() * 180.0)) - 90, float((random.random() * 180.0)) - 180) for _ in range(int(amount))]

    for i in range(amount):
        create(Point, route_id=route.id, coordinates_x=coords[i][0], coordinates_y=coords[i][1])


# create record in DB
def create(model, **kwargs):
    instance = model(**kwargs)
    session.add(instance)
    session.commit()
    return instance


def query(model, **kwargs):
    model = model
    q = session.query(model)
    for name, value in kwargs.items():
        q = q.filter(getattr(model, name) == value)
    return q


def all_records(model, **kwargs):
    q = query(model, **kwargs)
    return q


def one_record(model, **kwargs):
    q = query(model, **kwargs)
    return q.one_or_none()