import logging
import pathlib
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config import Config
cur_path = os.path.dirname(__file__)
log_path = os.path.relpath("app.log", cur_path)

def create_app_db():
    app = Flask(__name__)
    app.config.from_object(Config)
    db = SQLAlchemy()
    data_base_URI = "{connectorname}://{username}:{password}@{hostname}/{databasename}".format(
            connectorname="mariadb+mariadbconnector",
            username="root",
            password="pesk-2020",
            hostname="127.0.0.1:3306",
            databasename="time_managment_web_app",
            )
    app.config['SQLALCHEMY_DATABASE_URI'] = data_base_URI
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()

    @app.before_first_request
    def create_database():
        with app.app_context():
            db.create_all()

    db.init_app(app)
    return app, db



app, db = create_app_db()

from app.main_bp.views import main
app.register_blueprint(main)
