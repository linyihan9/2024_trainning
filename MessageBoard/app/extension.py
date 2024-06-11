from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

# 初始化拓展
def config_extensions(app):
    db.init_app(app)

    login_manager.init_app(app)
