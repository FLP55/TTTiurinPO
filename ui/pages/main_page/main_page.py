from typing import Any


import requests

from api.test_framework.main_checkers import CommonChecker
from test_data.data_url import base_url
from ui.locators.main_page.main_page_locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class MainPage:
    def __init__(self, browser: webdriver.Chrome):
        self.locators = MainPageLocators
        self.browser = browser
        self.url = base_url


    def click_button(self, locator: str) -> None:
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.locators.button_list_users_locator))
        list_button = self.browser.find_element(*getattr(self.locators, locator))
        list_button.click()


    def get_status_code_get(self, path: str) -> Any:
        status_code = requests.get(url=f"{self.url}{path}").status_code
        return status_code


    def get_status_code_post(self, path: str, json: dict = None) -> Any:
        status_code = requests.post(url=f"{self.url}{path}", json=json).status_code
        return status_code


    def get_status_code_put(self, path: str, json: dict = None) -> Any:
        status_code = requests.put(url=f"{self.url}{path}", json=json).status_code
        return status_code


    def get_status_code_patch(self, path: str, json: dict = None) -> Any:
        status_code = requests.patch(url=f"{self.url}{path}", json=json).status_code
        return status_code


    def get_status_code_delete(self, path: str) -> Any:
        status_code = requests.delete(url=f"{self.url}{path}").status_code
        return status_code


    def check_status_code(self, status_code: Any) -> None:
        expected_status_code = self.browser.find_element(*self.locators.field_response_status_code_locator).text
        CommonChecker.check_field_equals(
            str(status_code), expected_status_code, assertion_message="Неверный статус код страницы"
        )


    def get_response_body_get(self, path: str) -> Any:
        body = requests.get(url=f"{self.url}{path}").json()
        return body


    def get_response_body_post(self, path: str, json: dict = None) -> Any:
        body = requests.post(url=f"{self.url}{path}", json=json).json()
        return body


    def get_response_body_put(self, path: str, json: dict = None) -> Any:
        body = requests.put(url=f"{self.url}{path}", json=json).json()
        return body


    def get_response_body_patch(self, path: str, json: dict = None) -> Any:
        body = requests.patch(url=f"{self.url}{path}", json=json).json()
        return body


    def get_response_body_delete(self, path: str) -> Any:
        body = requests.delete(url=f"{self.url}{path}").text
        return body


    def check_response_body(self, body: Any) -> None:
        expected_body = self.browser.find_element(
            *self.locators.field_response_body_locator
        ).text.replace('\n    ', '').replace('"', "'").replace(" ", "").replace("\n", "")
        CommonChecker.check_field_equals(
            str(body).replace(" ", ""), expected_body, assertion_message="Тело запроса не совпадает"
        )
