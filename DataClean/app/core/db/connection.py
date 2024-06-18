import mysql.connector
from core.db.config import DBConfig
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

def getDbConnection():
    connection = mysql.connector.connect(
        host=DBConfig.HOST,
        port=DBConfig.PORT,
        user=DBConfig.USER,
        password=DBConfig.PWD,
        database=DBConfig.DATABASE
    )
    return connection

def getDb():
    # SQLAlchemy 数据库连接字符串
    SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{DBConfig.USER}:{DBConfig.PWD}@{DBConfig.HOST}:{DBConfig.PORT}/{DBConfig.DATABASE}"
    # 创建数据库引擎
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    # 创建会话类
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    return session
    