import os
from models.db.vehicleEnd3DInspectionDBModel import VehicleEnd3DInspectionDBModel
from models.db.dataPackageModel import DataPackageModel
from core.db.connection import getDb
import utils.exception as Exception
from utils.response import responseEnum
from utils.serverConfig import ServerConfig
from utils.analysisUtil import getJSON,calculateSha256Hash,convertMicrosecondsToDatetime
from concurrent.futures import ThreadPoolExecutor,as_completed

#单线程添加example文件需要8s左右
#多线程
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
    #这里读数据可以多线程，就是不知道能快多少，大部分时间应该还是数据库
    with ThreadPoolExecutor() as p:
        futures = []
        for item in data:
            futures.append(p.submit(addDataDetailToSession,htmlPrefix,item,path,dataPackageId,session))
        as_completed(futures)
    try:
        session.commit()
        return responseEnum.ResponseStatus.SUCCESS
    except Exception:
        session.rollback()
        return responseEnum.ResponseStatus.ANALYSISERROR
    
def addDataDetailToSession(htmlPrefix,item,path,dataPackageId,session):
    imagePathRouter=htmlPrefix+item['image_path']
    imagePathTimestamp = convertMicrosecondsToDatetime(int(item['image_timestamp']))
    pointcloudRouter=htmlPrefix+item['pointcloud_path']
    pointcloudTimestamp = convertMicrosecondsToDatetime(int(item['point_cloud_stamp']))
    pointcloudSize = os.path.getsize(path+"//"+item['pointcloud_path'])
    getJsonPath = []
    calibCameraPath =path+"//"+item['calib_camera_intrinsic_path']
    getJsonPath.append(calibCameraPath)
    calibLidarPath = path+"//"+item['calib_lidar_to_camera_path']
    getJsonPath.append(calibLidarPath)
    labelCameraPath = path+"//"+item['label_camera_std_path']
    getJsonPath.append(labelCameraPath)
    labelLidarPath = path+"//"+item['label_lidar_std_path']
    getJsonPath.append(labelLidarPath)
    anses = {}
    with ThreadPoolExecutor() as p:
        futures = []
        for jsonPath in getJsonPath:
            ans = p.submit(getJSON,jsonPath)
            anses[jsonPath.split('/')[-2]] = ans.result()
            futures.append(ans)
        as_completed(futures)

    #事务性
    if all(value != responseEnum.ResponseStatus.ANALYSISERROR for value in anses.values()):
        newVehicle = VehicleEnd3DInspectionDBModel(dataPackageId=dataPackageId,
                                                    imagePathRouter=imagePathRouter,
                                                    imagePathTimestamp=imagePathTimestamp,
                                                    pointcloudRouter=pointcloudRouter,
                                                    pointcloudTimestamp=pointcloudTimestamp,
                                                    pointcloudSize=pointcloudSize,
                                                    calibCameraIntrinsicPath=anses['camera_intrinsic'],
                                                    calibLidarToCameraPath=anses['lidar_to_camera'],
                                                    labelCameraStdPath=anses['camera'],
                                                    labelLidarStdPath=anses['lidar'])
        session.add(newVehicle)
    else:
        return responseEnum.ResponseStatus.ANALYSISPATHERROR
    