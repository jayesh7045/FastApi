from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def index1():
    return "Heyy";


@app.get('/about')
def about():
    return {"about" : "This is the about page"}