import os

class Config() :
    """
    Gereral configuration of the parent class
    """
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/{}?apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProConfig(Config) :
    """
    production configuration of child class 

    Args :
        config - the parent configuration class with  general configuration settings
    """
    pass

class DevConfig(Config) :
    """
    Development configuration of the parent class

    Args:
        Config - the parent configuration class with  general configuration settings
    """
    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProConfig
}



