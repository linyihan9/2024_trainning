import pytest
from utils.response import responseEnum
from core.analysis.vehicleEnd3DInspectionAnalysis import analysisEach,getJSON,calculateSha256Hash,convertMicrosecondsToDatetime
from datetime import datetime


def test_analysisEach():
    data =  [
                {
                    "image_path": "image/000000.jpg",
                    "image_timestamp": "1604988999001000",
                    "pointcloud_path": "velodyne/000000.pcd",
                    "point_cloud_stamp": "1604988999006000",
                    "calib_camera_intrinsic_path": "calib/camera_intrinsic/000000.json",
                    "calib_lidar_to_camera_path": "calib/lidar_to_camera/000000.json",
                    "label_camera_std_path": "label/camera/000000.json",
                    "label_lidar_std_path": "label/lidar/000000.json"
                },
                {
                    "image_path": "image/000001.jpg",
                    "image_timestamp": "1604989000204000",
                    "pointcloud_path": "velodyne/000001.pcd",
                    "point_cloud_stamp": "1604989000206000",
                    "calib_camera_intrinsic_path": "calib/camera_intrinsic/000001.json",
                    "calib_lidar_to_camera_path": "calib/lidar_to_camera/000001.json",
                    "label_camera_std_path": "label/camera/000001.json",
                    "label_lidar_std_path": "label/lidar/000001.json"
                }
            ]
    path = 'D://Project//MessageBoard//2024_trainning//DataClean//Data//single-vehicle-side-example'
    assert analysisEach(path,data) == responseEnum.ResponseStatus.SUCCESS


def test_getJSON():
    data =  [
                {
                    "image_path": "image/000000.jpg",
                    "image_timestamp": "1604988999001000",
                    "pointcloud_path": "velodyne/000000.pcd",
                    "point_cloud_stamp": "1604988999006000",
                    "calib_camera_intrinsic_path": "calib/camera_intrinsic/000000.json",
                    "calib_lidar_to_camera_path": "calib/lidar_to_camera/000000.json",
                    "label_camera_std_path": "label/camera/000000.json",
                    "label_lidar_std_path": "label/lidar/000000.json"
                },
                {
                    "image_path": "image/000001.jpg",
                    "image_timestamp": "1604989000204000",
                    "pointcloud_path": "velodyne/000001.pcd",
                    "point_cloud_stamp": "1604989000206000",
                    "calib_camera_intrinsic_path": "calib/camera_intrinsic/000001.json",
                    "calib_lidar_to_camera_path": "calib/lidar_to_camera/000001.json",
                    "label_camera_std_path": "label/camera/000001.json",
                    "label_lidar_std_path": "label/lidar/000001.json"
                }
            ]
    path = 'D://Project//tests//tests.json'
    assert getJSON(path) == data


def test_calculateSha256Hash():
    assert calculateSha256Hash('"hello world"') == 'a948904f2f0f479b8f8197694b30184b0d2e42a27b6f8fd474e330d6f43952a3'

def test_convertMicrosecondsToDatetime():
    assert convertMicrosecondsToDatetime(1672531200000000) == datetime(2021,1,1,0,0,0)#2023-01-01 00:00:00