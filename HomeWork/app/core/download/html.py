import urllib.request
import utils.exception as Exception
from utils.response import responseEnum
import os
from models.download.downloadHtmlModel import DownloadHtmlModel
import requests
from concurrent.futures import ThreadPoolExecutor,as_completed
from utils.downloadUtils import isValidPath,isValidUrl

#单线程下载
def singleThreadDownloadHtml(downloadHtmlModel:DownloadHtmlModel):
    validResult = isValidDownloadHtmlModel(downloadHtmlModel)
    if validResult is not True:
        return validResult
    #获取html内容
    html = urllib.request.urlopen(downloadHtmlModel.url).read()
    try:
        path = downloadHtmlModel.path+downloadHtmlModel.name
        with open (path,"wb") as f:
    #   写文件用bytes而不是str，所以要转码  
            f.write(html)
    except Exception as e:
        return responseEnum.ResponseStatus.DOWNLOADSAVEERROR
    return responseEnum.ResponseStatus.SUCCESS

#单线程流式下载
def singleThreadStreamDownloadHtml(downloadHtmlModel:DownloadHtmlModel):
    validResult = isValidDownloadHtmlModel(downloadHtmlModel)
    if validResult is not True:
        return validResult
    #获取html内容
    try:
        path = downloadHtmlModel.path+downloadHtmlModel.name
        with open (path,"wb") as f,requests.get(downloadHtmlModel.url,stream=True)as res:
            for downloadHtmlModel.chunk in res.iter_content(chunk_size=64*1024):
                if not downloadHtmlModel.chunk:
                    break
                f.write(downloadHtmlModel.chunk)
    except Exception:
        return responseEnum.ResponseStatus.DOWNLOADSAVEERROR
    return responseEnum.ResponseStatus.SUCCESS

#TODO: 必须要Content_Length存在
#单线程分片流式下载
def singleThreadPieceStreamDownloadHtml(downloadHtmlModel:DownloadHtmlModel):
    validResult = isValidDownloadHtmlModel(downloadHtmlModel)
    if validResult is not True:
        return validResult
    try:
        path = downloadHtmlModel.path+downloadHtmlModel.name
        #创建空文件
        with open(path, "wb") as f:
            pass
        res = requests.head(downloadHtmlModel.url)
        filesize = int(res.headers['Content-Length'])
        divisional_ranges = calDivisionalRange(filesize)
        for s_pos, e_pos in divisional_ranges:
            rangeDownload(path, s_pos, e_pos,downloadHtmlModel.url)
    except Exception:
        return responseEnum.ResponseStatus.DOWNLOADSAVEERROR
    return responseEnum.ResponseStatus.SUCCESS


#多线程下载
def multiThreadDownloadHtml(downloadHtmlModel:DownloadHtmlModel):
    validResult = isValidDownloadHtmlModel(downloadHtmlModel)
    if validResult is not True:
        return validResult
    try:
        res = requests.head(downloadHtmlModel.url)
        filesize = int(res.headers['Content-Length'])
        divisional_ranges = calDivisionalRange(filesize)
        path = downloadHtmlModel.path+downloadHtmlModel.name
        # 先创建空文件
        with open(path, "wb") as f:
            pass
        with ThreadPoolExecutor() as p:
            futures = []
            for s_pos, e_pos in divisional_ranges:
                print(s_pos, e_pos)
                futures.append(p.submit(rangeDownload, path, s_pos, e_pos,downloadHtmlModel.url))
            # 等待所有任务执行完毕
            as_completed(futures)
    except Exception:
        return responseEnum.ResponseStatus.DOWNLOADSAVEERROR
    return responseEnum.ResponseStatus.SUCCESS

#计算分片大小
def calDivisionalRange(filesize, chuck=10):
    step = filesize//chuck
    arr = list(range(0, filesize, step))
    result = []
    for i in range(len(arr)-1):
        s_pos, e_pos = arr[i], arr[i+1]-1
        result.append([s_pos, e_pos])
    result[-1][-1] = filesize-1
    return result

#分片下载
def rangeDownload(save_name, s_pos, e_pos,url):
    headers = {"Range": f"bytes={s_pos}-{e_pos}"}
    res = requests.get(url, headers=headers, stream=True)
    with open(save_name, "rb+") as f:
        f.seek(s_pos)
        for chunk in res.iter_content(chunk_size=64*1024):
            if chunk:
                f.write(chunk)

#检查输入的downloadHtmlModel是否规范
def isValidDownloadHtmlModel(downloadHtmlModel:DownloadHtmlModel):
    #判断路径是否符合规范，不符合则补默认的http://
    if isValidUrl(downloadHtmlModel.url) == False:
        return responseEnum.ResponseStatus.DOWNLOADURLERROR
    if isValidPath(downloadHtmlModel.path) == False:
        return responseEnum.ResponseStatus.DOWNLOADPATHERROR
    if not downloadHtmlModel.name:
        return responseEnum.ResponseStatus.DOWNLOADNAMEERROR
    return True

def getHtml(url):
    html = urllib.request.urlopen(url).read()
    return html
