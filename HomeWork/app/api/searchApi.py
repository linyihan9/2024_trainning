from fastapi import APIRouter
from datetime import datetime
from utils.response.responseEnum import ResponseStatus
from utils.response.responseUtil import create_response
from core.search.search import searchDataPackage,searchByImagePath,searchAllByDataPackage,searchTypeRangeTime

searchRouter = APIRouter(prefix='/search')

@searchRouter.get('/searchDataPackageAPI')
def searchDataPackageAPI():
    """从主表查询所有数据包
    """    
    start_time = datetime.now()
    res = searchDataPackage()
    end_time = datetime.now()
    return res

@searchRouter.get('/searchByImagePathAPI')
def searchByImagePathAPI(dataType:int,imagePathRouter):
    """PlanA中的:通过image文件名查询数据

    Args:
        dataType (int): 数据类型
        imagePathRouter (_type_): image文件名
    """    
    start_time = datetime.now()
    res = searchByImagePath(dataType,imagePathRouter)
    end_time = datetime.now()
    return res

@searchRouter.get('/searchAllFromDataPackageAPI')
def searchAllByDataPackageAPI(dataPackageName):
    """PlanB中的:查询某数据包下所有数据

    Args:
        dataPackageName (_type_): 数据包名称
    """    
    start_time = datetime.now()
    res = searchAllByDataPackage(dataPackageName)
    end_time = datetime.now()
    return res

@searchRouter.get('/searchTypeRangeTimeAPI')
def searchTypeRangeTimeAPI(dataType,startTime,endTime):
    """PlanB中的:查询同类型数据的所有数据包下数据（选择一个时间范围）

    Args:
        dataType (_type_): 数据类型
        startTime (_type_): 开始时间
        endTime (_type_): 结束时间
    """    
    start_time = datetime.now()
    res = searchTypeRangeTime(dataType,startTime,endTime)
    end_time = datetime.now()
    return res