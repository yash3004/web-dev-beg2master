from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models, schema,utils
from passlib.context import CryptContext
from .routes import posts,users

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(posts.router)
app.include_router(users.router)



