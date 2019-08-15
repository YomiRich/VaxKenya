import os

class Config:
    pass

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://petermagecha:1234@localhost/vaxkenya'
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}            