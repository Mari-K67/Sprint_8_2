import pytest
import allure
from api_requests import OrderApi
from data import AnswerMessage


class TestGetUserOder:
    @allure.title('Получение заказов авторизованного пользователя')
    def test_get_oder_with_login(self, create_user):
        access_token= create_user[3]
        response = OrderApi.get_user_oder(access_token)
        assert response.status_code == 200
        assert response.json()['success'] == True

    @allure.title('Получение заказов неавторизованного пользователя')
    def test_get_oder_without_login(self):
        access_token = None
        response = OrderApi.get_user_oder(access_token)
        assert response.status_code == 401
        assert response.json()['success'] == False
        assert response.json()['message'] == AnswerMessage.GET_ODER_WITHOUT_AVTIRIZATION_401