import allure

from tests.conftest import email_user, password_user, user_name
from vikunja_api_test_framework.pages.create_user import create_user_succsessfuly, create_user_unsuccsessfuly

created_user = {}


@allure.title('Create random user succsessfuly')
@allure.feature('User create API')
@allure.label('layer', 'API')
@allure.label('owner', 'Kostromin')
@allure.tag('regress', 'API')
@allure.severity('critical')
def test_create_user_succsessfuly():
    global created_user
    data = {
        "email": email_user,
        "password": password_user,
        "username": user_name
    }

    with allure.step("Создаем нового рандомного пользователя и сохраняем его данные"):
        created_user.update(create_user_succsessfuly(data))

@allure.title('Create random user unsuccsessfuly')
@allure.feature('User create without email')
@allure.label('layer', 'API')
@allure.label('owner', 'Kostromin')
@allure.tag('regress', 'API')
@allure.severity('critical')
def test_create_user_unsuccsessfuly():
    data = {
        "password": password_user,
        "username": user_name
    }

    with allure.step("Отправляем запрос на создание пользователя без 'email'"):
        create_user_unsuccsessfuly(data)
