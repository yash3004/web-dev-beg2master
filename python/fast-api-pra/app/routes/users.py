from fastapi import FastAPI, Depends, HTTPException, status, Response ,APIRouter
from sqlalchemy.orm import Session
from .. database import SessionLocal, engine,get_db
from .. import models, schema,utils
from passlib.context import CryptContext
router = APIRouter(prefix="/users", tags=['Users'])


@router.post("/" , response_model=schema.UserOut)
def create_user(user: schema.CreateUser, db: Session = Depends(get_db)):
    user.password =utils.hashed(user.password)
    new_user = models.User(**user.dict())
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}" , response_model=schema.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.Task).filter(models.User.id == id).first()
    if user is None:
        raise HTTPException
    return user
