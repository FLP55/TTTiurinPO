import pytest

from api.data_for_api_test.data_for_tests import random_letter
from api.test_framework.steps_api import ApiSteps

@pytest.mark.xfail
@pytest.mark.parametrize("data", random_letter)
def test_api_4_get_single_user_with_invalid_data(data):
    ApiSteps().get_single_user_negative(user_number=data)