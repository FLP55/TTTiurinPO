import pytest

from api.test_framework.steps_api import ApiSteps

@pytest.mark.api
def test_api_17_register_new_user():
    ApiSteps().register_new_user(email="eve.holt@reqres.in", password="pistol")