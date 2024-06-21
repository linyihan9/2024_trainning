import os
import utils.exception as Exception
from utils.response import responseEnum
import json
from core.analysis.vehicleEnd3DInspectionAnalysis import analysisEach as vehicleEnd3DInspectionAnalysisEach
from models.db.dataPackageModel import DataPackageModel
from core.db.connection import getDb,getDbEngine
from utils.analysisUtil import getJSON,calculateSha256Hash,inferTypeBySuf
from sqlalchemy import Column,Table,MetaData,Integer,String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def analysisDataInfo(path,dataType):
    if not os.path.exists(path):
        return responseEnum.ResponseStatus.ANALYSISPATHERROR
    try:
        with open(path,"r") as f:
            data = json.load(f)
            if dataType == 'vehicleEnd3DInspection':
                ans = vehicleEnd3DInspectionAnalysisEach(os.path.dirname(path),data)
                return ans
    except Exception:
        return responseEnum.ResponseStatus.ANALYSISERROR
    # return responseEnum.ResponseStatus.SUCCESS


#TODO 改html
#TODO 查询
#TODO json要保存写的内容，而不是路径
def analysisDataDiffTable(path,dataType):
    try:
        session = getDb()
    except:
        return responseEnum.ResponseStatus.DATABASEERROR
    dataPackageName = path.split('//')[-2]
    dataPackageHash = calculateSha256Hash(dataPackageName)
    #检测是否有重复hash值
    existData = session.query(DataPackageModel).filter_by(dataPackageHash=dataPackageHash).first()
    if existData:
        return responseEnum.ResponseStatus.INSERTREPEATERROR
    try:
        with open(path,'r') as f:
            data = json.load(f)
        #根据json中数据进行判断类型
    except:
        return responseEnum.ResponseStatus.ANALYSISERROR
    engine = getDbEngine()
    session = getDb()
    table = createTable(os.path.dirname(path),data,dataPackageName,engine)
    dataType = changeDataType(dataType)
    return insertData(dataPackageName,data,session,table,dataType)

#读取json，构建table，创建
def createTable(path,data,tableName,engine):
    columns = []
    addColumns = {}
    #读取json
    for item in data:
        for key in item:
            value = item[f'{key}'].split('.')[-1]
            type = inferTypeBySuf(value)
            column = Column(key,type)
            columns.append(column)
            if value == 'pcd':
                addColumns[key+'_size'] = Integer
        break
    #添加主键列
    appendPrimaryKeyColumn(columns)
    #添加额外列
    appendOtherColumn(addColumns,data,path,columns)
    table = createTableDetail(tableName,columns,engine)
    return table

def createTableDetail(tableName,columns,engine):
    metadata = MetaData()
    table = Table(tableName, metadata, *columns)
    metadata.create_all(engine)
    return table

# 动态创建 ORM 模型类
def createOrmClass(tableName, columns):
    attrs = {'__tablename__': tableName, '__table_args__': {'extend_existing': True}}
    for column in columns:
        attrs[column.name] = column
    return type(tableName, (Base,), attrs)

#添加主键列
def appendPrimaryKeyColumn(columns):
    column = Column('id',Integer,primary_key = True)
    columns.append(column)

#添加额外列
def appendOtherColumn(addColumns,data,path,columns):
    for key in addColumns:
        column = Column(key,addColumns[key])
        columns.append(column)
        if key.split('_')[-1] == 'size':
            appendPcdSizeColumn(data,path,key,'_'.join(key.split('_')[:-1]))

#二进制文件加一个文件大小列,并添加data
def appendPcdSizeColumn(data,path,key,keyDir):
    for item in data:
        item[key] = os.path.getsize(path+'//'+item[keyDir])

#转换dataType
def changeDataType(dataType):
    if(dataType == 'vehicleEnd3DInspection'):
        return 1
    else:
        return responseEnum.ResponseStatus.ANALYSISTYPEERROR

#插入数据
def insertData(dataPackageName,data,session,table,dataType):
    try:
        session.execute(
            f"INSERT INTO data_package (data_package_name, data_package_hash, data_type) VALUES ('{dataPackageName}', '{calculateSha256Hash(dataPackageName)}', '{dataType}');")
        #向数据表添加数据
        for record in data:
            # 使用 table.insert().values(**record) 创建插入语句对象
            insert_stmt = table.insert().values(**record)
            # 执行插入操作
            session.execute(insert_stmt)
        # 提交事务
        session.commit()
    except:
        session.rollback()
        return responseEnum.ResponseStatus.DATABASEERROR
    return responseEnum.ResponseStatus.SUCCESS


    
