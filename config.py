import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://amandine:pass@localhost/pitch'

class ProdConfig(Config):
    '''
    Production configuration
    Args:
        Config: the parent configuration class
    '''

    pass

class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config: the parent configuration class
    '''

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production' :ProdConfig
}

