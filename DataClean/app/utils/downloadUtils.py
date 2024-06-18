import os
import urllib

def isValidPath(path):
    # 检查路径格式是否合法
    if not isinstance(path, str):
        return False
    # 检查路径是否存在，并且是一个目录
    if not os.path.exists(path):
        os.mkdir(path)
    # 如果是文件夹，则检查是否有写入权限
    if os.path.isdir(path):
        return os.access(path, os.W_OK)
    # 其他情况，默认返回False
    return True

def isValidUrl(url):
    try:
        result = urllib.parse.urlparse(url)
        if not all([result.scheme, result.netloc]):
            return False
    except Exception:
        return False