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
from openapi_server.models.inline_object1 import InlineObject1
from openapi_server.models.inline_object2 import InlineObject2
from openapi_server.models.inline_object3 import InlineObject3
from openapi_server.models.inline_object4 import InlineObject4
from openapi_server.models.inline_object5 import InlineObject5


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
    ...


@router.post(
    "/users/{userId}/Carts",
    responses={
        200: {"description": "Success Resopnse with path param"},
        400: {"model": str, "description": "Fail Resopnse with path param"},
    },
    tags=["users"],
    summary="add the user&#39;s cart item",
)
async def users_user_id_carts_post(
    userId: int = Path(None, description="add product info to user&#39;s cart"),
    inline_object4: InlineObject4 = Body(None, description=""),
) -> None:
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
    userId: int = Path(None, description="Reads and displays user&#39;s cart information."),
    inline_object3: InlineObject3 = Body(None, description=""),
) -> None:
    ...
