from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database URL
# SQLALCHEMY_DATABASE_URL = "sqlite:///./blogs.db"  # You can use any name, e.g., "blog.db"


SQLALCHEMY_DATABASE_URL = "sqlite:///./blogs.db";
# Create the engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread" : False});
# Create a session
SessionLocal = sessionmaker(bind=engine, autoflush= False, autocommit = False);
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our models
Base = declarative_base()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




