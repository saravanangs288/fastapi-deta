from pydantic import BaseModel

class Todo(BaseModel):
    heading:str
    description:str 