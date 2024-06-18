from core.db.connection import getDb
from utils.response.responseEnum import ResponseStatus
from models.db.dataPackageModel import DataPackageModel
from models.db.vehicleEnd3DInspectionDBModel import VehicleEnd3DInspectionDBModel
from utils.response.responseUtil import create_response

def searchDataPackage():
    try:
        session = getDb()
        res = session.query(DataPackageModel).all()
    except:
        return create_response(ResponseStatus.DATABASEERROR.getCode(),ResponseStatus.DATABASEERROR.getMessage())
    return create_response(ResponseStatus.SUCCESS.getCode(),ResponseStatus.SUCCESS.getMessage(),res)


#TODO 可以加升降序等params
def searchByImagePath(dataType,imagePathRouter):
    try:
        session = getDb()
        #vehicleEnd3DInspection
        if dataType == 1:
            res = session.query(VehicleEnd3DInspectionDBModel).filter(VehicleEnd3DInspectionDBModel.imagePathRouter.ilike(f'%{imagePathRouter}%')).all()
            return create_response(ResponseStatus.SUCCESS.getCode(),ResponseStatus.SUCCESS.getMessage(),res)
    except:
        return create_response(ResponseStatus.DATABASEERROR.getCode(),ResponseStatus.DATABASEERROR.getMessage())
