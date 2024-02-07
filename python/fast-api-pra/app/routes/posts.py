
from fastapi import FastAPI , Depends , HTTPException,status,APIRouter,Response
from .. import models , schema
from ..database  import SessionLocal , get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix='/posts')
@router.get('/posts',response_model=list[schema.Post])
def read_posts(post : schema.CreatePost , db:Session=Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts
@router.get("/sql")
def test_posts(db:Session=Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"data": posts}

@router.post('/createposts' , status_code=status.HTTP_201_CREATED , response_model=schema.Post)
def create_post(post: schema.CreatePost , db:Session = Depends(get_db),):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return  new_post

@router.get("/posts/{post_id}")
def get_post(post_id: int , db:Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    return post


    #     response.status_code = 200
    #     return post
    # else:
    #     response.status_code = 404
    #     return {"eror" : "404"}
    return post

#deleting the https req
@router.delete("/del_post/{post_id}" , status_code=status.HTTP_204_NO_CONTENT , )
def del_post(post_id:int, db:Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id)
    if(post.first() is None):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    post.delete(synchronize_session= True)
    db.commit
    return post.first()
    
@router.put("/update_post/{post_id}", status_code=status.HTTP_205_RESET_CONTENT,response_model=schema.Post)
def put_post(post_id: int, response: Response, post: schema.CreatePost , db:Session=Depends(get_db)):
    post_q = db.query(models.Post).filter(models.Post.id == post_id)
    if(post_q.first() is None):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    post_q.update(**post.dict())
    