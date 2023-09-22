# import pytest
# import requests
#
# from tests.test_data import BASE_URL, AUTH_DATA
#
#
# @pytest.fixture(scope="session")
# def authenticate_and_get_token():
#     url = BASE_URL + "/auth"
#     response = requests.post(url, json=AUTH_DATA)
#     response_data = response.json()
#     token = response_data["token"]
#     return token
