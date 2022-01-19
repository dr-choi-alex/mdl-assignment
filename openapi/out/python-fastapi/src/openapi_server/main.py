# coding: utf-8

"""
    MDL Assignment

    Shopping Mall Demo

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from fastapi import FastAPI

from openapi_server.apis.default_api import router as DefaultApiRouter
from openapi_server.apis.product_api import router as ProductApiRouter
from openapi_server.apis.user_api import router as UserApiRouter

app = FastAPI(
    title="MDL Assignment",
    description="Shopping Mall Demo",
    version="1.0",
)

app.include_router(DefaultApiRouter)
app.include_router(ProductApiRouter)
app.include_router(UserApiRouter)
