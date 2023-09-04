import pytest

from api.test_framework.steps_api import ApiSteps

@pytest.mark.api
def test_api_19_login_user():
    ApiSteps().login_hard_user(email="eve.holt@reqres.in", password="pistol")