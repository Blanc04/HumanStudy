from pydantic import BaseModel
from pydantic import BaseModel, Field
# from fastapi import Field

class Todo(BaseModel) :
    id:int
    item:str

class Todo2(BaseModel) :
    id:int = Field
    item:str = Field(min_length=2, max_length=20)
