from pydantic import BaseModel

class Result(BaseModel):
    Data: dict
    rDesc: str
    rCode: str


class Result1(BaseModel):
    Data: list
    rDesc: str
    rCode: str