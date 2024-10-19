from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from . import models, schemas
from .dbConnect import engine, SessionLocal
from typing import List


# Initialize FastAPI app
app = FastAPI()

# Create the tables in the database if they don't exist
models.Base.metadata.create_all(bind=engine)

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/blogs", response_model=schemas.Blog)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blogs', status_code=status.HTTP_200_OK)
def get_blogs(db: Session = Depends(get_db)):
    all_blogs_data = db.query(models.Blog).all();
    return all_blogs_data


@app.delete('/delete_blogs/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blogs(id:int, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit();
    raise HTTPException(status_code = status.HTTP_204_NO_CONTENT, detail = f"The item with {id} is deleted")

@app.put('/update_blogs/{id}')
def update_blogs(id:int, request: schemas.Blog, db:Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).update({"title" : request.title, "body" : request.body})
    db.commit();
    raise HTTPException(status_code=status.HTTP_200_OK, detail = "Updated")

@app.get('/getblogs_in_response_model/{id}', status_code=200, response_model=schemas.Response_model)
def get_blogs_in_response_model(id: int, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    
    if not blog:
        response.status_code = 404
        return {"detail": "Blog not found"}
    
    return blog



@app.get('/getallblogs', response_model=List[schemas.Response_model])
def get_all_blogs(db:Session = Depends(get_db)):
    blog = db.query(models.Blog).all()
    return blog
    

