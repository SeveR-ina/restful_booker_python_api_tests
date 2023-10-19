import logging
from typing import Final

import pytest
import requests
import allure

from helpers.helpers_for_tests import assert_status_code
from tests.test_data import WRONG_AUTH_DATA, AUTH_DATA, BASE_URL
from logging_config import configure_logging

STEP: Final = 'Get response and authenticate'

# import os
# os.system("start report.html")
# for mac os: os.system("open report.html") / for linux: os.system("xdg-open # report.html")

# Call the configure_logging function to set up logging
configure_logging()


@allure.suite('Authentication')
class TestAuthentication:
    @allure.feature("Authentication statuses")
    @allure.story("Auth statuses with correct/wrong test data")
    @pytest.mark.parametrize("auth_data, expected_status",
                             [(AUTH_DATA, 200), (WRONG_AUTH_DATA, 200)])  # for wrong test data api shows 200 :/
    def test_authentication_statuses(self, auth_data, expected_status):
        logger = logging.getLogger(__name__)
        logger.info("Test started: Test auth statuses with correct/wrong test data")

        with allure.step(STEP):
            response = authenticate_with(json=auth_data)
        logger.info("Authentication response: %s", response.text)

        with allure.step("Assert status code"):
            assert_status_code(response, expected_status)
        logger.info("Test completed: Test auth statuses with correct/wrong test data")

    @allure.feature("Authentication")
    @allure.story("Successful Authentication")
    def test_successful_authentication(self):
        logger = logging.getLogger(__name__)

        logger.info("Test started: Successful Authentication")
        with allure.step(STEP):
            response = authenticate_with(json=AUTH_DATA)

        with allure.step("Assert token in response"):
            assert "token" in response.json(), "Authentication token not found in the response"
        logger.info("Test completed: Successful Authentication")

    @allure.feature("Authentication")
    @allure.story("Response data")
    def test_failed_authentication_response_data(self):
        logger = logging.getLogger(__name__)

        logger.info("Test started: Test reason in response data for failed authentication")
        with allure.step(STEP):
            response = authenticate_with(json=WRONG_AUTH_DATA)

        with allure.step("Get response data"):
            response_data = response.json()

        with allure.step("Assert reason is Bad credentials"):
            assert response_data["reason"] == "Bad credentials", "Unexpected 'reason' value in the response"
        logger.info("Test completed: Test reason in response data for failed authentication")


def authenticate_with(json):
    url = BASE_URL + "/auth"
    response = requests.post(url, json)
    return response
