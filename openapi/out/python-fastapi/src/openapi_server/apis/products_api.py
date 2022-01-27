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
from openapi_server.models.inline_object import InlineObject
from openapi_server.models.product import Product


router = APIRouter()


@router.get(
    "/products",
    responses={
        200: {"model": List[Product], "description": "Success Resopnse"},
    },
    tags=["products"],
    summary="Get the products in the store",
)
async def products_get(
) -> List[Product]:
    """Get Products Information"""
    ...


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
    inline_object: InlineObject = Body(None, description=""),
) -> str:
    ...
