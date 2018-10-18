from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

#creating bootstrap instance c

bootstrap = Bootstrap() c

def create_app(config_name):
    
    #create flask app instance c
    
    app = Flask(__name__)

    # Creating the app configurations c
    app.config.from_object(config_options[config_name])
    # config_options[config_name].init__app(app) c


    # initializing flask extention c
    bootstrap.init_app(app)

    # registering the blueprint c
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting config c
    from .requests import configure_request
    configure_request(app)


    return app
