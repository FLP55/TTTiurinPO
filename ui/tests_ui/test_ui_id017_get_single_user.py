
import pytest

from test_data.data_url import users_path
from ui.pages.main_page.main_page import MainPage


@pytest.mark.ui
def test_ui_get_single_user(browser):
    # Клик на кнопку single_user
    MainPage(browser).click_button("single_users_locator")
    # Получение статус кода с API
    status_code = MainPage(browser).get_status_code_get(f"{users_path}/2")
    # Сверка статус кода запроса
    MainPage(browser).check_status_code(status_code)
    # Получение тела зпроса с API
    response_body = MainPage(browser).get_response_body_get(f"{users_path}/2")
    # Проверка соответствия тела запроса
    MainPage(browser).check_response_body(response_body)
