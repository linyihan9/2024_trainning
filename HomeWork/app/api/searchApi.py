from fastapi import APIRouter
from datetime import datetime
from utils.response.responseEnum import ResponseStatus
from utils.response.responseUtil import create_response
from core.search.search import searchDataPackage,searchByImagePath

searchRouter = APIRouter(prefix='/search')

@searchRouter.get('/searchDataPackageAPI')
def searchDataPackageAPI():
    start_time = datetime.now()
    res = searchDataPackage()
    end_time = datetime.now()
    return res

@searchRouter.get('/searchByImagePathAPI')
def searchByImagePathAPI(dataType:int,imagePathRouter):
    start_time = datetime.now()
    res = searchByImagePath(dataType,imagePathRouter)
    end_time = datetime.now()
    return res