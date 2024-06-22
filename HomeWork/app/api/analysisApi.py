from fastapi import APIRouter,Depends
from core.analysis.analysis import analysisDataInfo,analysisDataDiffTable
from utils.response.responseEnum import ResponseStatus
from utils.response.responseUtil import create_response
from datetime import datetime
from sqlalchemy.orm import Session
from core.db.connection import getDb

analysisRouter = APIRouter(prefix='/analysis')


@analysisRouter.get('/analysisDataInfoAPI')
def analysisDataInfoAPI(path,dataType):
    """PlanA:做了数据的规定,例如规定了vehicleEnd3DInspection数据类型的字段包含calibCameraIntrinsicPath等,需要按照模板
              进行上传，相同数据类型放在一类表中
    通过解析dataInfo文件,对整体进行解析并保存至数据库

    Args:
        path (_type_): dataInfo文件路径
        dataType (_type_): 数据类型：
            vehicleEnd3DInspection ———— 1
    """    
    start_time = datetime.now()
    res = analysisDataInfo(path,dataType)
    end_time = datetime.now()
    if(res == ResponseStatus.SUCCESS):
        return create_response(res.getCode(),res.getMessage(),"解析完成，花费时间："+str(end_time-start_time))
    else:
        return create_response(res.getCode(),res.getMessage(),"解析失败")
    
@analysisRouter.get('/analysisDataDiffTableAPI')
def analysisDataDiffTableAPI(path,dataType):
    """PlanB:一个数据包一张表，无需按照模板上传
    通过解析dataInfo文件,对整体进行解析并保存至数据库
    Args:
        path (_type_): dataInfo文件路径
        dataType (_type_): 数据类型
    """    
    start_time = datetime.now()
    res = analysisDataDiffTable(path,dataType)
    end_time = datetime.now()
    if(res == ResponseStatus.SUCCESS):
        return create_response(res.getCode(),res.getMessage(),"解析完成，花费时间："+str(end_time-start_time))
    else:
        return create_response(res.getCode(),res.getMessage(),"解析失败")
