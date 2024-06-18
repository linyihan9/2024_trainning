from fastapi import APIRouter,Depends
from core.analysis.analysis import analysisDataInfo
from utils.response.responseEnum import ResponseStatus
from utils.response.responseUtil import create_response
from datetime import datetime
from sqlalchemy.orm import Session
from core.db.connection import getDb

analysisRouter = APIRouter(prefix='/analysis')

@analysisRouter.get('/analysisDataInfoAPI')
def analysisDataInfoAPI(path,dataType):
    start_time = datetime.now()
    res = analysisDataInfo(path,dataType)
    end_time = datetime.now()
    if(res == ResponseStatus.SUCCESS):
        return create_response(res.getCode(),res.getMessage(),"解析完成，花费时间："+str(end_time-start_time))
    else:
        return create_response(res.getCode(),res.getMessage(),"解析失败")
