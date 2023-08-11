import pytest
import requests
from test_data import BASE_URL, AUTH_DATA


@pytest.mark.feature("Authentication")
@pytest.mark.story("Successful Authentication")
def test_auth_success():
    response = authenticate()
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    assert "token" in response.json(), "Authentication token not found in the response"


def authenticate():
    url = BASE_URL + "/auth"
    response = requests.post(url, json=AUTH_DATA)
    return response
