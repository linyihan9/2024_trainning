from enum import Enum

class ResponseStatus(Enum):
    SUCCESS = (200, "Success")

    DATABASEERROR = (301,"DatabaseError")

    DOWNLOADERROR = (401,"DownloadError")
    DOWNLOADURLERROR = (402,"DownloadUrlError")
    DOWNLOADSAVEERROR = (403,"DownloadSaveError")
    DOWNLOADPATHERROR = (404,"DownloadPathError")
    DOWNLOADNAMEERROR = (405,"DownloadNameError")

    ANALYSISPATHERROR = (501,"AnalysisPathError")
    ANALYSISERROR = (502,"AnalysisError")
    ANALYSISTYPEERROR = (503,"AnalysisTypeError")

    INSERTREPEATERROR = (601,"InsertRepeatError")

    UNZIPERROR = (701,"UnzipError")



    def __init__(self, code, message):
        self.code = code
        self.message = message
    
    def getCode(self):
        return self.code
    
    def getMessage(self):
        return self.message