import os
class Config:
    '''
    General configuration parent class
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:123456@localhost/pitch'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
class ProdConfig(Config):
    '''
    Production config child class
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

# class TestConfig(Config):
#     '''
#     Test config child class
#     '''
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:123456@localhost/pitch_test'

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}