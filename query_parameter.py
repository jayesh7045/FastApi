from fastapi import FastAPI
import pydantic 
from typing import Optional
app = FastAPI()
@app.get('/getdata/')
def cal_fun(limit: int, published: bool):
    if published:
        return f"The published Blogs are {limit}";
    else:
        return f"The Blogs {limit} are not published"

@app.get('/optional_params')
def operation_fun_for_optional_params(limit : int, published : bool = True, sort:Optional[int] = 100):
    return f"The limit is {limit} and its published {published} and sort is {sort}";

