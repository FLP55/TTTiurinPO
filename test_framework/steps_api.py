from typing import Any

from test_framework.main_checkers import CommonChecker
from test_framework.requests import RequestForTestApi


class ApiSteps:

    def __init__(self) -> None:
        self.request = RequestForTestApi()

    def check_status_code_403(self, sol, camera, page, api_key, earth_date) -> Any:
        self.request.params['sol'] = sol
        self.request.params['camera'] = camera
        self.request.params['page'] = page
        self.request.params['api_key'] = api_key
        self.request.params['earth_date'] = earth_date
        response = self.request.get_data_from_request()
        print(response)
        CommonChecker.check_status_code_403(response, assertion_message="Статус код 200")

    def check_status_code_200(self, sol, camera, page, api_key, earth_date) -> Any:
        self.request.params['sol'] = sol
        self.request.params['camera'] = camera
        self.request.params['page'] = page
        self.request.params['api_key'] = api_key
        self.request.params['earth_date'] = earth_date
        response = self.request.get_data_from_request()
        print(response.json())
        CommonChecker.check_status_code_200(response, assertion_message="Статус код 403")