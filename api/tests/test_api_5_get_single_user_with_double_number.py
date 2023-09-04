import pytest

from api.data_for_api_test.data_for_tests import random_double_number
from api.test_framework.steps_api import ApiSteps

@pytest.mark.xfail
@pytest.mark.parametrize("data", random_double_number)
def test_api_5_get_single_user_with_double_number(data):
    ApiSteps().get_single_user_negative(user_number=data)