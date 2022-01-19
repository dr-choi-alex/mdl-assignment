# coding: utf-8

from fastapi.testclient import TestClient




def test_test_post(client: TestClient):
    """Test case for test_post

    RequestBody Test
    """
    request_body = [None]

    headers = {
    }
    response = client.request(
        "POST",
        "/test",
        headers=headers,
        json=request_body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

