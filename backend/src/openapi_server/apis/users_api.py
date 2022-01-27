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
from models.inline_object2 import InlineObject2
from models.inline_object3 import InlineObject3
from models.inline_object4 import InlineObject4
from models.inline_object5 import InlineObject5

from pydantic import BaseModel
from starlette.responses import JSONResponse
from db.db_pool import get_db_conn


router = APIRouter()

class Cart(BaseModel):
    productID: int
    quantity : int
    
class User(BaseModel):
    userID: str
    password: str
    
class Register(BaseModel):
    usertype : str
    username: str
    userID : str
    password : str
    email : str

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
    user: Register
    #inline_object1: InlineObject1 = Body(None, description=""),
) -> str:
    print("abc")
    usertype = user.usertype
    username = user.username
    userID = user.userID
    password = user.password
    email = user.email
    
    
    with get_db_conn() as conn:
        result = conn.insertDB("users", "login_id, password, email, full_name, type", "%s, %s, %s, %s, %s", userID, password, email, username, usertype)
        if result:
            return JSONResponse(status_code=200, content=dict(msg="Success"))
        else:
            return JSONResponse(status_code=400, content=dict(msg="fail"))


@router.post(
    "/users/signin",
    responses={
        201: {"model": str, "description": "Success Resopnse with path param"},
        400: {"model": str, "description": "Fail to Log-in."},
    },
    tags=["users"],
    summary="Login User",
)
async def users_signin_post(
    user :User
    # inline_object2: InlineObject2 = Body(None, description=""),
    
) -> str:
    print("abc")
    user_id = user.userID
    password = user.password
    usertype = ""
    
    with get_db_conn() as conn:
        
        #conn.deleteDB("carts", "user_id=%s", 56)
        result = conn.selectDB("users", "id, email, full_name, type", "login_id = %s and password = %s", user_id, password)

        # 아이디 찾기에 실패했을 때
        if len(result) == 0:
            return JSONResponse(status_code=400, content=dict(msg="fail"))
        
        # 아이디를 찾았을 때
        usertype = "buyer"
        if result[0].get("type") == 1:
            usertype = "seller"    
        
        return {
            "id" : result[0].get("id"),
            "userID" : user_id,
            "usertype" : usertype
        }


@router.delete(
    "/users/{userId}/Carts",
    responses={
        200: {"description": "Success Resopnse with path param"},
        400: {"model": str, "description": "Fail Resopnse with path param"},
    },
    tags=["users"],
    summary="Delete the user&#39;s cart item",
)
async def users_user_id_carts_delete(
    cart : Cart,
    userId: int = Path(None, description="Reads and displays user&#39;s cart information."),
    # inline_object5: InlineObject5 = Body(None, description=""),
) -> None:
    print(userId)
    with get_db_conn() as conn:
        result = conn.deleteDB ("carts", "user_id=%s and product_id=%s", userId,cart.productID )
        if len(result) > 0 and result is not None:
            return result
        else:
            return {}


@router.get(
    "/users/{userId}/Carts",
    responses={
        200: {"model": List[object], "description": "Success Resopnse"},
    },
    tags=["users"],
    summary="Get the user&#39;s cart information",
)
async def users_user_id_carts_get(
    userId: int = Path(None, description="Reads and displays user&#39;s cart information."),
) -> List[object]:
    with get_db_conn() as conn:
        result = conn.selectDB("carts", "*","user_id = %d", userId)
        if len(result) > 0 and result is not None:
            return result
        else:
            return {}
            #return JSONResponse(status_code=200, content=dict(msg="empty"))


@router.post(
    "/users/{userId}/Carts",
    responses={
        201: {"model": str, "description": "Success Resopnse with path param"},
        400: {"model": str, "description": "Fail Resopnse with path param"},
    },
    tags=["users"],
    summary="add the user&#39;s cart item",
)
async def users_user_id_carts_post(
    cart : Cart,
    userId: int = Path(None, description="add product info to user&#39;s cart"),
    #inline_object4: InlineObject4 = Body(None, description=""),
) -> str:
   with get_db_conn() as conn:
            result = conn.selectDB("carts", "*", "user_id = %s and product_id = %s", userId, cart.productID)

            print(result)
            
            if len(result) > 0 and result is not None:
                return JSONResponse(status_code=200, content=dict(msg="already exist"))
            else:
                result = conn.insertDB("carts", "user_id, product_id, quantity", "%s, %s, %s", userId, cart.productID, cart.quantity)
                return JSONResponse(status_code=200, content=dict(msg="update DB"))


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
    userId: int = Path(None, description="Reads and displays user&#39;s cart information."),
    inline_object3: InlineObject3 = Body(None, description=""),
) -> None:
    ...
