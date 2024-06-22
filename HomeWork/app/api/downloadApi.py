from fastapi import APIRouter,Depends
from datetime import datetime
import core.download.html as html
import core.download.data as data
from utils.response.responseEnum import ResponseStatus
from utils.response.responseUtil import create_response
from models.download.downloadHtmlModel import DownloadHtmlModel
from models.download.downloadDataModel import DownloadDataModel
from core.db.connection import getDb
from mysql.connector import cursor

downloadRouter = APIRouter(prefix='/download')

@downloadRouter.get('/singleThreadDownloadHtmlAPI')
def singleThreadDownloadHtmlAPI(downloadHtmlModel:DownloadHtmlModel):
    """单线程下载Html

    Args:
        downloadHtmlModel (DownloadHtmlModel): 
            url: 网页地址
            path: 保存地址
            name: 保存名称
            chunk: 分片数量
            kwargs: 可以放例如请求头等信息
    """    
    start_time = datetime.now()
    res = html.singleThreadDownloadHtml(downloadHtmlModel)
    end_time = datetime.now()
    if(res == ResponseStatus.SUCCESS):
        return create_response(res.getCode(),res.getMessage(),"下载完成，花费时间："+str(end_time-start_time))
    else:
        return create_response(res.getCode(),res.getMessage(),"下载失败")

@downloadRouter.get('/singleThreadStreamDownloadHtmlAPI')
def singleThreadStreamDownloadHtmlAPI(downloadHtmlModel:DownloadHtmlModel):
    """单线程流式下载html

    Args:
        downloadHtmlModel (DownloadHtmlModel): 
            url: 网页地址
            path: 保存地址
            name: 保存名称
            chunk: 分片数量
            kwargs: 可以放例如请求头等信息
    """    
    start_time = datetime.now()
    res = html.singleThreadStreamDownloadHtml(downloadHtmlModel)
    end_time = datetime.now()
    if(res == ResponseStatus.SUCCESS):
        return create_response(res.getCode(),res.getMessage(),"下载完成，花费时间："+str(end_time-start_time))
    else:
        return create_response(res.getCode(),res.getMessage(),"下载失败")

@downloadRouter.get('/singleThreadPieceStreamDownloadHtmlAPI')
def singleThreadPieceStreamDownloadHtmlApi(downloadHtmlModel:DownloadHtmlModel):
    """单线程分片流式下载html

    Args:
        downloadHtmlModel (DownloadHtmlModel): 
            url: 网页地址
            path: 保存地址
            name: 保存名称
            chunk: 分片数量
            kwargs: 可以放例如请求头等信息
    """   
    start_time = datetime.now()
    res = html.singleThreadPieceStreamDownloadHtml(downloadHtmlModel)
    end_time = datetime.now()
    if(res == ResponseStatus.SUCCESS):
        return create_response(res.getCode(),res.getMessage(),"下载完成，花费时间："+str(end_time-start_time))
    else:
        return create_response(res.getCode(),res.getMessage(),"下载失败")

@downloadRouter.get('/multiThreadDownloadHtmlAPI')
def multiThreadDownloadHtmlAPI(downloadHtmlModel:DownloadHtmlModel):
    """多线程流式分片下载html

    Args:
        downloadHtmlModel (DownloadHtmlModel): 
            url: 网页地址
            path: 保存地址
            name: 保存名称
            chunk: 分片数量
            kwargs: 可以放例如请求头等信息
    """   
    start_time = datetime.now()
    res = html.multiThreadDownloadHtml(downloadHtmlModel)
    end_time = datetime.now()
    if(res == ResponseStatus.SUCCESS):
        return create_response(res.getCode(),res.getMessage(),"下载完成，花费时间："+str(end_time-start_time))
    else:
        return create_response(res.getCode(),res.getMessage(),"下载失败")   
    
#多线程下载Zip
@downloadRouter.get('/multiThreadDownloadZipAPI')
def multiThreadDownloadZipAPI(downloadDataModel:DownloadDataModel):
    """多线程分片流式下载Zip

    Args:
        downloadHtmlModel (DownloadHtmlModel): 
            url: 网页地址
            path: 保存地址
            name: 保存名称
            chunk: 分片数量
            kwargs: 可以放例如请求头等信息
    """   
    start_time = datetime.now()
    res = data.multiThreadDownloadZip(downloadDataModel)
    end_time = datetime.now()
    if(res == ResponseStatus.SUCCESS):
        return create_response(res.getCode(),res.getMessage(),"下载完成，花费时间："+str(end_time-start_time))
    else:
        return create_response(res.getCode(),res.getMessage(),"下载失败")   


#解压Zip
@downloadRouter.get('/unzipAPI')
def unzipAPI(zipFile,path):
    """解压

    Args:
        zipFile (_type_): 压缩文件路径
        path (_type_): 保存路径
    """    
    start_time = datetime.now()
    res = data.unzip(zipFile,path)
    end_time = datetime.now()
    if(res == ResponseStatus.SUCCESS):
        return create_response(res.getCode(),res.getMessage(),"下载完成，花费时间："+str(end_time-start_time))
    else:
        return create_response(res.getCode(),res.getMessage(),"下载失败")   


