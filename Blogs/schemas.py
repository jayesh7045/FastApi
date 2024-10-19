# Pydantic Schemas

from pydantic import BaseModel
from typing import List
class User(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

class Blog(BaseModel):
    id: int
    title: str
    body: str
    user_id: int

    class Config:
        orm_mode = True


class UserBlog(User):
    blogs : List[Blog]
    class Config():
        orm_mode = True
    
    
class NewResponse(BaseModel):
    id: int
    title: str
    body: str
    user: User  # Include the user relationship

    class Config:
        orm_mode = True
