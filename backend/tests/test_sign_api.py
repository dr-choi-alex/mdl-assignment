# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.inline_object2 import InlineObject2  # noqa: F401
from openapi_server.models.inline_object3 import InlineObject3  # noqa: F401
from openapi_server.models.inline_object4 import InlineObject4  # noqa: F401


def test_signin_post(client: TestClient):
    """Test case for signin_post

    Login User
    """
    inline_object2 = openapi_server.InlineObject2()

    headers = {
    }
    response = client.request(
        "POST",
        "/signin",
        headers=headers,
        json=inline_object2,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_signout_post(client: TestClient):
    """Test case for signout_post

    Logout User
    """
    inline_object3 = openapi_server.InlineObject3()

    headers = {
    }
    response = client.request(
        "POST",
        "/signout",
        headers=headers,
        json=inline_object3,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_signup_post(client: TestClient):
    """Test case for signup_post

    Logout User
    """
    inline_object4 = openapi_server.InlineObject4()

    headers = {
    }
    response = client.request(
        "POST",
        "/signup",
        headers=headers,
        json=inline_object4,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

