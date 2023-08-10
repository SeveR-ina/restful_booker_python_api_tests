import unittest
import allure
import requests
from test_data import BASE_URL, AUTH_DATA


class TestAuthEndpoint(unittest.TestCase):

    def setUp(self):
        self.base_url = BASE_URL
        self.headers = {"Content-Type": "application/json"}

    @allure.step("Test Auth Success")
    @allure.feature("Authentication")
    @allure.story("Successful Authentication")
    def test_auth_success(self):
        response = self.authenticate()
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
        assert "token" in response.json(), "Authentication token not found in the response"
        token = response.json()["token"]
        allure.attach(token, name="Authentication Token", attachment_type=allure.attachment_type.TEXT)

    def authenticate(self):
        url = self.base_url + "/auth"
        response = requests.post(url, json=AUTH_DATA, headers=self.headers)
        return response


if __name__ == "__main__":
    unittest.main()
