import json

import allure
import jsonschema
import requests
from allure_commons.types import AttachmentType
import logging
from utils.random_data import email, password,username
from utils.utils import load_schema

base_url = "https://try.vikunja.io/api/v1"

#
# def api_request(endpoint, method, **kwargs):
#     url = f'{base_url}/{endpoint}'
#     result = getattr(requests, method)(url, **kwargs)
#
#     return result

email_user = email()
password_user = password()
user_name = username()
data = {}

def API_request(endpoint, method, **kwargs):
    url = f'{base_url}/{endpoint}'
    results = getattr(requests, method)(url, **kwargs)
    # allure.attach(body=results.text, name="Response",attachment_type=AttachmentType.TEXT)
    allure.attach(body=json.dumps(results.json(), indent=4, ensure_ascii=True), name="Response",
                  attachment_type=AttachmentType.JSON, extension="json")
    allure.attach(body=str(results.status_code), name="Response status code", attachment_type=AttachmentType.TEXT,
                  extension='txt')
    allure.attach(body=results.url, name="API URL", attachment_type=AttachmentType.TEXT,
                  extension='txt')
    allure.attach(body=json.dumps(kwargs, indent=4, ensure_ascii=True), name="Request body",
                  attachment_type=AttachmentType.JSON, extension="json")

    logging.info("Request: " + results.request.url)
    if results.request.body:
        logging.info("INFO Request body: " + results.request.body.decode('utf-8'))
    logging.info("Request headers: " + str(results.request.headers))
    logging.info("Response code " + str(results.status_code))
    logging.info("Response: " + results.text)

    return results


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

# logging.info("Request: " + result.request.url)
# if result.request.body:
#     logging.info("INFO Request body: " + result.request.body)
# logging.info("Request headers: " + str(result.request.headers))
# logging.info("Response code " + str(result.status_code))
# logging.info("Response: " + result.text)


