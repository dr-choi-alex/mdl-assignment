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
from models.inline_object1 import InlineObject1
from models.user import User
from pydantic import BaseModel

from starlette.responses import JSONResponse
from db.db_pool import get_db_conn

router = APIRouter()

class Cart(BaseModel):
    productID: int
    quantity : int


@router.post(
    "/users",
    responses={
        201: {"model": str, "description": "Success Resopnse with path param"},
        400: {"model": str, "description": "Fail Resopnse with path param"},
    },
    tags=["users"],
    summary="Create User",
)
async def users_post(
    inline_object1: InlineObject1 = Body(None, description=""),
) -> str:
    ...


@router.get(
    "/users/{userId}/Carts",
    responses={
        200: {"model": List[object], "description": "Success Resopnse"},
    },
    tags=["users"],
    summary="Get the user&#39;s cart information",
)
async def users_user_id_carts_get(
    userId: str = Path(None, description="Reads and displays user&#39;s cart information."),
) -> List[object]:
    with get_db_conn() as conn:
        result = conn.selectDB("carts", "*","user_id = %d", userId)
        if len(result) > 0 and result is not None:
            return result
        else:
            return {}
            #return JSONResponse(status_code=200, content=dict(msg="empty"))


@router.put(
    "/users/{userId}/Carts",
    responses={
        200: {"description": "Success Resopnse with path param"},
        400: {"model": str, "description": "Fail Resopnse with path param"},
    },
    tags=["users"],
    summary="Update the user&#39;s cart information",
)
async def users_user_id_carts_put(
    cart : Cart,
    userId: str = Path(None, description="Reads and displays user&#39;s cart information."),
) : 
    # #=========================[ 확인 ]======================
    # #post임 수정해야함, API 수정 후 다시 skeleton 만들어서 하기
    # #=======================================================

    # # FIXME: API 수정 cart가 배열로, url path로 userId를 받고  cart에 productID, quantity만 있으면 됨. 
    # import psycopg2

    # connection = psycopg2.connect(host='10.99.80.67', dbname='mdl',user='testuser',password='1234',port=5432)
    
    # # Create a cursor to perform database operations
    # cursor = connection.cursor()
    
    # # write DB

    # sqlString = "SELECT * FROM carts WHERE user_id=%s AND product_id=%s"
    # cursor.execute(sqlString, (cart.userID, cart.productID))
    # print()
    
    # if cursor.rowcount > 0 :
    #     return {"exist"}
    # else :
    #     sqlString = "INSERT INTO carts (user_id, product_id, quantity) VALUES (%s, %s, %s);"
    #     cursor.execute(sqlString, (cart.userID, cart.productID, 1) )
    #     connection.commit()
    # return {"update DB"}

    with get_db_conn() as conn:
            result = conn.selectDB("carts", "*", "user_id = %s and product_id = %s", userId, cart.productID)

            print(result)
            
            if len(result) > 0 and result is not None:
                return JSONResponse(status_code=200, content=dict(msg="already exist"))
            else:
                result = conn.insertDB("carts", "user_id, product_id, quantity", "%s, %s, %s", userId, cart.productID, cart.quantity)
                return JSONResponse(status_code=200, content=dict(msg="update DB"))


@router.get(
    "/users/{userId}",
    responses={
        200: {"model": User, "description": "Success Resopnse"},
    },
    tags=["users"],
    summary="Get the user detail information",
)
async def users_user_id_get(
    userId: str = Path(None, description="The id of the user to retrieve"),
) -> User:
    with get_db_conn() as conn:
        result = conn.selectDB("users", "*", "id = %d", userId)
        if len(result) > 0 and result is not None:
            return result
        else:
            return JSONResponse(status_code=400, content=dict(msg="User ID does not exist"))
