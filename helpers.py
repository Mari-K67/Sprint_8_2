import random
import string

def generate_random_string_EN(length=7):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string


#универсальный метод для создания body для запросов на создание пользователя 
def create_data_payload():
    return {
        "email": f"{generate_random_string_EN()}@mail.ru",
        "password": generate_random_string_EN(),
        "name": generate_random_string_EN()
    }