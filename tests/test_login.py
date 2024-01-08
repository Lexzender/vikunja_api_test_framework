import os

import allure
from dotenv import load_dotenv

from tests.conftest import create_user_unsuccsessfuly, user_name, create_user_succsessfuly
from tests.test_create_user import API_request, email_user, password_user, created_user


# load_dotenv()



def test_login_user_succsessfuly():
    # global data
    # data = {
    #     "email": email_user,
    #     "password": password_user,
    #     "username": user_name
    # }

    #test_create_user_succsessfuly():
    # with allure.step("Отправляем запрос на создание пользователя"):
    #     new_data = create_user_succsessfuly(data)

    data = created_user

    with allure.step("Отправляем запрос на получение jwt токена"):
        results = API_request("login","post",json=data)

    with allure.step("Сохраняем jwt токен"):
        jwt_token = results.json()["token"]

        return jwt_token





