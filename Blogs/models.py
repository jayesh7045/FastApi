from sqlalchemy import Column, Integer, String
from .dbConnect import Base

# Define the Blog model, representing a table in the database
class Blog(Base):
    __tablename__ = "blogs"  # This will be the name of the table

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String)
