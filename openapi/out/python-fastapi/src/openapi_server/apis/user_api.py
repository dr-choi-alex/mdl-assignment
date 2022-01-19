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

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.register import Register
from openapi_server.models.register1 import Register1
from openapi_server.models.user_id_password import UserIDPassword


router = APIRouter()


@router.get(
    "/user/carts",
    responses={
        200: {"model": List[object], "description": "Success Resopnse with path param"},
    },
    tags=["user"],
    summary="Get the user&#39;s cart information",
)
async def user_carts_get(
    shopping_cart:  = Query(None, description="Reads and displays user&#39;s cart information."),
) -> List[object]:
    ...


@router.put(
    "/user/carts",
    responses={
        200: {"model": List[object], "description": "Success Resopnse with path param"},
        400: {"model": str, "description": "Fail Resopnse with path param"},
    },
    tags=["user"],
    summary="Update the user&#39;s cart information",
)
async def user_carts_put(
    shopping_cart: str = Query(None, description="Reads and displays user&#39;s cart information."),
) -> List[object]:
    ...


@router.post(
    "/user/login",
    responses={
        201: {"model": object, "description": "Success Resopnse with path param"},
        400: {"model": str, "description": "Fail to Log-in."},
    },
    tags=["user"],
    summary="Login User",
)
async def user_login_post(
    user_id_password: UserIDPassword = Query(None, description="Send the user&#39;s id and password to find out appropriate DB data."),
) -> object:
    ...


@router.post(
    "/user/logout",
    responses={
        201: {"model": str, "description": "Success Resopnse with path param"},
        400: {"model": str, "description": "Fail Resopnse with path param"},
    },
    tags=["user"],
    summary="Logout User",
)
async def user_logout_post(
    register: Register1 = Query(None, description="Add data to DB by sending user information."),
) -> str:
    ...


@router.post(
    "/user",
    responses={
        201: {"model": str, "description": "Success Resopnse with path param"},
        400: {"model": str, "description": "Fail Resopnse with path param"},
    },
    tags=["user"],
    summary="Create User",
)
async def user_post(
    register: Register = Query(None, description="Add data to DB by sending user information."),
) -> str:
    ...
