from pydantic import BaseModel,Field
from typing import Dict

class DownloadHtmlModel(BaseModel):
    url:str
    path:str = Field(default="D:/Project/tests/")
    name:str
    chunk:int = 10
    kwargs:Dict[str,str]