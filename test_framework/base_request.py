from typing import Any
import requests
from requests import Response

main_params = {
    "sol": None,
    "camera": None,
    "api_key": None,
    "earth_date": None,
    "page": None
}



class BaseRequests:

    def __init__(self) -> None:
        self.params = main_params

    def get(self, url: str, params: dict = None) -> Response:
        return self._api_call("GET", url=url, params=params)

    def _api_call(self, method: Any, url: str, params: dict = None) -> Any:
        return self._request(method, url, params=params)

    def _request(self, method: Any, url: str, params: dict = None) -> Response:
        return requests.request(method, url, params=params)