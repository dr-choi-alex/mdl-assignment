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


router = APIRouter()


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
    ...


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
    userId: str = Path(None, description="Reads and displays user&#39;s cart information."),
) -> None:
    ...


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
    ...
