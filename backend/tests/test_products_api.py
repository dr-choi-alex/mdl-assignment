# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.inline_object import InlineObject  # noqa: F401
from openapi_server.models.product import Product  # noqa: F401


def test_products_get(client: TestClient):
    """Test case for products_get

    Get the products in the store
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/products",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_products_post(client: TestClient):
    """Test case for products_post

    Add a new product to the store
    """
    inline_object = openapi_server.InlineObject()

    headers = {
    }
    response = client.request(
        "POST",
        "/products",
        headers=headers,
        json=inline_object,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

