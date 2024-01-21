from fastapi import FastAPI,Response,HTTPException,status
from pydantic import BaseModel
from random import randrange


app = FastAPI()

# Define the API schema
class Post(BaseModel):

    title: str
    content: str
    published: bool = False
    ratings: int = None

# Dictionary to store posts
posts = []
#dinding the po st 
def find_post(post_id):
    for i in posts:
        if(i['id'] == post_id):
            return i
def find_idx(post_id):
    for i,p in enumerate(posts):
        if(p["id"] == post_id):
            return i
        


@app.get('/posts')
def read_posts():
    return posts

@app.post('/createposts' , status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,100)
    posts.append(post_dict)
    return {"post_id": post_dict['id'], "message": "Post created successfully"}

@app.get("/posts/{post_id}")
def get_post(post_id: int , response:Response):
    post = find_post(post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    #     response.status_code = 200
    #     return post
    # else:
    #     response.status_code = 404
    #     return {"eror" : "404"}

#deleting the https req
@app.delete("/del_post/{post_id}" , status_code=status.HTTP_204_NO_CONTENT)
def del_post(post_id:int,response : Response):
    idx=find_idx(post_id)
    if(idx  == None):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"post id : {post_id} not found")
    posts.pop(idx)
    return {"message" : f"{post_id} is successfully deleted "}
@app.put("/update_post/{post_id}", status_code=status.HTTP_205_RESET_CONTENT)
def put_post(post_id: int, response: Response, post: Post):
    idx = find_idx(post_id)
    if idx is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    post_dict = post.dict()
    post_dict['id'] = post_id  # Corrected variable name to post_id
    posts[idx] = post_dict
    return {"data": post_dict}
