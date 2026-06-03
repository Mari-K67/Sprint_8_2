import pytest
import allure
from api_requests import UserApi
from data import AnswerMessage

class TestLogin:
    @allure.title('Авторизация под существующим пользователем')
    def test_login_exist_user_succeed(self, create_user):
        user_body = create_user[0]
        response = UserApi.user_login(user_body)
        assert response.status_code == 200 
        assert response.json()['success'] == True

    @allure.title('Авторизация c неверным логином и паролем')
    @pytest.mark.parametrize("empty_key", [
       'email', 
       'password'
       ])
    def test_create_user_without_1_field(self, create_user, empty_key):
        user_body = create_user[0]
        user_body[empty_key] = 'something_wrong'  
        response = UserApi.user_login(user_body)
        assert response.status_code == 401
        assert response.json()['success'] == False
        assert AnswerMessage.LOGIN_USER_WITH_WRONG_FIELD_401 in response.text