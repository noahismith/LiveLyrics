from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import app_config

# db variable initialization
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(app_config['production'])
    app.config.from_pyfile('../config.py')
    db.app = app
    db.init_app(app)

    from app import models

    migrate = Migrate(app, db)
    
    from .views import views_blueprint
    app.register_blueprint(views_blueprint)

    from .usersBp import users_blueprint
    app.register_blueprint(users_blueprint, url_prefix="/users")

    from .lyricsBp import lyrics_blueprint
    app.register_blueprint(lyrics_blueprint, url_prefix="/lyrics")

    from .lyricratingBp import lyricrating_blueprint
    app.register_blueprint(lyricrating_blueprint, url_prefix="/lyricrating")

    return app
