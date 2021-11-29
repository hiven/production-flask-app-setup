import os
from flask import Flask, render_template
from config import Config  # NEW!!!!!


### Application Factory ###
def create_app():

    app = Flask(__name__)

    # Configure the flask app instance
    CONFIG_TYPE = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(CONFIG_TYPE)

    from app.main import main_blueprint

    app.register_blueprint(main_blueprint)

    return app
