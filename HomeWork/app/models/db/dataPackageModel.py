from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DataPackageModel(Base):
    __tablename__ = "data_package"

    dataPackageId = Column("data_package_id",Integer,primary_key=True)
    dataPackageName = Column("data_package_name",String(50))
    dataPackageHash = Column("data_package_hash",String(64))
    dataType = Column("data_type",Integer)