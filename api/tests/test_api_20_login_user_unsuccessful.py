import pytest

from api.data_for_api_test.data_for_tests import data_for_register_user_unsuccessful
from api.test_framework.steps_api import ApiSteps

@pytest.mark.api
@pytest.mark.parametrize("data", data_for_register_user_unsuccessful)
def test_api_20_login_user_unsuccessful(data):
    ApiSteps().login_hard_user_negative(email=data)