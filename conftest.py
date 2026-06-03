import pytest
import api_requests
import helpers


@pytest.fixture
def create_user():
    body = helpers.create_data_payload()
    response = api_requests.create_user(body)
    response_data = response.json()
    access_token = response_data.get("accessToken")
   
    yield body, response_data, response.status_code, access_token

    if access_token:
        api_requests.delete_user(access_token)