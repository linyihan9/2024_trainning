from utils.response import responseUtil,responseEnum
import os
import requests
from concurrent.futures import ThreadPoolExecutor,as_completed
from models.download.downloadDataModel import DownloadDataModel
from utils.downloadUtils import isValidPath,isValidUrl
from urllib.parse import urlencode
import zipfile

#多线程下载
def multiThreadDownloadZip(downloadDataModel:DownloadDataModel):
    fullUrl = downloadDataModel.url
    if downloadDataModel.kwargs:
        fullUrl+='?'
        for key,value in downloadDataModel.kwargs.items():
            fullUrl = fullUrl+key+'='+value
    try:
        res = requests.get(fullUrl,stream=True)
        filesize = int(res.headers['Content-Length'])
        divisional_ranges = calDivisionalRange(filesize)
        print(divisional_ranges)
        path = downloadDataModel.path+downloadDataModel.name
        # 先创建空文件
        with open(path, "wb"):
            pass
        with ThreadPoolExecutor() as p:
            futures = []
            for s_pos, e_pos in divisional_ranges:
                futures.append(p.submit(rangeDownload, path, s_pos, e_pos,fullUrl))
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

#检查输入的downloadDataModel是否规范
def isValidDownloadDataModel(downloadDataModel:DownloadDataModel):
    #判断路径是否符合规范，不符合则补默认的http://
    if isValidUrl(downloadDataModel.url) == False:
        return responseEnum.ResponseStatus.DOWNLOADURLERROR
    if isValidPath(downloadDataModel.path) == False:
        return responseEnum.ResponseStatus.DOWNLOADPATHERROR
    if not downloadDataModel.name:
        return responseEnum.ResponseStatus.DOWNLOADNAMEERROR
    return True

#解压
def unzip(zipFile,path):
    try:
        # 创建一个用于存放解压后文件的文件夹
        os.makedirs(path, exist_ok=True)
        with zipfile.ZipFile(zipFile,'r') as f:
            f.extractall(path)
        return responseEnum.ResponseStatus.SUCCESS
    except:
        return responseEnum.ResponseStatus.UNZIPERROR
