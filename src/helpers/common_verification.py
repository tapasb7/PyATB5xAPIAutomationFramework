#Common Verification
# Common Verification

# HTTP Status Code
# Headers
# Data Verification
# JSON schema


def verify_http_status_code(response_data, expected_data):
    assert response_data.status_code == expected_data, "Failed to get http status code"

def verify_response_key(key, expected_data):
    assert key == expected_data, "Failed to get http status code"

def verify_json_key_not_null(key):
    assert key  != 0, "Failed : Key is NULL"

def verify_json_key_not_none(key):
    assert key is not None

def verify_json_key_greater_than_zero(key):
    assert key >= 0, "Failed : Key is not greater than zero"

def verify_response_deleted_booking(response):
    assert "Created" in response, "Failed to Delete booking"
