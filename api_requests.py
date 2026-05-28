import requests
import allure
from data import Url


@allure.step('запрос на создание пользователя')
def create_user(body):
    return requests.post(Url.create_user_url, json=body)

@allure.step('запрос на авторизацию пользователя')
def user_login(body):
    return requests.post(Url.login_url, data=body)

@allure.step('запрос на изменение пользователя')
def change_user_data(access_token, body):
    return requests.patch(Url.change_user_data_url, headers={'Authorization': f'{access_token}'}, data=body)

@allure.step('запрос на создание заказа')
def create_oder(body, access_token):
    return requests.post(Url.create_oder, data=body, headers={'Authorization': f'{access_token}'})

@allure.step('запрос на получение заказов пользователя')
def get_user_oder(access_token):
    return requests.get(Url.get_user_oder_url, headers={'Authorization': f'{access_token}'})

@allure.step('запрос на удаление пользователя')
def delete_user(access_token):
    return requests.delete(Url.delete_user_url, headers={'Authorization': f'{access_token}'})