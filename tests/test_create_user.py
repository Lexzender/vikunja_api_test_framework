import json
import allure
import jsonschema
import requests
from allure_commons.types import AttachmentType
import logging
from tests.conftest import base_url, email_user, password_user, API_request, user_name, \
    create_user_succsessfuly, create_user_unsuccsessfuly
from utils.random_data import *
from utils.utils import load_schema



# email_user = email()
# password_user = password()
# username = username()
# data = {}
#
# def API_request(endpoint, method, **kwargs):
#     url = f'{base_url}/{endpoint}'
#     results = getattr(requests, method)(url, **kwargs)
#     # allure.attach(body=results.text, name="Response",attachment_type=AttachmentType.TEXT)
#     allure.attach(body=json.dumps(data, indent=4, ensure_ascii=True), name="Request body",
#                   attachment_type=AttachmentType.JSON, extension="json")
#     allure.attach(body=json.dumps(results.json(), indent=4, ensure_ascii=True), name="Response",
#                   attachment_type=AttachmentType.JSON, extension="json")
#     allure.attach(body=str(results.status_code), name="Response status code", attachment_type=AttachmentType.TEXT,
#                   extension='txt')
#     allure.attach(body=results.url, name="API URL", attachment_type=AttachmentType.TEXT,
#                   extension='txt')
#
#     logging.info("Request: " + results.request.url)
#     if results.request.body:
#         logging.info("INFO Request body: " + results.request.body.decode('utf-8'))
#     logging.info("Request headers: " + str(results.request.headers))
#     logging.info("Response code " + str(results.status_code))
#     logging.info("Response: " + results.text)
#
#     return results
created_user = {}

def test_create_user_succsessfuly():
    global created_user
    data = {
        "email": email_user,
        "password": password_user,
        "username": user_name
    }

    with allure.step("Создаем нового пользователя и сохраняем его данные"):
        # results = API_request("register","post",json=data)
        created_user.update(create_user_succsessfuly(data))



    # with allure.step("Проверяем, что в ответе статус код == 200"):
    #     assert results.status_code == 200
    #
    # with allure.step("Проверяем, что в ответе имя совпадает с отправляемым"):
    #     assert results.json()["username"] == user_name
    #
    # with allure.step("Проверяем, что тело ответа совпадает с json_схемой"):
    #     schema_res = load_schema("create_succsessfull_user_responce.json")
    #     jsonschema.validate(results.json(), schema_res)
    #
    # with allure.step("Проверяем, что тело запроса совпадает с json_схемой"):
    #     schema_req = load_schema("create_succsessfull_user_req.json")
    #     jsonschema.validate(data, schema_req)
    #
    # with allure.step("Сохраняем логин и пароль"):
    #     created_user = {"username":data["username"],"password":data["password"]}
    #
    #     return created_user



def test_create_user_unsuccsessfuly():

    data = {
        "password": password_user,
        "username": user_name
    }

    with allure.step("Отправляем запрос на создание пользователя без 'email'"):
        results = create_user_unsuccsessfuly(data)

    # with allure.step("Проверяем, что в ответе статус код == 400"):
    #     assert results.status_code == 400
    #
    # with allure.step("Проверяем, текст ответа"):
    #     assert results.text.strip()  == '{"code":1004,"message":"Please specify a username and a password."}'
    #
    # with allure.step("Проверяем, что тело ответа совпадает с json_схемой"):
    #     schema_res = load_schema("create_unsuccsessfull_user_responce.json")
    #     jsonschema.validate(results.json(), schema_res)