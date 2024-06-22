from core.db.connection import getDb
from utils.response.responseEnum import ResponseStatus
from models.db.dataPackageModel import DataPackageModel
from models.db.vehicleEnd3DInspectionDBModel import VehicleEnd3DInspectionDBModel
from utils.response.responseUtil import create_response
from core.db.config import DBConfig
from concurrent.futures import ThreadPoolExecutor,as_completed

def searchDataPackage():
    try:
        session = getDb()
        res = session.query(DataPackageModel).all()
    except:
        return create_response(ResponseStatus.DATABASEERROR.getCode(),ResponseStatus.DATABASEERROR.getMessage())
    return create_response(ResponseStatus.SUCCESS.getCode(),ResponseStatus.SUCCESS.getMessage(),res)


#TODO 可以加升降序等params
def searchByImagePath(dataType,imagePathRouter):
    try:
        session = getDb()
        #vehicleEnd3DInspection
        if dataType == 1:
            res = session.query(VehicleEnd3DInspectionDBModel).filter(VehicleEnd3DInspectionDBModel.imagePathRouter.ilike(f'%{imagePathRouter}%')).all()
            return create_response(ResponseStatus.SUCCESS.getCode(),ResponseStatus.SUCCESS.getMessage(),res)
    except:
        return create_response(ResponseStatus.DATABASEERROR.getCode(),ResponseStatus.DATABASEERROR.getMessage())
    

def searchAllByDataPackage(dataPackageName):
    try:
        session = getDb()
        res = session.execute(f'select * from `{dataPackageName}`').all()
        return create_response(ResponseStatus.SUCCESS.getCode(),ResponseStatus.SUCCESS.getMessage(),res)
    except:
        return create_response(ResponseStatus.DATABASEERROR.getCode(),ResponseStatus.DATABASEERROR.getMessage())
    
def searchTypeRangeTime(dataType,startTime,endTime):
    try:
        #1.去主表查询所有该类型包
        session = getDb()
        items = session.execute(f'select data_package_name from `{DBConfig.MAINTABLE}` where data_type = {dataType}').all()
        #2.多线程去获取这些包
        reses = []
        with ThreadPoolExecutor() as p:
            futures = []
            for item in items:
                futures.append(p.submit(getPackageRangeTime, item[0],startTime,endTime,reses))
            # 等待所有任务执行完毕
            as_completed(futures)
        #3.做整合
        return 
    except:
        return create_response(ResponseStatus.DATABASEERROR.getCode(),ResponseStatus.DATABASEERROR.getMessage(),"")

def getPackageRangeTime(packageName,startTime,endTime,reses):
    session = getDb()
    res = session.execute(f'select * from `{packageName}` where image_timestamp >= {startTime} and image_timestamp <= {endTime}').all()
    reses.append(res)
    
