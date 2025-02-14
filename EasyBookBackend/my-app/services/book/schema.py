import re
import datetime
from pydantic.main import BaseModel
from typing import Optional

class BookRequest(BaseModel):
    ID:int
    RID: int
    Name: str
    Phone: str
    Reason: str
    ReTime:datetime.datetime 
    Person: int  

class CancelRequest(BaseModel):
    ID:int
    RID: int
    ReNumber:int

