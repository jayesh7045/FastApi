
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session, joinedload
from passlib.context import CryptContext 
from .. import schemas, dbConnect, models
from typing import List
router = APIRouter();


get_db = dbConnect.get_db
pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated = "auto")


@router.post('/user', tags = ['User'])
def post_user(request : schemas.User, db: Session = Depends(get_db)):
    hashed_pwd = pwd_cxt.hash(request.password);
    new_user = models.User(id = request.id, name = request.name, email = request.email, password = hashed_pwd)
    db.add(new_user)
    db.commit();
    db.refresh(new_user)
    return new_user

@router.get('/user', tags = ['User'])
def get_all_user(db: Session = Depends(get_db)):
    users = db.query(models.User).all();
    return users;

@router.get('/user/{id}', tags = ['User'])
def get_with_user_id(id:int, status_code = status.HTTP_200_OK, db:Session = Depends(get_db)):
    user_data = db.query(models.User).filter(id == models.User.id).first()
    if not user_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"No user with {id} as id")
    return user_data