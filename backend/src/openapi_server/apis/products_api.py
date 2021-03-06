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
from models.inline_object import InlineObject
from models.product import Product
from pydantic import BaseModel
from starlette.responses import JSONResponse
from db.db_pool import get_db_conn


router = APIRouter()


class Product(BaseModel):
    name : str
    price: int
    image : str
    description : str
    


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
    with get_db_conn() as conn:
        result = conn.selectDB("products", "*")
        return result

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
    product : Product,
    #inline_object: InlineObject = Body(None, description=""),
) -> str:
    with get_db_conn() as conn:
        result = conn.insertDB("products", "name, img_addr, description, price", "%s, %s, %s, %s", product.name, product.image, product.description, product.price)
        
        if result:
            return JSONResponse(status_code=201, content=dict(msg="Success"))
        else:
            return JSONResponse(status_code=400, content=dict(msg="Fail"))
