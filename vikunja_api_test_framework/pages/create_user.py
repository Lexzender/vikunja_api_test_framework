import allure
import jsonschema

from tests.conftest import API_request, user_name
from vikunja_api_test_framework.utils.utils import load_schema


def create_user_succsessfuly(data):

    with allure.step("Отправляем запрос на создание пользователя"):
        results = API_request("register", "post", json=data)

    with allure.step("Проверяем, что в ответе статус код == 200"):
        assert results.status_code == 200

    with allure.step("Проверяем, что в ответе имя совпадает с отправляемым"):
        assert results.json()["username"] == user_name

    with allure.step("Проверяем, что тело ответа совпадает с json_схемой"):
        schema_res = load_schema("create_succsessfull_user_responce.json")
        jsonschema.validate(results.json(), schema_res)

    with allure.step("Проверяем, что тело запроса совпадает с json_схемой"):
        schema_req = load_schema("create_succsessfull_user_req.json")
        jsonschema.validate(data, schema_req)

    with allure.step("Сохраняем логин и пароль"):
        created_user = {"username":data["username"],"password":data["password"]}

        return created_user


def create_user_unsuccsessfuly(data):

    with allure.step("Отправляем запрос на создание пользователя"):
        results = API_request("register", "post", json=data)

    with allure.step("Проверяем, что в ответе статус код == 400"):
        assert results.status_code == 400

    with allure.step("Проверяем, текст ответа"):
        assert results.text.strip() == '{"code":1004,"message":"Please specify a username and a password."}'

    with allure.step("Проверяем, что тело ответа совпадает с json_схемой"):
        schema_res = load_schema("create_unsuccsessfull_user_responce.json")
        jsonschema.validate(results.json(), schema_res)

        return results
