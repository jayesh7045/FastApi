from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

class Blog(BaseModel):
    title : str
    bodyContent : str
    rno : int
app = FastAPI()
@app.post('/blog')
def post_method(request : Blog):
    return f"The title is {request.title} and the body is {request.bodyContent} and the {request.rno}"

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port = 9000)