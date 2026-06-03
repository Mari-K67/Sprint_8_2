import pytest
import allure
from api_requests import UserApi
from data import AnswerMessage

class TestCreateUser:
    @allure.title('Успешное создание уникального пользователя')
    def test_create_user_succeed(self, create_user):
        response_data = create_user[1]
        status_code = create_user[2]
        assert status_code == 200
        assert response_data['success'] == True

    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_user_twice(self, create_user):
        user_body= create_user[0]
        response_2 = UserApi.create_user(user_body)
        assert response_2.status_code == 403
        assert response_2.json()['success'] == False
        assert AnswerMessage.EXIST_USER_ANSWER_403 in response_2.text

    @allure.title('Создание пользователя c не заполненым одним из обязательных полей')
    @pytest.mark.parametrize("empty_key", [
       'email', 
       'password',
       'name'
       ])
    def test_create_user_without_1_field(self, create_user, empty_key):
        user_body = create_user[0].copy()
        user_body[empty_key] = ''
        response = UserApi.create_user(user_body)
        assert response.status_code == 403
        assert response.json()['success'] == False
        assert AnswerMessage.USER_WITHOUT_1_FIELD_403 in response.text
    