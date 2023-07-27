

from test_data.url import MainURL
from test_framework.base_request import BaseRequests


class RequestForTestApi:

    def __init__(self) -> None:
        self.request = BaseRequests()
        self.base_url = MainURL().get_url_from_dict("base_url")
        self.params = self.request.params

    def get_data_from_request(self):
        return self.request.get(url=f"{self.base_url}", params=self.params)