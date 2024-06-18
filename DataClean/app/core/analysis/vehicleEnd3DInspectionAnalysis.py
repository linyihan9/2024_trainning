import os
from models.db.vehicleEnd3DInspectionDBModel import VehicleEnd3DInspectionDBModel
from models.db.dataPackageModel import DataPackageModel
from core.db.connection import getDb
import json
import utils.exception as Exception
from utils.response import responseEnum
import hashlib
from datetime import datetime
from utils.serverConfig import ServerConfig

#单线程添加example文件需要8s左右
#TODO 多线程
#地址需要修改成html形式
def analysisEach(path,data):
    try:
        session = getDb()
    except:
        return responseEnum.ResponseStatus.DATABASEERROR
    dataPackageName = path.split('//')[-1]
    dataPackageHash = calculateSha256Hash(dataPackageName)
    #检测是否有重复hash值
    existData = session.query(DataPackageModel).filter_by(dataPackageHash=dataPackageHash).first()
    if existData:
        return responseEnum.ResponseStatus.INSERTREPEATERROR
    newDataPackage = DataPackageModel(dataPackageName=dataPackageName,
                                      dataPackageHash=dataPackageHash,
                                      dataType=1)
    session.add(newDataPackage)
    session.flush()
    dataPackageId = newDataPackage.dataPackageId
    htmlPrefix = ServerConfig.HOST+':'+ServerConfig.TOMCATPORT+'/'+ dataPackageName+'/'
    #TODO 这里读数据可以多线程，就是不知道能快多少，大部分时间应该还是数据库
    for item in data:
        imagePathRouter=htmlPrefix+item['image_path']
        imagePathTimestamp = convertMicrosecondsToDatetime(int(item['image_timestamp']))
        pointcloudRouter=htmlPrefix+item['pointcloud_path']
        pointcloudTimestamp = convertMicrosecondsToDatetime(int(item['point_cloud_stamp']))
        pointcloudSize = os.path.getsize(path+"//"+item['pointcloud_path'])
        calibCameraPath =path+"//"+item['calib_camera_intrinsic_path']
        calibCameraJSON = getJSON(calibCameraPath)
        calibLidarPath = path+"//"+item['calib_lidar_to_camera_path']
        calibLidarJSON = getJSON(calibLidarPath)
        labelCameraPath = path+"//"+item['label_camera_std_path']
        labelCameraJSON = getJSON(labelCameraPath)
        labelLidarPath = path+"//"+item['label_lidar_std_path']
        labelLidarJSON = getJSON(labelLidarPath)

        #事务性
        if calibCameraJSON != responseEnum.ResponseStatus.ANALYSISERROR and calibLidarJSON != responseEnum.ResponseStatus.ANALYSISERROR and labelCameraJSON != responseEnum.ResponseStatus.ANALYSISERROR and labelLidarJSON != responseEnum.ResponseStatus.ANALYSISERROR:
            newVehicle = VehicleEnd3DInspectionDBModel(dataPackageId=dataPackageId,
                                                            imagePathRouter=imagePathRouter,
                                                            imagePathTimestamp=imagePathTimestamp,
                                                            pointcloudRouter=pointcloudRouter,
                                                            pointcloudTimestamp=pointcloudTimestamp,
                                                            pointcloudSize=pointcloudSize,
                                                            calibCameraIntrinsicPath=calibCameraJSON,
                                                            calibLidarToCameraPath=calibLidarJSON,
                                                            labelCameraStdPath=labelCameraJSON,
                                                            labelLidarStdPath=labelLidarJSON)
            session.add(newVehicle)
        else:
            return responseEnum.ResponseStatus.ANALYSISPATHERROR
    try:
        session.commit()
        return responseEnum.ResponseStatus.SUCCESS
    except Exception:
        session.rollback()
        return responseEnum.ResponseStatus.ANALYSISERROR

def getJSON(path):
    try:
        with open(path,'r') as f:
            data = json.load(f)
            return data
    except Exception:
        return responseEnum.ResponseStatus.ANALYSISERROR

#计算Hash值
def calculateSha256Hash(input_string: str) -> str:
    # 创建一个 sha256 哈希对象
    sha256_hash = hashlib.sha256()
    # 将输入字符串编码为字节并更新哈希对象
    sha256_hash.update(input_string.encode('utf-8'))
    # 返回十六进制的哈希值
    return sha256_hash.hexdigest()

#转换时间为timestamp
def convertMicrosecondsToDatetime(microsecondsTimestamp: int) -> datetime:
    # 将微秒时间戳转换为秒时间戳
    secondsTimestamp = microsecondsTimestamp / 1_000_000
    # 创建 datetime 对象
    dtObject = datetime.fromtimestamp(secondsTimestamp)
    return dtObject