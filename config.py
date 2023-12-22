import os 

class Config:
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'ccxcxx'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    FLASK_ENV = 'production'
