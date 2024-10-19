from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class MyClass(BaseModel):
    name: str
    roll_no: int

@app.get('/')
def index1():
    return "Heyy"

@app.post('/get/postmethod')
def showData(data: MyClass):
    return data

@app.get('/about')
def about():
    return {"about": "This is the about page"}

@app.get('/get/{id}/comments')
def comments(id: int):
    return {"id": id}

@app.get('/get/blogs')
def blogs(limit: int, published: bool):
    if published:
        return f'{limit} blogs are there and the blogs are {published}'
    else:
        return f'There are no published blogs'

@app.get('/get/optional')
def optional_fun(published: bool, sort: Optional[str] = None):
    return f'Lets {sort} the game'
