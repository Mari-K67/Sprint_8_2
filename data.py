import random
import string

class Url:
    MAIN_URL = 'https://stellarburgers.education-services.ru'
    CREATE_USER_URL = f'{MAIN_URL}/api/auth/register'
    LOGIN_URL = f'{MAIN_URL}/api/auth/login'
    CHANGE_USER_DATA_URL = f'{MAIN_URL}/api/auth/user'
    CREATE_ODER = f'{MAIN_URL}/api/orders'
    GET_USER_ODER_URL = f'{MAIN_URL}/api/orders'
    DELETE_USER_URL  = f'{MAIN_URL}/api/auth/user'

class Body:
    RANDOM_FIELD = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
    USER_BODY = {
        "email": f'{RANDOM_FIELD}@mail.ru',
        "password": RANDOM_FIELD,
        "name": RANDOM_FIELD
    }

    ODER_BODY = {"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa6f"]}
    ODER_BODY_WRONG = {"ingredients": ["wrong_ingredient"]}

class AnswerMessage:
    EXIST_USER_ANSWER_403 = 'User already exists'
    USER_WITHOUT_1_FIELD_403 = 'Email, password and name are required fields'
    LOGIN_USER_WITH_WRONG_FIELD_401 = 'email or password are incorrect'
    CHANGE_USER_DATA_401 = 'You should be authorised'
    CREATE_ODER_WITHOUT_INGREDIENTS_400 = 'Ingredient ids must be provided'
    GET_ODER_WITHOUT_AVTIRIZATION_401 = 'You should be authorised'