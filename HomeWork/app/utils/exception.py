class AppError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class DownloadError(AppError):
    pass

class DownloadSaveError(AppError):
    pass

class DownloadUrlError(AppError):
    pass

class AnalysisPathError(AppError):
    pass