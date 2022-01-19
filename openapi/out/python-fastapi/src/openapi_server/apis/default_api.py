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


router = APIRouter()


@router.post(
    "/test",
    responses={
        201: {"description": "Success Resopnse with path param"},
    },
    tags=["default"],
    summary="RequestBody Test",
)
async def test_post(
    request_body: List[List] = Body(None, description="List of user object zzz"),
) -> None:
    ...
