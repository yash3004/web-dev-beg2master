#user authorization 
so we'll perforn the same crud operation on the user like we did before for the post 
we'll create seperate table in db and perform the CRUD operations 
email validator , passlib hashing convertt password to hashed password 


-- after the user authentucation take place ""

2  types of authentication 
session based:- a info stored in the backend server to keep track of the loggin in and logged out 
jwt authentication :- there is nothing on the backend server for login and logout its stored on the frontend rather than backend 
    (cliend side ) flow of user auth in jwt:
        1.client try to login in /login(username+pass)
        2.if cred(username + pass) are valid a jwt token is generated 
        3.we get the token and if we want to access the post then we req the post with the jwt token 
            /post {token}
        4. if the token is valid then the response will be the acc to the request 
JWT token breakout :
token is made up of 3 pieces :- 1.header(meta data for the token ie 1. the type and the algo to hash the token (sha256)) 
                                2.payload(data(id of the user) , name of the user , role of the user , date) (the data we want should be less as it will result in making the string long and lagging)
                                3.verification secrete 
                    we take all these things and addup the verification secrete and create the jwt token (we pass it to the singing algorithms)
purpose of the signature :
    1.user logged in -> token created with credentials if creds are valid a token is generated then same process as above :
    the token include:header payload data , secrete (password)with these three we create a signature (hashing function) => and hence a token is formed 
    ![alt text](image.png)
    ![image](https://github.com/yash3004/web-dev-beg2master/assets/91517727/892a8c2d-f618-4057-9f02-ea5a99f09c6b)
