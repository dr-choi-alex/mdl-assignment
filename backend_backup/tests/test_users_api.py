# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.inline_object1 import InlineObject1  # noqa: F401
from openapi_server.models.user import User  # noqa: F401


def test_users_post(client: TestClient):
    """Test case for users_post

    Create User
    """
    inline_object1 = openapi_server.InlineObject1()

    headers = {
    }
    response = client.request(
        "POST",
        "/users",
        headers=headers,
        json=inline_object1,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_users_user_id_carts_get(client: TestClient):
    """Test case for users_user_id_carts_get

    Get the user's cart information
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/users/{userId}/Carts".format(userId='user_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_users_user_id_carts_put(client: TestClient):
    """Test case for users_user_id_carts_put

    Update the user's cart information
    """

    headers = {
    }
    response = client.request(
        "PUT",
        "/users/{userId}/Carts".format(userId='user_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_users_user_id_get(client: TestClient):
    """Test case for users_user_id_get

    Get the user detail information
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/users/{userId}".format(userId='user_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

