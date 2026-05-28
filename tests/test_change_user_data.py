import pytest
import allure
import api_requests
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
        user_body[empty_key] = Body.random_field
        response = api_requests.change_user_data(access_token, user_body)
        assert response.status_code == 200 
        assert response.json()['success'] == True

    @allure.title('Изменение данных пользователя без авторизации')
    @pytest.mark.parametrize("empty_key", [
       'email', 
       'password'
       ])
    def test_change_user_data_without_login(self, empty_key):
        user_body = Body.user_body
        access_token = None
        user_body[empty_key] = Body.random_field
        response = api_requests.change_user_data(access_token, user_body)
        assert response.status_code == 401 
        assert response.json()['success'] == False
        assert response.json()['message'] == AnswerMessage.change_user_data_401