from pydantic import BaseModel, Field

class Error(BaseModel):
    detail: str
    status: int
    title: str
    type: str 