from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class DBConfig:
    HOST = "47.97.18.187"
    PORT = 3306
    USER = "root"
    PWD = "123456"
    DATABASE = "data_clean"

# SQLAlchemy 数据库连接字符串
SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{DBConfig.USER}:{DBConfig.PWD}@{DBConfig.HOST}:{DBConfig.PORT}/{DBConfig.DATABASE}"
# 创建数据库引擎
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 创建基类
Base = declarative_base()

# 定义数据模型类
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))

Base.metadata.create_all(engine)

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()

# 创建新学生
new_student = Student(name='aaa')
session.add(new_student)

# 提交事务
session.commit()

students = session.query(Student).all()

for student in students:
    print(f'ID: {student.id}, Name: {student.name}')

student = session.query(Student).filter_by(name='aaa').first()

student.name = 'bbb'

# 提交事务
session.commit()

student = session.query(Student).filter_by(name='bbb').first()

session.delete(student)


session.commit()