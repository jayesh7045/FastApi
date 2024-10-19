from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session, joinedload
from . import models, schemas
from .dbConnect import engine, get_db
from typing import List
from passlib.context import CryptContext

# Initialize FastAPI app
app = FastAPI()

# Create the tables in the database if they don't exist
models.Base.metadata.create_all(bind=engine)









    
    
