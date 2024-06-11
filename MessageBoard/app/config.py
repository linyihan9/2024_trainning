import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# base configuration
class Config:
    SECRET_KEY = os.environ.get('KEY') or '123456'
    # 数据库规则
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

# 开发环境
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@47.97.18.187:3306/test'

config = {
    "default": DevelopmentConfig
}