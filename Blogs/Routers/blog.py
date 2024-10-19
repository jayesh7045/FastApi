from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session, joinedload
from .. import schemas, dbConnect, models
from typing import List
get_db = dbConnect.get_db


router = APIRouter();

@router.post("/blogs", response_model=schemas.Blog, tags = ['Blog'])
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(id = request.id, title=request.title, body=request.body, user_id = request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.get('/blogs', status_code=status.HTTP_200_OK, tags = ['Blog'])
def get_blogs(db: Session = Depends(get_db)):
    all_blogs_data = db.query(models.Blog).all();
    return all_blogs_data


@router.delete('/delete_blogs/{id}', status_code=status.HTTP_204_NO_CONTENT, tags = ['Blog'])
def delete_blogs(id:int, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit();
    raise HTTPException(status_code = status.HTTP_204_NO_CONTENT, detail = f"The item with {id} is deleted")

@router.put('/update_blogs/{id}', tags = ['Blog'])
def update_blogs(id:int, request: schemas.Blog, db:Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).update({"title" : request.title, "body" : request.body})
    db.commit();
    raise HTTPException(status_code=status.HTTP_200_OK, detail = "Updated")



@router.get('/getblogs_in_response_model/{id}', response_model=schemas.NewResponse, tags=['Blog'])
def get_blogs_in_response_model(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).options(joinedload(models.Blog.user)).filter(models.Blog.id == id).first()
    
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    
    return blog



@router.get('/getallblogs/{id}', response_model=List[schemas.UserBlog], tags = ['Blog'])
def get_all_blogs(id:int, db:Session = Depends(get_db)):
    
    blog = db.query(models.User).options(joinedload(models.User.blogs)).filter(models.User.id == id).all()
    return blog