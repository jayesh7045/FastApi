from .dbConnect import Base
from pydantic import BaseModel
class Blog(BaseModel):
    title : str
    body : str 
    class config:
        orm_mode = True
    
    