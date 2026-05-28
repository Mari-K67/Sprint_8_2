import pytest
import allure
import api_requests
from data import Body, AnswerMessage

class TestCreateOder:
    @allure.title('Создание заказа c авторизацией')
    def test_create_oder_with_login(self, create_user):
        access_token = create_user[3]
        response = api_requests.create_oder(Body.oder_body, access_token)
        assert response.status_code == 200
        assert response.json()['success'] == True

    @allure.title('Создание заказа без авторизации')
    def test_create_oder_without_login(self):
        access_token = None
        response = api_requests.create_oder(Body.oder_body, access_token)
        assert response.status_code == 200
        assert response.json()['success'] == True
    
    @allure.title('Создание заказа без ингредиентов')
    def test_create_oder_without_ingredients(self, create_user):
        access_token = create_user[3]
        oder_body = {}
        response = api_requests.create_oder(oder_body, access_token)
        assert response.status_code == 400
        assert response.json()['success'] == False
        assert AnswerMessage.create_oder_without_ingredients_400 in response.text

    @allure.title('Создание заказа c неверным хешем ингредиентов.')
    def test_create_oder_with_wrong_ingredient(self, create_user):
        access_token= create_user[3]
        response = api_requests.create_oder(Body.oder_body_wrong, access_token)
        assert response.status_code == 500