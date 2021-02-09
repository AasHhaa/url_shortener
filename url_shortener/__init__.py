import time
from flask import Flask
from .extensions import db
from .routers import short


def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    app.register_blueprint(short)
    create_all_tables(app=app)

    return app


def create_all_tables(app):
    db_status = False
    while not db_status:
        try:
            db.create_all(app=app)
            db_status = True
        except:
            print("The database system is starting up")
            time.sleep(5)
