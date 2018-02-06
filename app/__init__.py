from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import app_config

# db variable initialization
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(app_config['server'])
    app.config.from_pyfile('../config.py')
    db.app = app
    db.init_app(app)

    from app import models

    migrate = Migrate(app, db)
    
    from .views import views_blueprint
    app.register_blueprint(views_blueprint)

    return app
