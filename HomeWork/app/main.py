from typing import Union
import uvicorn
from fastapi import FastAPI
from api.downloadApi import downloadRouter
from api.analysisApi import analysisRouter
from api.searchApi import searchRouter

app = FastAPI()
app.include_router(downloadRouter)
app.include_router(analysisRouter)
app.include_router(searchRouter)

if __name__=="__main__":
    uvicorn.run(app="main:app",host = "0.0.0.0" ,port = 8080,reload = True)
    