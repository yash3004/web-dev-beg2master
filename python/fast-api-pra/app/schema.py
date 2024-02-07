from pydantic import BaseModel,EmailStr
from datetime import datetime
class PostBase(BaseModel):

    title: str
    content: str
    published: bool = False
    ratings: int = None

class CreatePost(PostBase):
    pass
class Post(PostBase):
    id : int 
    created_at : datetime
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email : EmailStr
    password : str
    


class CreateUser(UserBase):
    pass


class UserOut(UserBase):
    created_at: datetime
    class Config:
        exclude = { "password"}
  