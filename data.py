import random
import string

class Url:
    main_url = 'https://stellarburgers.education-services.ru'
    create_user_url = f'{main_url}/api/auth/register'
    login_url = f'{main_url}/api/auth/login'
    change_user_data_url = f'{main_url}/api/auth/user'
    create_oder = f'{main_url}/api/orders'
    get_user_oder_url = f'{main_url}/api/orders'
    delete_user_url = f'{main_url}/api/auth/user'

class Body:
    random_field = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
    user_body = {
        "email": f'{random_field}@mail.ru',
        "password": random_field,
        "name": random_field
    }

    oder_body = {"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa6f"]}
    oder_body_wrong = {"ingredients": ["wrong_ingredient"]}

class AnswerMessage:
    exist_user_answer_403 = 'User already exists'
    user_without_1_field_403 = 'Email, password and name are required fields'
    login_user_with_wrong_field_401 = 'email or password are incorrect'
    change_user_data_401 = 'You should be authorised'
    create_oder_without_ingredients_400 = 'Ingredient ids must be provided'
    get_oder_without_avtirization_401 = 'You should be authorised'