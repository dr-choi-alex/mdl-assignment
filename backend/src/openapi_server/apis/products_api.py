# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from models.extra_models import TokenModel  # noqa: F401
from models.inline_object import InlineObject
from models.product import Product
from pydantic import BaseModel


router = APIRouter()

class Product(BaseModel):
    name : str
    price: int
    description : str
    image : str


@router.get(
    "/products",
    responses={
        200: {"model": List[Product], "description": "Success Resopnse"},
    },
    tags=["products"],
    summary="Get the products in the store / main page",
)
async def products_get(
# ) -> List[Product]:
#     """Get Products Information"""
#     ...
) :
    import psycopg2
    from psycopg2.extras import RealDictCursor

    connection = psycopg2.connect(host='10.99.80.67', dbname='mdl',user='testuser',password='1234',port=5432)
    
    # Create a cursor to perform database operations
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    
    # read DB
    sqlString = "SELECT * FROM products"
    cursor.execute(sqlString)
    rows = cursor.fetchall()
    
    return rows



@router.post(
    "/products",
    responses={
        201: {"model": str, "description": "Success Resopnse with path param"},
        400: {"model": str, "description": "Fail Resopnse with path param"},
    },
    tags=["products"],
    summary="Add a new product to the store",
)
async def products_post(
    product : Product,
    # inline_object: InlineObject = Body(None, description=""),
# ) -> str:
#      ...
) : 
    


    import psycopg2

    connection = psycopg2.connect(host='10.99.80.67', dbname='mdl',user='testuser',password='1234',port=5432)
    
    # Create a cursor to perform database operations
    cursor = connection.cursor()
    
    # write DB
    sqlString = "INSERT INTO products (name, img_addr, description, price) VALUES (%s, %s, %s, %s);"
    cursor.execute(sqlString, (product.name, product.image, product.description, product.price) )
    connection.commit()
    
    return {"name" : product.name, "image" : product.image, "price" : product.price, "description" : product.description}
