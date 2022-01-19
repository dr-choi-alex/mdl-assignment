# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.register import Register  # noqa: F401
from openapi_server.models.register1 import Register1  # noqa: F401
from openapi_server.models.user_id_password import UserIDPassword  # noqa: F401


def test_user_carts_get(client: TestClient):
    """Test case for user_carts_get

    Get the user's cart information
    """
    params = [("shopping_cart", None)]
    headers = {
    }
    response = client.request(
        "GET",
        "/user/carts",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_carts_put(client: TestClient):
    """Test case for user_carts_put

    Update the user's cart information
    """
    params = [("shopping_cart", 'shopping_cart_example')]
    headers = {
    }
    response = client.request(
        "PUT",
        "/user/carts",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_login_post(client: TestClient):
    """Test case for user_login_post

    Login User
    """
    params = [("user_id_password", {'key': openapi_server.UserIDPassword()})]
    headers = {
    }
    response = client.request(
        "POST",
        "/user/login",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_logout_post(client: TestClient):
    """Test case for user_logout_post

    Logout User
    """
    params = [("register", {'key': openapi_server.Register1()})]
    headers = {
    }
    response = client.request(
        "POST",
        "/user/logout",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_post(client: TestClient):
    """Test case for user_post

    Create User
    """
    params = [("register", {'key': openapi_server.Register()})]
    headers = {
    }
    response = client.request(
        "POST",
        "/user",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

