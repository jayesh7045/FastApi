from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .dbConnect import SessionLocal, engine
from . import models
from . import schemas
app = FastAPI();
models.Base.metadata.create_all(bind = engine)
def get_db():
    db = SessionLocal()
    try:
        yield db;
    except:
        db.close();
@app.post('/jayeshblogs', response_model=schemas.Blog)
def insert_data(request : schemas.Blog, db: Session = Depends(get_db)):
    new_data = models.Blog(title = request.title, body = request.body )
    db.add(new_data);
    db.commit();
    db.refresh(new_data)
    return new_data
@app.get('/jayeshblogs')
def get_data(db: Session = Depends(get_db)):
   db_data = db.query(models.Blog).all();
   return db_data
    
@app.get('/blogs/{id}')
def get_by_id(id:int, db: Session=Depends(get_db)):
    blog_data = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog_data