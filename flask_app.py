from app import create_app

if __name__ == '__main__':
    app = create_app()
    # import os
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)