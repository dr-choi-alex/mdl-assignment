# coding: utf-8

"""
    MDL Assignment

    Shopping Mall Demo

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from ast import Num
from torch import quantile
from cmath import log
from ntpath import join
from time import time
from fastapi import FastAPI, Path

from apis.products_api import router as ProductsApiRouter
from apis.users_api import router as UsersApiRouter

import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from pydantic import BaseModel
from db.db_pool import get_db_pool, get_db_conn

app = FastAPI(
    title="MDL Assignment",
    description="Shopping Mall Demo",
    version="1.0",
)


origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(ProductsApiRouter)
app.include_router(UsersApiRouter)


get_db_pool().init_app(app, DB_USER="testuser"
                            , DB_PW="1234"
                            , DB_HOST = "10.99.80.67"
                            , DB_PORT = "5432"
                            , DB_NAME = "mdl")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
