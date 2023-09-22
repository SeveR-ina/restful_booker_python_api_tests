def assert_status_code(response, expected_code):
    assert response.status_code == expected_code, f"Expected {expected_code}, but got {response.status_code}"
