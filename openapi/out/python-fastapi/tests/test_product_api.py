# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.parameters import Parameters  # noqa: F401


def test_product_get(client: TestClient):
    """Test case for product_get

    Get the products in the store / main page
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/product",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_product_post(client: TestClient):
    """Test case for product_post

    Add a new product to the store
    """
    params = [("parameters", {'key': openapi_server.Parameters()})]
    headers = {
    }
    response = client.request(
        "POST",
        "/product",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

