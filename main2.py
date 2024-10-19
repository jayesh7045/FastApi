from fastapi import FastAPI
import pydantic
app = FastAPI()
@app.get('/')
def route_operation_function():
    return "Hello, This is the route page";

@app.get('/get/{id}')
def route_operation_function(id:int):
    str = 'The id is ', {id}
    return str;
    