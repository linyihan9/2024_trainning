from pydantic import BaseModel,Field
from typing import Dict

class DownloadDataModel(BaseModel):
    url:str
    path:str = Field(default="/usr/data")
    name:str
    chunk:int = 10
    kwargs:Dict[str,str]