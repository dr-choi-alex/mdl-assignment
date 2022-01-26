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
from models.inline_object2 import InlineObject2
from models.inline_object3 import InlineObject3
from models.inline_object4 import InlineObject4


router = APIRouter()


@router.post(
    "/signin",
    responses={
        201: {"model": object, "description": "Success Resopnse with path param"},
        400: {"model": str, "description": "Fail to Log-in."},
    },
    tags=["sign"],
    summary="Login User",
)
async def signin_post(
    inline_object2: InlineObject2 = Body(None, description=""),
) -> object:
    ...


@router.post(
    "/signout",
    responses={
        201: {"model": str, "description": "Success Resopnse with path param"},
        400: {"model": str, "description": "Fail Resopnse with path param"},
    },
    tags=["sign"],
    summary="Logout User",
)
async def signout_post(
    inline_object3: InlineObject3 = Body(None, description=""),
) -> str:
    ...


@router.post(
    "/signup",
    responses={
        201: {"model": str, "description": "Success Resopnse with path param"},
        400: {"model": str, "description": "Fail Resopnse with path param"},
    },
    tags=["sign"],
    summary="Logout User",
)
async def signup_post(
    inline_object4: InlineObject4 = Body(None, description=""),
) -> str:
    ...
