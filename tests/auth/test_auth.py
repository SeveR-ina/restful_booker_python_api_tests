import logging

import pytest
import requests
import allure

from helpers.helpers_for_tests import assert_status_code
from tests.test_data import WRONG_AUTH_DATA, AUTH_DATA, BASE_URL
from logging_config import configure_logging  # Import the logging configuration function

# import os
# os.system("start report.html")
# for mac os: os.system("open report.html") / for linux: os.system("xdg-open # report.html")

# Call the configure_logging function to set up logging
configure_logging()


@allure.parent_suite('Authentication Suite')
@pytest.mark.feature("Authentication")
@pytest.mark.story("Successful Authentication and Authentication with wrong credentials")
@pytest.mark.parametrize("auth_data, expected_status",
                         [(AUTH_DATA, 200), (WRONG_AUTH_DATA, 200)])  # for wrong test data api shows 200 :/
def test_authentication(auth_data, expected_status):
    logger = logging.getLogger(__name__)
    logger.info("Test started: Authentication")

    response = authenticate_with(json=auth_data)
    logger.info("Authentication response: %s", response.text)

    assert_status_code(response, expected_status)

    if auth_data == AUTH_DATA:
        assert "token" in response.json(), "Authentication token not found in the response"
    elif auth_data == WRONG_AUTH_DATA:
        response_data = response.json()
        assert "reason" in response_data, "Expected 'reason' key in the response"
        assert response_data["reason"] == "Bad credentials", "Unexpected 'reason' value in the response"

    logger.info("Test completed: Authentication")


def authenticate_with(json):
    url = BASE_URL + "/auth"
    response = requests.post(url, json)
    return response
