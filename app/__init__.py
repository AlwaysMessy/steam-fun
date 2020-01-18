import os
from flask import Flask
from setting import config
from extensions import db
from app.blueprints.web import web

def create_app(config_name=None):
    if config_name is None:
        #如果没有传入配置名，就从FLASK_CONFIG环境变量获取，如果没有获取到则使用默认值development
        config_name = os.getenv('FLASK_CONFIG', 'development')

        app = Flask('wsgi')
        app.config.from_object(config[config_name])

        db.init_app(app)

        app.register_blueprint(web)

        return app