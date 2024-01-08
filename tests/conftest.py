import json
import logging

import allure
import requests
from allure_commons.types import AttachmentType

from vikunja_api_test_framework.utils.random_data import email, password, username

base_url = "https://try.vikunja.io/api/v1"

email_user = email()
password_user = password()
user_name = username()
data = {}


def API_request(endpoint, method, **kwargs):
    url = f'{base_url}/{endpoint}'
    results = getattr(requests, method)(url, **kwargs)
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
