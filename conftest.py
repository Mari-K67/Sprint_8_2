import pytest
from api_requests import UserApi
import helpers


@pytest.fixture
def create_user():
    body = helpers.create_data_payload()
    response = UserApi.create_user(body)
    response_data = response.json()
    access_token = response_data.get("accessToken")
   
    yield body, response_data, response.status_code, access_token

    if access_token:
        UserApi.delete_user(access_token)