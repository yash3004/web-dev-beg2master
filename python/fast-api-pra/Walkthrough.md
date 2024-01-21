//creating a crud applicaiton here well be sharing the docs related to it 
C - create - /create/posts
R - Read -/posts/{id}
        -/posts
U - Update -/update/posts/{id}
D - Delete -/delete/posts/{id}

//all the crud operations are performed now we'll shift to the using of db and code it in the proper format 

database :- 
        we never update/delete/post/read in the db we prefer to use an dbms which helps in accessing the dbms 
        2 types of db : relational(sql-based) and no-sql
        1.realtional : 1.mysql 
                       2.postgresql --> we'll work with postgres
                       3.oracle
                       4.sqlserver
        2.nosql:       1.Mongodb
                       2.Dynamodb
                       3.oracle
                       4.sqlserver
        sql :- structured query language, is the language for accessing and changing the data in the db 

        postgres :- multiple seperate db for diff app (the instance is created for the postgres )
