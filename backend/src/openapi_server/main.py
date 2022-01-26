# coding: utf-8

"""
    MDL Assignment

    Shopping Mall Demo

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from ast import Num
import uvicorn
from cmath import log
from ntpath import join
from time import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from numpy import array, integer, number

from apis.products_api import router as ProductsApiRouter
from apis.sign_api import router as SignApiRouter
from apis.users_api import router as UsersApiRouter
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2
import datetime
from db.db_pool import get_db_pool, get_db_conn


##Postgresql 연동
#db = psycopg2.connect(host='localhost', dbname='postgres',user='postgres',password='1234',port=5432)
db = psycopg2.connect(host='10.99.80.67', dbname='mdl',user='testuser',password='1234',port=5432)
cursor=db.cursor()

def execute(self,query,args={}):
    self.cursor.execute(query,args)
    row = self.cursor.fetchall()
    return row

def insertDB(table,colum,data):
    sql = " INSERT INTO {table}({colum}) VALUES ('{data}') ;".format(table=table,colum=colum,data=data)
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e :
        print(" insert DB  ",e) 
        
def readDB(table,colum, query):
    sql = " SELECT {colum} from {table} {query}".format(colum=colum,table=table, query=query)
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except Exception as e :
        result = (" read DB err",e)
    
    return result

app = FastAPI(
    title="MDL Assignment",
    description="Shopping Mall Demo",
    version="1.0",
)
origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ProductsApiRouter)
app.include_router(SignApiRouter)
app.include_router(UsersApiRouter)

get_db_pool().init_app(app, DB_USER="testuser"
                            , DB_PW="1234"
                            , DB_HOST = "10.99.80.67"
                            , DB_PORT = "5432"
                            , DB_NAME = "mdl")

# 준석 sample code
class User(BaseModel):
    userID: str
    password: str
    
class UserID(BaseModel):
    id: str
    userID: str
    usertype: str
    
class Register(BaseModel):
    usertype : str
    username: str
    userID : str
    password : str
    email : str

    
class Cart_Product(BaseModel):
    id: str
    name: str
    img_addr: str
    description: str
    price: str
    created_at : str
    

@app.post('/login')
def login(user: User):
    userID = user.userID
    password = user.password
    usertype = ""
    
    with get_db_conn() as conn:
        
        #conn.deleteDB("carts", "user_id=%s", 56)
        result = conn.selectDB("users", "id, email, full_name, type", "login_id = %s and password = %s", userID, password)

        # 아이디 찾기에 실패했을 때
        if len(result) == 0:
            return JSONResponse(status_code=400, content=dict(msg="fail"))
        
        # 아이디를 찾았을 때
        usertype = "buyer"
        if result[0].get("type") == 1:
            usertype = "seller"    
        
        return {
            "id" : result[0].get("id"),
            "userID" : userID,
            "usertype" : usertype
        }

@app.post('/register')
def register(user : Register):
    usertype = user.usertype
    username = user.username
    userID = user.userID
    password = user.password
    email = user.email
    return_value = ""
    
    
    with get_db_conn() as conn:
        result = conn.insertDB("users", "login_id, password, email, full_name, type", "%s, %s, %s, %s, %s", userID, password, email, username, usertype)
        if result:
            return JSONResponse(status_code=200, content=dict(msg="Success"))
        else:
            return JSONResponse(status_code=400, content=dict(msg="fail"))

@app.post('/shopping-cart')
def shoppingCart(user:UserID):
    userID = user.userID

    with get_db_conn() as conn:
        
        result = conn.selectDB("users", "id", "login_id = %s", userID )

        user_id = result[0].get("id")
        
        cart_info = conn.selectDB("carts", "*", "user_id = %s", user_id)

        if cart_info is None or len(cart_info) == 0:
            return {}

        cond = ''
        for info in cart_info:
            cond = "{a} {b},".format(a=cond, b=info.get("product_id"))

        
        product_info = conn.selectDB("products", "*", "id in ({cond})".format(cond=cond[:-1]) )
       
        return { "product_info": product_info, "cart_info" :cart_info }
    

@app.post('/removeItem')
def removeItem(item : Cart_Product):
    id: item.id
    name: item.name
    img_addr: item.imgaddr
    description: item.description
    price: item.price
    created_at : item.created_at
    
    print(id)
    return
    
    
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)