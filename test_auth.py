import logging
import pytest
import requests
from test_data import BASE_URL, AUTH_DATA, WRONG_AUTH_DATA
from logging_config import configure_logging  # Import the logging configuration function
import os
os.system("start report.html")
# for mac os: os.system("open report.html") / for linux: os.system("xdg-open # report.html")

# Call the configure_logging function to set up logging
configure_logging()


@pytest.mark.feature("Authentication")
@pytest.mark.story("Successful Authentication")
def test_auth_success():
    """
    Test successful authentication.
    """
    logger = logging.getLogger(__name__)  # Get a logger for this test function
    logger.info("Test started: Successful Authentication")
    response = authenticate(json=AUTH_DATA)
    logger.info("Authentication response: %s", response.text)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    assert "token" in response.json(), "Authentication token not found in the response"
    logger.info("Test completed: Successful Authentication")


@pytest.mark.feature("Authentication")
@pytest.mark.story("Authentication with wrong credentials")
def test_auth_failure():
    """
    Test unsuccessful authentication.
    """
    logger = logging.getLogger(__name__)  # Get a logger for this test function
    logger.info("Test started: Authentication with wrong credentials")
    response = authenticate(json=WRONG_AUTH_DATA)
    logger.info("Authentication response: %s", response.text)

    # Check for the "reason" key in the response JSON
    response_data = response.json()
    assert "reason" in response_data, "Expected 'reason' key in the response"
    assert response_data["reason"] == "Bad credentials", "Unexpected 'reason' value in the response"
    logger.info("Test completed: Authentication with wrong credentials")


def authenticate(json):
    url = BASE_URL + "/auth"
    response = requests.post(url, json)
    return response
