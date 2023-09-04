from typing import Any
import requests
from requests import Response




class BaseRequests:

    def get(self, url: str) -> Response:
        return self._api_call("GET", url=url)

    def post(self, url: str, json: dict = None) -> Response:
        return self._api_call("POST", url=url, json=json)

    def put(self, url: str, json: dict = None) -> Response:
        return self._api_call("PUT", url=url, json=json)

    def patch(self, url: str, json: dict = None) -> Response:
        return self._api_call("PATCH", url=url, json=json)

    def delete(self, url: str) -> Response:
        return self._api_call("DELETE", url=url)

    def _api_call(self, method: Any, url: str, json: dict = None) -> Any:
        return self._request(method, url, json=json)

    def _request(self, method: Any, url: str, json: dict = None) -> Response:
        return requests.request(method, url, json=json)