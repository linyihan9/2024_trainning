from fastapi import APIRouter
from datetime import datetime
from utils.response.responseEnum import ResponseStatus
from utils.response.responseUtil import create_response
from core.search.search import searchDataPackage,searchByImagePath,searchAllByDataPackage,searchTypeRangeTime

searchRouter = APIRouter(prefix='/search')

#查询所有数据包
@searchRouter.get('/searchDataPackageAPI')
def searchDataPackageAPI():
    start_time = datetime.now()
    res = searchDataPackage()
    end_time = datetime.now()
    return res

#通过image文件名查询数据
@searchRouter.get('/searchByImagePathAPI')
def searchByImagePathAPI(dataType:int,imagePathRouter):
    start_time = datetime.now()
    res = searchByImagePath(dataType,imagePathRouter)
    end_time = datetime.now()
    return res

#查询某数据包下所有数据
@searchRouter.get('/searchAllFromDataPackageAPI')
def searchAllByDataPackageAPI(dataPackageName):
    start_time = datetime.now()
    res = searchAllByDataPackage(dataPackageName)
    end_time = datetime.now()
    return res

#查询同类型数据的所有数据包下数据（选择一个时间范围）
@searchRouter.get('/searchTypeRangeTimeAPI')
def searchTypeRangeTimeAPI(dataType,startTime,endTime):
    start_time = datetime.now()
    res = searchTypeRangeTime(dataType,startTime,endTime)
    end_time = datetime.now()
    return res