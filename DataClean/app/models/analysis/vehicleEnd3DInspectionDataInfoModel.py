from datetime import datetime
import json
from models.analysis.dataInfoModel import DataInfoModel

class VehicleEnd3DInspectionDataInfoModel(DataInfoModel):
    id:int
    dataName:str
    dataNameHash:str
    imagePathRouter:str
    imagePathTimestamp:str
    pointcloudRouter:str
    pointcloudTimestamp:datetime
    pointcloudSize:int
    calibCameraIntrinsicPath:json
    calibLidarToCameraPath:json
    labelCameraStdPath:json
    labelLidarStdPath:json