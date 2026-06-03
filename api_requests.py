import requests
import allure
from data import Url

class UserApi:
    @staticmethod
    @allure.step('запрос на создание пользователя')
    def create_user(body):
        return requests.post(Url.CREATE_USER_URL, json=body)

    @staticmethod
    @allure.step('запрос на авторизацию пользователя')
    def user_login(body):
        return requests.post(Url.LOGIN_URL, data=body)

    @staticmethod
    @allure.step('запрос на изменение пользователя')
    def change_user_data(access_token, body):
        return requests.patch(Url.CHANGE_USER_DATA_URL, headers={'Authorization': f'{access_token}'}, data=body)

    @staticmethod
    @allure.step('запрос на удаление пользователя')
    def delete_user(access_token):
        return requests.delete(Url.DELETE_USER_URL, headers={'Authorization': f'{access_token}'})

class OrderApi:
    @staticmethod
    @allure.step('запрос на создание заказа')
    def create_oder(body, access_token):
        return requests.post(Url.CREATE_ODER, data=body, headers={'Authorization': f'{access_token}'})
    
    @staticmethod
    @allure.step('запрос на получение заказов пользователя')
    def get_user_oder(access_token):
        return requests.get(Url.GET_USER_ODER_URL, headers={'Authorization': f'{access_token}'})
