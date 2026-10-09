import pytest
import allure
from api_requests import UserApi
from data import Body, AnswerMessage

class TestChangeUserData:
    @allure.title('Изменение данных пользователя c авторизацией')
    @pytest.mark.parametrize("empty_key", [
       'email', 
       'password'
       ])
    def test_change_user_data_with_login(self, create_user, empty_key):
        user_body = create_user[0].copy()
        access_token= create_user[3]
        user_body[empty_key] = Body.RANDOM_FIELD
        response = UserApi.change_user_data(access_token, user_body)
        assert response.status_code == 200 
        assert response.json()['success'] == True

    @allure.title('Изменение данных пользователя без авторизации')
    @pytest.mark.parametrize("empty_key", [
       'email', 
       'password'
       ])
    def test_change_user_data_without_login(self, empty_key):
        user_body = Body.USER_BODY
        access_token = None
        user_body[empty_key] = Body.RANDOM_FIELD
        response = UserApi.change_user_data(access_token, user_body)
        assert response.status_code == 401 
        assert response.json()['success'] == False
        assert response.json()['message'] == AnswerMessage.CHANGE_USER_DATA_401