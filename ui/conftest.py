import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager




@pytest.fixture(scope="function")
def browser():
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service=service, options=options)
    browser.get("https://reqres.in")
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
