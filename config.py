#!/usr/bin/env python

import os 

class Config:
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'ccxcxx'
#    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class DevelopmentConfig(Config):
    DEBUG = True
#    SQLALCHEMY_DATABASE_URI = 'ccxcxx'

class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
#    SQLALCHEMY_DATABASE_URI = os.getenv('SECRET_KEY')

class ProductionConfig(Config):
    FLASK_ENV = 'production'
#    SQLALCHEMY_DATABASE_URI = os.getenv('SECRET_KEY')
