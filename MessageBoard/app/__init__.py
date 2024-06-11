from flask import Flask
from app.api import config_blueprint
from app.extension import config_extensions

def create_app(DevelopmentConfig):
   
    # 实例化 app
    app = Flask(__name__)

    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@47.97.18.187:3306/test'
    # 加载配置项
    app.config.setdefault('SQLALCHEMY_DATABASE_URI','mysql://root:123456@47.97.18.187:3306/test')
    # app.config.from_object(DevelopmentConfig)

    # 加载拓展
    config_extensions(app)

    # 加载蓝图
    config_blueprint(app)
    return app