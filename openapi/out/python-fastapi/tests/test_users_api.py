# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.inline_object1 import InlineObject1  # noqa: F401
from openapi_server.models.inline_object2 import InlineObject2  # noqa: F401
from openapi_server.models.inline_object3 import InlineObject3  # noqa: F401
from openapi_server.models.inline_object4 import InlineObject4  # noqa: F401
from openapi_server.models.inline_object5 import InlineObject5  # noqa: F401


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


def test_users_signin_post(client: TestClient):
    """Test case for users_signin_post

    Login User
    """
    inline_object2 = openapi_server.InlineObject2()

    headers = {
    }
    response = client.request(
        "POST",
        "/users/signin",
        headers=headers,
        json=inline_object2,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_users_user_id_carts_delete(client: TestClient):
    """Test case for users_user_id_carts_delete

    Delete the user's cart item
    """
    inline_object5 = openapi_server.InlineObject5()

    headers = {
    }
    response = client.request(
        "DELETE",
        "/users/{userId}/Carts".format(userId=56),
        headers=headers,
        json=inline_object5,
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
        "/users/{userId}/Carts".format(userId=56),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_users_user_id_carts_post(client: TestClient):
    """Test case for users_user_id_carts_post

    add the user's cart item
    """
    inline_object4 = openapi_server.InlineObject4()

    headers = {
    }
    response = client.request(
        "POST",
        "/users/{userId}/Carts".format(userId=56),
        headers=headers,
        json=inline_object4,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_users_user_id_carts_put(client: TestClient):
    """Test case for users_user_id_carts_put

    Update the user's cart information
    """
    inline_object3 = openapi_server.InlineObject3()

    headers = {
    }
    response = client.request(
        "PUT",
        "/users/{userId}/Carts".format(userId=56),
        headers=headers,
        json=inline_object3,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

