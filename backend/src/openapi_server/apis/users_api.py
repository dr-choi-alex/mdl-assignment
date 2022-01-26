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


@router.post(
    "/users/signin",
    responses={
        201: {"model": object, "description": "Success Resopnse with path param"},
        400: {"model": str, "description": "Fail to Log-in."},
    },
    tags=["users"],
    summary="Login User",
)
async def users_signin_post(
    inline_object2: InlineObject2 = Body(None, description=""),
) -> object:
    ...


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
    userId: int = Path(None, description="Reads and displays user&#39;s cart information."),
    inline_object5: InlineObject5 = Body(None, description=""),
) -> None:
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
