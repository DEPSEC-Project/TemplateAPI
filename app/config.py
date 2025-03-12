import os
from dotenv import load_dotenv
load_dotenv("../.env")

class Config: # config par défaut
    SECRET_KEY = os.getenv('SECRET_KEY', 'password')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://admdev:password@localhost:5432/basepardefaut')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'enormemotdepasse')
    PERMANENT_SESSION_LIFETIME = os.getenv("PERMANENT_SESSION_LIFETIME",3600)

class DevelopmentConfig(Config): 
    FLASK_ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL', 'postgresql://user:password@db:5432/basededev')
    PERMANENT_SESSION_LIFETIME = 36000 # 10h pour la duree de la session

class TestingConfig(Config):
    FLASK_ENV = 'testing'
    TESTING = True
    PERMANENT_SESSION_LIFETIME = 1800# 30min pour la duree de la session
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL', 'postgresql://user:password@db:5432/basedeprod')

class ProductionConfig(Config):
    FLASK_ENV = 'production'
    PERMANENT_SESSION_LIFETIME = 300 # 5 minutes pour la duree de la session
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URL', 'postgresql://user:password@db:5432/basedeprod')

config = { #dictionnaire des confs
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
