import allure
import jsonschema

from tests.conftest import API_request
from tests.test_create_user import created_user
from vikunja_api_test_framework.utils.utils import load_schema


@allure.title('Successful authorization')
@allure.feature('Authorization with API')
@allure.label('layer', 'API')
@allure.label('owner', 'Kostromin')
@allure.tag('regress', 'API')
@allure.severity('critical')
def test_login_user_succsessfuly():
    data = created_user
    with allure.step("Отправляем запрос на авторизацию"):
        results = API_request("login", "post", json=data)

    with allure.step("Проверяем, что в ответе статус код == 200"):
        assert results.status_code == 200

    with allure.step("Проверяем, что тело ответа совпадает с json_схемой"):
        schema_res = load_schema("login_user_responce.json")
        jsonschema.validate(results.json(), schema_res)

    with allure.step("Сохраняем jwt токен из ответа"):
        jwt_token = results.json()["token"]

        return jwt_token
