import pytest
import allure
import api_requests
from data import AnswerMessage


class TestGetUserOder:
    @allure.title('Получение заказов авторизованного пользователя')
    def test_get_oder_with_login(self, create_user):
        access_token= create_user[3]
        response = api_requests.get_user_oder(access_token)
        assert response.status_code == 200
        assert response.json()['success'] == True

    @allure.title('Получение заказов неавторизованного пользователя')
    def test_get_oder_without_login(self):
        access_token = None
        response = api_requests.get_user_oder(access_token)
        assert response.status_code == 401
        assert response.json()['success'] == False
        assert response.json()['message'] == AnswerMessage.get_oder_without_avtirization_401