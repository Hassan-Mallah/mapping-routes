from flask_app import create_app

app = create_app()

if __name__ == '__main__':
    import random
    # Threaded option to enable multiple instances for multiple user access support
    coords = [(float((random.random() * 180.0)) - 90, float((random.random() * 180.0)) - 180) for _ in range(2)]

    app.app_context().push()
    app.run(threaded=True, port=5000)