import os
class Config:
    '''
    General configuration parent class
    '''
    

class ProdConfig(Config):
    '''
    Production config child class
    '''

class TestConfig(Config):
    '''
    Test config child class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:123456@localhost/pitch_test'

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}