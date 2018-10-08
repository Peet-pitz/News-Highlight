from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

#creating bootstrap instance
bootstrap = Bootstrap()

def create_app(config_name):
    #create flask app instance
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    # config_options[config_name].init__app(app)


    # initializing flask extention
    bootstrap.init_app(app)

    # registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting config
    from .requests import configure_request
    configure_request(app)


    return app
