from fastapi import HTTPException
from typing import Any, Dict

def create_response(code:int, message:str,data:Any) -> Dict[str, Any]:
    return {
        "code": code,
        "message": message,
        "data": data
    }