import allure

from tests.conftest import API_request
from tests.test_create_user import created_user

@allure.title('Successful authorization')
@allure.feature('Authorization with API')
@allure.label('layer', 'API')
@allure.label('owner', 'Kostromin')
@allure.tag('regress', 'API')
@allure.severity('critical')
def test_login_user_succsessfuly():
    data = created_user

    with allure.step("Отправляем запрос на получение jwt токена"):
        results = API_request("login", "post", json=data)

    with allure.step("Сохраняем jwt токен"):
        jwt_token = results.json()["token"]

        return jwt_token
