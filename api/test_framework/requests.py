from test_data.url import MainURL
from api.test_framework.base_request import BaseRequests


class RequestForTestApi:

    def __init__(self) -> None:
        self.request = BaseRequests()
        self.base_url = MainURL().get_url_from_dict("base_url")

    def get_list_user(self, number_page : any):
        return self.request.get(url=f"{self.base_url}/api/users?page={number_page}")

    def get_singe_user(self, user_number : any):
        return self.request.get(url=f"{self.base_url}/api/users/{user_number}")

    def get_list_resource(self):
        return self.request.get(url=f"{self.base_url}/api/unknown")

    def get_list_resource_with_number(self, res_number):
        return self.request.get(url=f"{self.base_url}/api/unknown/{res_number}")

    def create_user(self, payload: dict):
        return self.request.post(url=f"{self.base_url}/api/users", json=payload)

    def update_user(self, user_number: any, payload: dict):
        return self.request.put(url=f"{self.base_url}/api/users/{user_number}", json=payload)

    def update_user_patch(self, user_number: any, payload: dict):
        return self.request.patch(url=f"{self.base_url}/api/users/{user_number}", json=payload)

    def delete_user(self, user_number : any):
        return self.request.delete(url=f"{self.base_url}/api/users/{user_number}")

    def register_user(self, payload: dict):
        return self.request.post(url=f"{self.base_url}/api/register", json=payload)

    def login_user(self, payload: dict):
        return self.request.post(url=f"{self.base_url}/api/login", json=payload)

    def get_delayed_response(self, delay_page : any):
        return self.request.get(url=f"{self.base_url}/api/users?delay={delay_page}")