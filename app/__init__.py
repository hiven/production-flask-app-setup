import os
from flask import Flask, render_template
from config import Config

def create_app():

    app = Flask(__name__)
    app.config.from_object(config.DevelopmentConfig)

    from app.main import main_blueprint

    app.register_blueprint(main_blueprint)

    return app
