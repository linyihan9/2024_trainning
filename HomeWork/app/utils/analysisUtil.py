import json
from utils.response import responseEnum
import hashlib
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime, MetaData, Table,Text,JSON,BigInteger

#获取Json
def getJSON(path):
    try:
        with open(path,'r') as f:
            data = json.load(f)
            return data
    except Exception:
        return responseEnum.ResponseStatus.ANALYSISERROR

#计算Hash值
def calculateSha256Hash(input_string: str) -> str:
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()

#转换时间为timestamp
def convertMicrosecondsToDatetime(microsecondsTimestamp: int) -> datetime:
    # 将微秒时间戳转换为秒时间戳
    secondsTimestamp = microsecondsTimestamp / 1_000_000
    dtObject = datetime.fromtimestamp(secondsTimestamp)
    return dtObject

#根据值判断类型
def inferTypeByValue(value):
    if isinstance(value, int):
        return Integer
    elif isinstance(value, float):
        return Float
    elif isinstance(value, bool):
        return Boolean
    elif isinstance(value, str):
        if len(value) < 100:
            return String(100)
        elif len(value) >= 100 and len(value) < 255:
            return String(255)
        else:
            return Text
    elif isinstance(value, datetime.date):
        return DateTime
    else:
        return String(255)
    
#根据后缀判断类型
def inferTypeBySuf(value):
    if value == 'jpg' or value == 'pcd':
        return String(100)
    elif value == 'json':
        return JSON
    elif value.isdigit():
        num = int(value)
        if num >= -2147483648 and num <= 2147483647:
            return Integer
        else:
            return BigInteger
    else:
        return String(255)