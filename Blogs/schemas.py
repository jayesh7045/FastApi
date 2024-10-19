from pydantic import BaseModel

# Pydantic schema for Blog
class Blog(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True  # This allows Pydantic to work with ORM models like SQLAlchemy

class Response_model(BaseModel):
    title : str
    class Config():
        orm_mode = True