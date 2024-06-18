from sqlalchemy import Column, String,DateTime,Integer,JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class VehicleEnd3DInspectionDBModel(Base):
    __tablename__ = 'vehicle_end_3D_inspection'

    id = Column("id",Integer, primary_key=True,index=True)
    dataPackageId = Column("data_package_id",Integer)
    imagePathRouter = Column("image_path_router",String(100))
    imagePathHttp = Column("image_path_http",String(100))
    imagePathTimestamp = Column("image_path_timestamp",DateTime)
    pointcloudRouter = Column("pointcloud_router",String(100))
    pointcloudTimestamp = Column("pointcloud_timestamp",DateTime)
    pointcloudSize = Column("pointcloud_size",Integer)
    calibCameraIntrinsicPath = Column("calib_camera_intrinsic_path",JSON)
    calibLidarToCameraPath = Column("calib_lidar_to_camera_path",JSON)
    labelCameraStdPath = Column("label_camera_std_path",JSON)
    labelLidarStdPath = Column("label_lidar_std_path",JSON)