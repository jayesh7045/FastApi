from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQL_URL = "sqlite:///./blogs.db";
engine = create_engine(SQL_URL, connect_args = {"check_same_thread" : False});
SessionLocal = sessionmaker(bind = engine , autocommit = False, autoflush=False);
Base = declarative_base();