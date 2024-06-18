import pytest
from utils.response import responseEnum
from core.analysis.analysis import analysisDataInfo

def test_analysisDataInfo():
    assert analysisDataInfo('D://Project//MessageBoard//2024_trainning//DataClean//Data//single-vehicle-side-example//data_info.json',
                            'vehicleEnd3DInspection') == responseEnum.ResponseStatus.SUCCESS