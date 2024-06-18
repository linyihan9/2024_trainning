import os
import utils.exception as Exception
from utils.response import responseEnum
import json
from core.analysis.vehicleEnd3DInspectionAnalysis import analysisEach as vehicleEnd3DInspectionAnalysisEach


def analysisDataInfo(path,dataType):
    if not os.path.exists(path):
        return responseEnum.ResponseStatus.ANALYSISPATHERROR
    try:
        with open(path,"r") as f:
            data = json.load(f)
            if dataType == 'vehicleEnd3DInspection':
                ans = vehicleEnd3DInspectionAnalysisEach(os.path.dirname(path),data)
                return ans
    except Exception:
        return responseEnum.ResponseStatus.ANALYSISERROR
    # return responseEnum.ResponseStatus.SUCCESS
