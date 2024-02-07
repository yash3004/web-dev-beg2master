# database.py
from .database import Base
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy import Column,Integer,String,Boolean

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    title = Column(String, index=True)
    content = Column(String)
    ratings = Column(Integer)
    published = Column(Boolean , server_default='False')
    created_at = Column(TIMESTAMP(timezone=True) ,nullable=False , server_default=text('now()'))   
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    email = Column(String , nullable=False , unique= True)  
    password = Column(String ,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True) ,nullable=False , server_default=text('now()'))  
    