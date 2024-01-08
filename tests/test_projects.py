import allure
import jsonschema

from tests.test_create_user import API_request
from tests.test_login import test_login_user_succsessfuly
from utils.utils import load_schema

project_id = ""

def test_create_new_projects():
    global project_id

    with allure.step("Авторизуемся и получаем jwt_token"):
        jwt_token = test_login_user_succsessfuly()

    headers = {'Authorization': f"Bearer {jwt_token}"}
    data =  {
        "title": "Тестовый проект 2",
        "description": "",
        "identifier": "",
        "hex_color": "",
        "parent_project_id": 0,
        "default_bucket_id": 0,
        "done_bucket_id": 0,
        "owner": {
            "id": 74,
            "name": "",
            "username": "xichnek",
            "created": "2024-01-06T17:12:04+01:00",
            "updated": "2024-01-06T17:12:04+01:00"
        },
        "is_archived": False,
        "background_information": None,
        "background_blur_hash": "",
        "is_favorite": False,
        "position": 5439488,
        "created": "2024-01-06T17:12:04+01:00",
        "updated": "2024-01-06T17:12:04+01:00"
    }

    with allure.step("Отправляем запрос на создание нового проекта"):
        results = API_request("projects","put",headers=headers, json=data)

    with allure.step("Проверяем, что в ответе статус код == 201"):
        assert results.status_code == 201

    with allure.step("Проверяем название проекта"):
        assert results.json()["title"] == "Тестовый проект 2"

    with allure.step("Проверяем, что тело ответа совпадает с json_схемой"):
        schema_res = load_schema("create_projects_responce.json")
        jsonschema.validate(results.json(), schema_res)

    with allure.step("Сохраняем id проекта"):
        project_id = str(results.json()["id"])


def test_Get_projects_by_id():


    with allure.step("Авторизуемся и получаем jwt_token"):
        jwt_token = test_login_user_succsessfuly()

    headers = {'Authorization': f"Bearer {jwt_token}"}

    with allure.step("Отправляем запрос на получение проекта"):
        results = API_request(f"projects/{project_id}","get",headers=headers)

    with allure.step("Проверяем, что в ответе статус код == 200"):
        assert results.status_code == 200

    with allure.step("Проверяем название проекта"):
        assert results.json()["title"] == "Тестовый проект 2"

    with allure.step("Проверяем, что тело ответа совпадает с json_схемой"):
        schema_res = load_schema("get_projects_id_responce.json")
        jsonschema.validate(results.json(), schema_res)

def test_delete_projects():
    with allure.step("Авторизуемся и получаем jwt_token"):
        jwt_token = test_login_user_succsessfuly()

    headers = {'Authorization': f"Bearer {jwt_token}"}

    with allure.step("Отправляем запрос на удаление проекта"):
        results = API_request(f"projects/{project_id}", "delete", headers=headers)

    with allure.step("Проверяем, что в ответе статус код == 200"):
        assert results.status_code == 200

    with allure.step("Проверяем текст ответа"):
        results.json()["message"] == "Successfully deleted."

    with allure.step("Проверяем, что тело ответа совпадает с json_схемой"):
        schema_res = load_schema("delete_project_responce.json")
        jsonschema.validate(results.json(), schema_res)
