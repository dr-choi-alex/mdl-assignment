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
from openapi_server.models.parameters import Parameters


router = APIRouter()


@router.get(
    "/product",
    responses={
        200: {"model": object, "description": "Success Resopnse"},
    },
    tags=["product"],
    summary="Get the products in the store / main page",
)
async def product_get(
) -> object:
    """Get Product Information"""
    ...


@router.post(
    "/product",
    responses={
        201: {"model": str, "description": "Success Resopnse with path param"},
        400: {"model": str, "description": "Fail Resopnse with path param"},
    },
    tags=["product"],
    summary="Add a new product to the store",
)
async def product_post(
    parameters: Parameters = Query(None, description="Add data to DB by sending product information."),
) -> str:
    ...
